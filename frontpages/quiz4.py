import sys
import os
projectpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
curPath = os.path.abspath(os.path.dirname(__file__))
if projectpath not in sys.path:
    sys.path.append(projectpath)
from questions_json import codeblock
import globals_
from streamlit_multipage import MultiPage
import streamlit as st

def page4(st,**kwargs):
    st.header("4. 反向传播（Backpropagation）")
    st.markdown("""
    在上一章我们已经学会输入数据经过什么样的计算过程得到输出数据了，但是模型的权重$ W $ 和
    偏置值$ b $ 是如何确定的呢？
    如果将每个隐藏层的激活值反向表示为数据，有可能会发现每一个隐藏层实际上提取了有某些特征的数据(比如人脸识别中边缘、直角、五官等)
    这就是我们称深度学习为"黑盒"的原因，由于处理的数据量大且复杂，我们很难人为地为模型确定一个参数。
    这就要引入 ** 反向传播算法 ** 让程序通过迭代自己调整参数了
    """)
    st.markdown("""
    反向传播（Backpropagation）是神经网络训练中的一种核心算法，用于计算梯度并更新权重和偏置，以最小化损失函数。
    """)
    st.markdown("""
    1. 计算损失：根据输出值计算损失函数 $ L $ 衡量预测输出与真实标签之间的差距。
    """)
    st.image(globals_.ImagePath+r'error.png',caption="预测值y和真实的标签（z）相比较，计算误差δ")
    st.image(globals_.ImagePath+r'error2.png',caption="计算每个神经元的误差")
    st.image(globals_.ImagePath+r'error3.png',caption="反向计算每个神经元误差")
    st.markdown("""
    2. 反向计算梯度：从输出层开始，逐层向后计算梯度。使用链式法则，将损失函数对每一层参数的梯度进行计算。
    """)
    st.image(globals_.ImagePath+r'daoshu.png',caption="误差对权重求导")

    st.markdown("3. 更新权重和偏置：使用梯度下降算法，根据计算得到的梯度更新每一层的权重和偏置，以减少损失函数的值。")
    st.image(globals_.ImagePath+r'tidu.png',caption="梯度下降算法")
    st.divider()
    st.markdown("你可以通过以下代码理解反向传播的过程")
    st.code("""
    import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)
def forward_propagation(W1, b1, func_1, W2, b2, func_2, X):
    Z1 = W1.dot(X) + b1
    A1 = func_1(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = func_2(Z2)
    return Z1, A1, Z2, A2

def backward_propagation(X, Y, Z1, A1, Z2, A2, W1, b1, W2, b2, func1_derive,func2_derive,learning_rate=0.01):
    m = X.shape[1]
    dZ2 = A2-Y #误差
    dW2 = 1/m * np.dot(dZ2,A1.T)
    db2 = 1/m * np.sum(dZ2,axis=1,keepdims=True)

    dA1 = np.dot(W2.T, dZ2)
    dZ1 = dA1 * func1_derive(Z1)
    dW1 = 1 / m * np.dot(dZ1, X.T)
    db1 = 1 / m * np.sum(dZ1, axis=1, keepdims=True)

    W2 -= learning_rate*dW2
    b2 -= learning_rate*db2
    W1 -= learning_rate*dW1
    b1 -= learning_rate*db1

    return W1,b1,W2,b2

def compute_loss(A2,Y):
    return np.mean((A2 - Y) ** 2)


X = np.array([[1, 2, 3], [4, 5, 6]])  # 输入数据 (2, 3)
Y = np.array([[0, 1, 0]])             # 真实标签 (1, 3)

W1 = np.array([[0.1, 0.2],
               [0.3, 0.4],
               [0.5, 0.6],
               [0.7, 0.8]])  # 权重矩阵 (4, 2)
b1 = np.array([[0.1], [0.2], [0.3], [0.4]])  # 偏置向量 (4, 1)

W2 = np.array([[0.1, 0.2, 0.3, 0.4]])  # 权重矩阵 (1, 4)
b2 = np.array([[0.1]])  # 偏置向量 (1, 1)


Z1, A1, Z2, A2 = forward_propagation(W1, b1, sigmoid, W2, b2, sigmoid, X)

# 计算初始损失
initial_loss = compute_loss(A2, Y)
print("初始损失：", initial_loss)

# 反向传播并更新参数
W1, b1, W2, b2 = backward_propagation(X, Y, Z1, A1, Z2, A2, W1, b1, W2, b2,sigmoid_derivative,sigmoid_derivative)

# 前向传播
Z1, A1, Z2, A2 = forward_propagation(W1, b1, sigmoid, W2, b2, sigmoid, X)

# 计算更新后的损失
updated_loss = compute_loss(A2, Y)
print("更新后的损失：", updated_loss)
    """,language='python',line_numbers=True)

    codeblock.set_codeblock(globals_.user_id,4,10)
    st.divider()
if __name__ == '__main__':
    page4()