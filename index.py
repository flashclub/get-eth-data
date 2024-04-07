from web3 import Web3
import json,ast
# 连接到以太坊节点，这里使用的是Infura的主网节点
# 您需要替换 YOUR_INFURA_PROJECT_ID 为您的 Infura 项目ID
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))

# 检查连接是否成功
if web3.is_connected():
    print("连接成功!")
else:
    print("连接失败.")

# 获取最新区块的信息
latest_block = web3.eth.get_block('latest')

# 自定义JSON序列化函数
def serialize_block(block):
    processed_block = {}
    for key, value in block.items():
      if key == 'transactions':
        processed_transactions = []
        print('transactions')
        for tx in value:
          # 尝试将字符串形式的字节数据转换为真正的字节串，然后转为十六进制
          print('tx: ', tx)
          try:
            # 使用ast.literal_eval安全地评估字符串形式的字节数据
            # real_bytes = ast.literal_eval(tx)
            processed_transactions.append(tx.hex())
          except ValueError:
            # 如果转换失败，保留原始值
            processed_transactions.append(tx)
        processed_block[key] = processed_transactions
      # 特别处理bytes类型，将其转换为十六进制字符串
      elif isinstance(value, bytes):
          print('value: ', value)
          processed_block[key] = value.hex()
      else:
          processed_block[key] = value
    return processed_block

# 将区块信息转换为JSON格式
block_info_json = json.dumps(serialize_block(dict(latest_block)), default=str)

# 保存到本地文件
with open('latest_block_info.json', 'w') as json_file:
    json_file.write(block_info_json)
    

# 获取最新区块的交易数量
transaction_count = web3.eth.get_block_transaction_count(latest_block['number'])
print(f"最新区块的交易数量: {transaction_count}")
