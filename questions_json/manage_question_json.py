"""
对questions.json的操作
增：增加题目
删：删除题目
改：更新题目答案，输出
查：查询题目
"""
import json
import tempfile
import subprocess
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
json_file = rootPath + "\\questions_json\\questions.json"

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

def load_data(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            questions = json.load(file)
    except FileNotFoundError:
        questions = {}
    return questions

def load_question(json_file:str, question_id:str)-> (str,str, str, str):
    data = load_data(json_file)
    contents = data[question_id]['contents']
    pretext = data[question_id]['pretext']
    answer = data[question_id]['answer']
    output = data[question_id]['output']
    return (contents,pretext, answer,output)

def load_code(json_file, question):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            questions = json.load(file)
            code=questions[question]['answer']
    except FileNotFoundError:
        print("filenotfound")
        code = ""
    return code

def save_questions(question_file,questions:str):
    with open(question_file, 'w',encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False,indent=4)


def update_output(json_file,question:str,output:str):
    questions = load_data(json_file)
    if question in questions:
        questions[question]['output'] = output
        save_questions(json_file,questions)
        print(f"updated output: {question}")
    else:print("题目不存在")


def update_answer(json_file,question:str,answer:str):
    questions = load_data(json_file)
    if question in questions:
        questions[question]['answer'] = answer
        save_questions(json_file,questions)
        print(f"updated answer: {question}")
    else:print("题目不存在")


def add_question(json_file,question:str,contents:str,pretext:str,answer:str,output:str):
    questions = load_data(json_file)
    if question in questions:
        print("题目已经存在")
    else:
        questions[question] ={
            'contents':contents,
            'pretext':pretext,
            'answer':answer,
            'output':output
        }
    save_questions(json_file,questions)






if __name__ == "__main__":
    with open(json_file, 'r',encoding='utf-8') as f :
        datas = json.load(f)
    print(datas)