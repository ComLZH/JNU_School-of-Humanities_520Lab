# 此代码用于实现对完成处理的训练集excel文件内部去重，提升数据集质量。

import pandas as pd # 导入pandas库实现调用Excel文件

# 读取Excel文件
df = pd.read_excel('2021combined_data_Correct.xlsx')

# 删除重复的行（依据第一列去重）
df = df.drop_duplicates(subset=df.columns[0], keep='first')

# 将新的数据框写入新的Excel文件
df.to_excel("2021combined_data_final.xlsx", index=False)