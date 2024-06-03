# -*- coding: utf-8 -*-
import streamlit as st
import subprocess
import tempfile
import sys
import os
import globals_
from database_ import methods
from database_ import methods
import questions_json.manage_question_json as mgjson
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


question_file = rootPath + r"\\questions_json\\questions.json"

def execute_code(code):
    try:
        # 创建一个临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py',mode='w',encoding='utf-8') as temp_file:
            temp_file.write(code)
            temp_file.flush()
            temp_filename = temp_file.name
            #print(temp_filename)
            #使用subprocess运行Python代码
            result = subprocess.run([sys.executable, temp_filename], capture_output=True, text=True, encoding="utf-8",
                                timeout=100)
            print(result.stdout)
            return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return "", "Error: Code execution timed out"
    except Exception as e:
        return "", str(e)
    finally:
        if temp_file and os.path.exists(temp_file.name):
            os.remove(temp_file.name)


def show_answer(answer:str):
    st.code(answer)


def judge_code(stdout:str, stderr:str, output:str):
    if stderr.strip():
        st.error(f"Error:\n {stderr}")
        return False
    elif output == stdout:
        return True
    else:
        st.info("输出 " + str(stdout) + '不符合预期输出')
        return False


def set_codeblock(stu_id:int=0,question_id:int=0,grade:int=10):
    (contents,pretext, answer,output) = mgjson.load_question(question_file,str(question_id))
    st.markdown(contents)

    code_input :str= st.text_area("Code Input",key='code_input',height=500,value=pretext)

    def reset_codeblock():
        st.session_state["code_input"] = pretext
    col1, col2 = st.columns(2)

    with col1:
        if st.button("提交"):
            if globals_.login_:
                if code_input.strip():
                    stdout, stderr = execute_code(code_input)
                    if judge_code(stdout, stderr, output):
                        methods.add_record(stu_id=stu_id,quiz_id=question_id,result="success")
                        methods.update_grade_delt(stu_id,grade)
                        st.success(f"提交成功!")
                    else:
                        methods.add_record(stu_id=stu_id,quiz_id=question_id,result="fail")
                        st.info("输出 " + str(stdout) + '不符合预期输出')
                else:
                    st.warning("code space empty!")
            else:st.warning("先登录才能提交代码")
    with col2:
        st.button("重置",on_click=reset_codeblock)
    if st.button("显示答案"):
        show_answer(answer)

if __name__ == "__main__":
    code = "print('Hello, world!')"
    print(execute_code(code))