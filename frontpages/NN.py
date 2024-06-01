from questions_json import codeblock
from streamlit_multipage import MultiPage
def page2(st,**state):
    st.header("2. Hidden Layer")

    st.markdown(r"""首先我们来学习input层和hidden层连接的几个参数：
    
    1. $权重矩阵 𝑊 $: $W_{ij} $表示从输入层第$ j $个节点到隐藏层第$ i $个节点的连接权重
    
    从输入节点与隐藏层节点之间有一个权重连接 W，其维度为 m×n，其中 m 是隐藏层节点的数量，n 是输入层节点的数量。
    
    2. $ 偏置向量 b $ : $b_i$ 表示计算隐藏层第$ i $ 个节点的加权和$ z_i $时添加的偏置值
    
    每个隐藏层节点有一个对应的偏置值 b，偏置值是一个向量，其维度为 m，与隐藏层节点的数量相同。
    
    3. $ 加权和z $ : 对于第 $ i $个节点，加权和计算公式如下：
    
    $ z_i = \sum_{j=1}^{n} W_{ij} x_j + b_i$
    
    4. $ 激活函数f $: 将加权和通过激活函数变换得到隐藏层输出$ a_i $，以引入非线性。常见的激活函数包括 Sigmoid、ReLU 和 Tanh 等。
    
    $ReLU:a_i = \text{ReLU}(z_i) = \max(0, z_i) $
    
    $Tanh: \tanh(z) = \frac{e^z - e^{-z}} {e^z + e^{-z}} $
    
    $ Sigmoid: \sigma(z) = \frac{1}{1 + e^{-z}} $
     
     """)

    st.text("A = f(WX+bw) 过程 ")

    st.divider()

    codeblock.set_codeblock("2")

    st.divider()

    st.subheader("前向算法")

    st.text("前向算法原理：z=，a= 等待补充;theta意义")

    st.divider()

    st.text("quiz3 -- 前向传播")

    st.divider()

    st.header("反向传播--调整参数W")

    st.markdown('''前面我们已经说到权重参数W和偏置值b是影响模型的性能关键，那么我们如何确定他们的值呢？
    这就用到反向传播的算法调整了
    
    确定初始参数 ->得到输出 -> 计算损失 -> 反向调整参数 -> 重复迭代''')


