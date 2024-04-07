from web3 import Web3
from dotenv import load_dotenv
import json,os,time


# 加载当前目录下的.env文件
load_dotenv()

# 现在可以像读取系统环境变量一样读取.env文件中的变量了
api_key = os.getenv('INFURA_PROJECT_ID')

# 使用Infura，替换为你的项目ID
infura_url = f"https://mainnet.infura.io/v3/{api_key}"

web3 = Web3(Web3.HTTPProvider(infura_url))

# 检查连接
if not web3.is_connected():
    print("连接失败，请检查你的节点或网络")
    exit()

print("连接成功，开始监听新区块...")

def attribute_dict_to_dict(obj):
    """
    递归将AttributeDict及其嵌套对象转换为普通字典。
    """
    if isinstance(obj, dict):
        return {k: attribute_dict_to_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [attribute_dict_to_dict(v) for v in obj]
    elif hasattr(obj, '__dict__'):
        return attribute_dict_to_dict(vars(obj))
    else:
        return obj
      
def save_block_data(block_data):
    """将区块数据追加到本地文件"""
    with open('block_data.json', 'a') as file:
        json.dump(block_data, file)
        file.write('\n')  # 添加换行符以分隔每个区块的数据

last_block_number = web3.eth.block_number

def add_block_to_json_file(block_data, filename='block_data.json'):
    # 将AttributeDict转换为普通字典
    block_data_dict = attribute_dict_to_dict(block_data)
    
    try:
        # 尝试读取现有数据
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # 如果文件不存在或为空，则开始一个新数组
        data = []
    
    # 添加新的区块数据到数组
    data.append(block_data_dict)
    
    # 将更新后的数据写回文件
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        
while True:
    current_block_number = web3.eth.block_number
    if current_block_number > last_block_number:
        print(f"发现新区块: {current_block_number}")
        block = web3.eth.get_block(current_block_number, full_transactions=True)
        block_data = dict(block)
        # 转换所有bytes类型数据为hex字符串，以便JSON序列化
        for key, value in block_data.items():
          if isinstance(value, bytes):
              block_data[key] = value.hex()
        block_data_dict = attribute_dict_to_dict(block_data)
        add_block_to_json_file(block_data_dict)
        last_block_number = current_block_number
    time.sleep(10)  # 每10秒检查一次新区块
