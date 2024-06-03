import sys
import os
projectpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
if projectpath not in sys.path:
    sys.path.append(projectpath)
from questions_json import codeblock
import globals_
from streamlit_multipage import MultiPage

def page3(st,**kwargs):
    st.header("3. 前向传播算法")
    st.markdown("""前向传播算法（Forward Propagation）用于计算网络的输出。下面是前向传播的简要过程：""")
    st.markdown("""
            1. 接受输入：输入层接受输入数据 𝑋
    
            2. 计算隐藏层加权和 $ Z $
    
            3. 应用激活函数得到隐藏层激活值 $ A $
    
            4. 计算输出层加权和 $ Z $,其中 $ Z_k = W_x * A + b_k $ ,其中 $ W_k $是隐藏层到输出层第 k 个神经元的权重向量
    
            5. 应用激活函数得到输出层激活值 $ σ_out $ 
    
            实际上输出层激活值计算过程与隐藏层相同
        """)

    st.markdown("在上一节我们已经完成了激活值计算的定义，下面我们利用这几个函数构造一个简单的模型")
    st.divider()
    codeblock.set_codeblock(globals_.user_id, 3, 10)
    st.divider()


if __name__=='__main__':
    import streamlit as st
    page3(st)