# 此代码用于实现对Json格式的微调数据集信息补全。
import json

# 假设您有一个名为 'output.json' 的文件
with open('output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

'''# 定义要拼接的字符串
prefix_prompt = "文本分类包含A/B/C/D/E/F/G/H/I/J/K共十一种类别，请判断下面这句话的类别："
prefix_response = "这句话的类别属于："'''

# 学姐训练类别（自定义类别点：）
prefix_prompt = "文本特征分类包含R/False共两种类别，请判断下面这句话的类别："
prefix_response = "这句话的类别属于："

# 遍历数据并对每一项进行处理
for item in data:
    # 修改 prompt
    if isinstance(item['prompt'], str):
        item['prompt'] = prefix_prompt + item['prompt']
    else:
        item['prompt'] = prefix_prompt + str(item['prompt'])

    # 修改 response
    if isinstance(item['response'], str):
        item['response'] = prefix_response + item['response']
    else:
        item['response'] = prefix_response + str(item['response'])

# 将处理后的数据写回新的.json文件
with open('modified_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)