import sys
import os
import streamlit as st
import login

projectpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
if projectpath not in sys.path:
    sys.path.append(projectpath)
imagepath = projectpath + r'/images/'

from pages import home,CNN,NN

if __name__ == '__main__':
    while(True):
        if 'page' not in st.session_state:
            st.session_state['page'] = 'login'
        if st.session_state['page'] == 'home':
            st.session_state['page'] = home.page_home()
        elif st.session_state['page'] == 'login':
            st.session_state['page'] = login.login_page()
        elif st.session_state['page' ]== 'page1':
            st.session_state['page'] = CNN.page1()
        elif st.session_state['page'] == 'page2':
            st.session_state['page'] = NN.page_NN()