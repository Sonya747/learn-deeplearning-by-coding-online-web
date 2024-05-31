import streamlit as st
import subprocess
import tempfile
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from database import methods
import questions_json.manage_question_json as mgjson

question_file = rootPath + r"\\questions_json\\questions.json"

def execute_code(code):
    try:
        # 创建一个临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_file:
            temp_file.write(code.encode('utf-8'))
            temp_file.flush()
            temp_filename = temp_file.name
        # 使用subprocess运行Python代码
        result = subprocess.run([sys.executable, temp_filename], capture_output=True, text=True, encoding="utf-8",
                                timeout=10)
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return "", "Error: Code execution timed out"
    except Exception as e:
        return "", str(e)
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)


def show_answer(answer:str):
    st.code(answer)


def judge_code(stdout:str, stderr:str, output:str):
    if stderr.strip():
        st.error(f"Error:\n {stderr}")
    elif output == stdout:
        st.success(f"提交成功!")
        return True
    else:
        st.info("输出 " + str(stdout) + '不符合预期输出')
        return False


def set_codeblock(question_id:str):
    (contents,pretext, answer,output) = mgjson.load_question(question_file,question_id)
    st.markdown(contents)

    code_input = st.text_area("Code Input",key='code_input',height=500,value=pretext)

    def reset_codeblock():
        st.session_state["code_input"] = pretext
    col1, col2 = st.columns(2)

    with col1:
        if st.button("提交"):
            if code_input.strip():
                stdout, stderr = execute_code(code_input)
                if judge_code(stdout, stderr, output):
                    return True
            else:
                st.warning("code space empty!")
    with col2:
        st.button("重置",on_click=reset_codeblock)
    if st.button("显示答案"):
        show_answer(answer)

if __name__ == "__main__":
    set_codeblock("1")
