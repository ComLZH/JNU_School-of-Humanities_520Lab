# -*- coding: utf-8 -*-
#语料预处理程序：基础处理——特述符号（@）与关联对象去除。

import pandas as pd

# 1. 读取Excel文件。
file_path = 'C:/Users/user/Desktop/6.xlsx'  #注意跨平台的通用性，统一正斜杠/。
df = pd.read_excel(file_path, engine='openpyxl')

# 2. 处理B列的单元格。
# 定义一个函数来处理单元格中的文本。
def process_cell(text):
    if '@' in text:
        # 找到第一个@符号的位置。
        idx = text.index('@')
        # 去除@符号以及之后的内容，直到遇到空格。
        return text[:idx].rstrip()
    else:
        return text

# 应用该函数到B列。注意：其它列名称时需更换“B”为目标列名称。
df['B'] = df['B'].apply(process_cell)

# 3. 将处理的结果重新填充到读取的单元格。
#注意是对原始文件的更改，做好初期备份。
df.to_excel(file_path, index=False, engine='openpyxl')
