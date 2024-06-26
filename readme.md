# 获取 eth 链上数据

## 前置条件

注册 Infura，获取 INFURA_PROJECT_ID

新建.env 并参照 .env.example 设置环境变量

安装相应依赖
`pip install web3`
`pip install python-dotenv`

## 运行脚本

`python3 index3.py`

脚本会 10s 检测一次区块

## 分析数据

每个区块有 4000 多行数据，简略分析如下（from AI）：

这个区块的数据提供了关于以太坊区块链的一系列详细信息。让我们逐一分析关键点：

1. **基本费用（baseFeePerGas）**: 12997329537 - 这是该区块中每单位 gas 的基本费用。这个数值反映了网络当前的拥堵程度，基本费用越高，意味着网络越拥堵。

2. **难度（difficulty）**: 0 - 在以太坊的 PoS（Proof of Stake，权益证明）机制下，这个值通常为 0，因为它是一个遗留字段，主要用于 PoW（Proof of Work，工作量证明）机制。

3. **额外数据（extraData）**: "0x6265617665726275696c642e6f7267" - 这通常包含矿工或验证节点的附加信息。在这个例子中，它可能是一个编码后的消息或标识。

4. **gas 限制（gasLimit）**: 30000000 - 这是该区块允许的最大 gas 量，用于限制一个区块中所有交易消耗的 gas 总量。

5. **已使用的 gas（gasUsed）**: 15155904 - 这表示在该区块中已经被所有交易消耗的 gas 总量。

6. **区块哈希（hash）**: "0x3bcfa..." - 每个区块都有一个唯一的哈希值，用于在区块链网络中唯一标识该区块。

7. **矿工（miner）**: "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5" - 这是挖出该区块的验证节点（在 PoS 机制中称为验证节点而不是矿工）的地址。

8. **区块编号（number）**: 19603186 - 这是该区块在整个区块链中的序号。

9. **时间戳（timestamp）**: 1712485271 - 这是该区块生成的时间戳，通常表示为自 1970 年 1 月 1 日以来的秒数。

10. **交易（transactions）** - 区块包含了一个交易的列表。每个交易都有自己的详细信息，如发送者、接收者、gas 价格、交易值等。

11. **提款（withdrawals）** - 这个字段特定于以太坊 2.0，涉及到质押和验证节点的奖励提取。每个提款有提款地址、金额、索引和验证节点索引。

这个区块的数据反映了以太坊网络在一个特定时间点的状态，包括网络的拥堵程度、交易活动、验证节点的活动等。如果你有特定的问题或需要进一步的解释，请告诉我！

## 代码

所有代码均来自 AI

## 注意
实际测试，1分钟获取到6个区块，占用800KB左右，预估24小时占用1GB左右磁盘空间

长时间运行注意磁盘空间

## 其他

index.py index2.py 为学习过程，无实际用途，仅供参考
