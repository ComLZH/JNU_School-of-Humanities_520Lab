# 此代码用于实现微调json文件的标准化转换，转换为大模型可使用的JSONL格式。
import json

# 指定正确的文件编码（假设是UTF-8）
with open('modified_data.json', 'r', encoding='utf-8') as input_file:
    data = json.load(input_file)

# 将数据转换为JSONL格式并写入新文件
with open('Finnal_Data.jsonl', 'w', encoding='utf-8') as output_file:
    if isinstance(data, list):
        # 如果原始数据是一个包含多个对象的列表
        for item in data:
            json_line = json.dumps(item) + '\n'
            output_file.write(json_line)
    else:
        # 如果原始数据只有一个对象
        json_line = json.dumps(data) + '\n'
        output_file.write(json_line)