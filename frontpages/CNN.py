import streamlit as st
from streamlit_multipage import MultiPage
import sys
import os

projectpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
if projectpath not in sys.path:
    sys.path.append(projectpath)
import globals_
from questions_json import codeblock
from globals_ import ImagePath

def page1(st=st,**state):
    st.title("神经网络")
    st.markdown("""
                传统的Neural Network 有三层: input Layer,Hidden Layer,Output Layer,层与层之间节点的连接状态通过 **权重$w$** 来体现
                
                接下来我们将分别学习三层的功能和实现，亲手搭建一个自己的反馈型神经网络,解决识别手写数字问题
                
                """)

    st.image(ImagePath + r"BP.png", caption="经典的BP神经网络结构")

    st.markdown("""
    值得注意的是，在学习原理的阶段，我们不会用到任何的现有框架(pyplot,tensorflow,keras等)，而是基于 **numpy** 库，用矩阵进行运算
    """)

    st.header("1. Input Layer")

    st.markdown("""顾名思义，这一层的功能是传递来自外界的信息进入神经网络中，比如图片信息，文本信息。同时，这层需要完成数据预处理的工作，其中包括：
        
        - 去均值：把输入数据各个维度都中心化为0,如下图所示，其目的就是把样本的中心拉回到坐标系原点上。
        - 归一化：幅度归一化到同样的范围，即减少各维度数据取值范围的差异而带来的干扰
        - PCA/白化：PCA/白化；用PCA降维；白化是对数据各个特征轴上的幅度归一化
        - OneHot编码：将属性数据转换为二进制编码
        
    """)

    st.image(ImagePath + r"BP.png", caption="去均值与归一化效果图")
    st.image(ImagePath + r"meanquit.png", caption="去相关和白化效果图")
    st.divider()
    codeblock.set_codeblock(globals_.user_id,1,10)
    st.divider()




