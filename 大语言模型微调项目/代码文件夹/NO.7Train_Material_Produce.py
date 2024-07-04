#分步处理数据集文件，有助于掌握各阶段状态。
#此文件为数据处理第一步：实现转换为json文件。
import pandas as pd

# 读取Excel文件
df = pd.read_excel('2021combined_data_final.xlsx', engine='openpyxl')  # 如果是xls文件，则使用 'xlrd'

# 确保数据只有两列，并且列名为'A'和'B'
df.columns = ['prompt', 'response']  # 如果列名不是'A'和'B'，请替换为实际列名

# 转换为字典列表
data_list = df.to_dict(orient='records')

# 将字典列表转换为json格式
import json
json_data = json.dumps(data_list, indent=4)

# 写入到json文件中
with open('output.json', 'w') as f:
    f.write(json_data)