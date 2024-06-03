import sys
import os
projectpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
if projectpath not in sys.path:
    sys.path.append(projectpath)
from questions_json import codeblock
import globals_
from streamlit_multipage import MultiPage

def page2(st,**state):
    st.header("2. Hidden Layer")
    st.image(globals_.ImagePath+r'hiddenlayer.png')
    st.markdown(r"""首先我们来学习input层和hidden层连接的几个参数：""")

    st.markdown("""
    1. $权重矩阵 𝑊 $: 
        
        $W_{ij} $表示从输入层第$ j $个节点到隐藏层第$ i $个节点的连接权重，其维度为 m×n，其中 m 是隐藏层节点的数量，n 是输入层节点的数量。
    
    2. $ 偏置向量 b $ :
     
        $b_i$ 表示计算隐藏层第$ i $ 个节点的加权和$ z_i $时添加的偏置值,每个隐藏层节点有一个对应的偏置值 b，其维度为 m，与隐藏层节点的数量相同。
    
    3. $ 加权和z $ : 对于第 $ i $个节点，加权和计算公式如下：
    
    $$z_i = \sum_{j=1}^{n} W_{ij} x_j + b_i$$
    
    4. $ 激活值a $ :
        加权和 $ z $ 会通过激活函数得到隐藏层每个神经元的激活值 $ a $,表示神经元的输出。即：
        
        $$ a = f (z) ，其中{f}为激活函数$$
        
     """)

    st.subheader("""下面是三个常用的激活函数：""")
    st.image(globals_.ImagePath + r'activ.png', caption="三个常用激活函数")
    st.markdown(r"""
    1. $ sigma(x) = \frac{1}{1 + e^{-x}} $
    
    Sigmoid 函数的输出值在 (0, 1) 之间,常用于二分类问题的输出层，因为其输出值可以解释为正类的概率。
    
    在输入值非常大或非常小(>5或《-5)时，Sigmoid 函数的梯度会趋近于零，这会导致反向传播过程中的梯度消失问题，进而导致网络训练困难。
    
    2. $ \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} $
    
    Tanh 函数的输出值在 (-1, 1) 之间,Tanh 函数输出的均值接近于 0，梯度下降的收敛较快,
    常用于隐藏层，尤其是在需要中心化数据的情况下。
    
    虽然 Tanh 函数也存在梯度消失问题，但其程度较 Sigmoid 函数轻微。
    
    3. $ \text{ReLU}(x) = \max(0, x)  $
    
    ReLU 函数的输出值在 [0, ∞) 之间，在正值区域的梯度为 1，有效解决了梯度消失问题，并且简单高效，适合深层网络。
    
    当输入为负时，ReLU 函数的输出为零，这会导致一些神经元永远不会被激活，称为“死亡 ReLU”问题。
    
    ReLU 是目前最常用的隐藏层激活函数，适用于各种类型的神经网络，包括卷积神经网络（CNN）和循环神经网络（RNN）。
    """)



    st.divider()
    st.text("接下来我们完成激活值a的计算，即A = f(WX+bw) 过程 ")

    st.subheader("quiz2")

    codeblock.set_codeblock(globals_.user_id,2,10)

    st.divider()



import streamlit as st
if __name__ == '__main__':
    page2(st)

