import streamlit as st
from streamlit_multipage import MultiPage

def page_home(st,**state):
    st.title("Home")

    st.header("介绍")
    st.markdown('''
    在这个网站中，我们将从零开始学习神经网络。我们将会：
    1. 学习神经网络和卷积神经网络的数学原理
    2. 基于numpy搭建模型,完成手写数字识别任务
    
    接下来让我们开始吧！
    
    ''')
    #st.page_link(r"frontpages/NN.py",label="第一章 神经网络")