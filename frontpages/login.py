import os
import sys
projectpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if projectpath not in sys.path:
    sys.path.append(projectpath)

from database import database,methods
from streamlit_multipage import MultiPage
def login_page(st,**state):
    # Streamlit界面
    st.title("用户登录和注册")

    menu = ["登录", "注册"]
    choice = st.sidebar.selectbox("选择操作", menu)

    if choice == "注册":
        st.subheader("注册新用户")

        stu_id = st.text_input("学号")
        stu_name = st.text_input("姓名")
        stu_class = st.text_input("课程号")
        user_name = st.text_input("用户名(建议为姓名)")
        user_password = st.text_input("密码",type="password")
        if st.button("注册"):
            if user_name and user_password:
                try:
                    #methods.register_student(id=int(stu_id),name=user_name,class_id=int(stu_class),grade=0)
                    methods.register_user(user_id=int(stu_id), username=user_name, password=user_password,class_id=stu_class)
                    st.success("注册成功！")
                    return "home"
                except Exception as e:
                    st.error(f"{str(e)}\n 请检查表单信息或联系工作人员")
            else:
                st.error("请填写用户名和密码")

    elif choice == "登录":
        st.subheader("用户登录")
        user_id = st.text_input("学号")
        password = st.text_input("密码", type='password')
        if st.button("登录"):
            try:
                methods.login_user(int(user_id),password,)
                st.success("欢迎登入")
                return "home"
            except Exception as e:
                raise e
