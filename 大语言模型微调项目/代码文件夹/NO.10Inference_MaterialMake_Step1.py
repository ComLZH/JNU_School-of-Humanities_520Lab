# 本代码在于实现excel文件验证集的制作。逻辑为：标准数据集——标准格式
# 目前已完成转换添加提示词。

# 导入pandas库以实现对excel文件的处理
import pandas as pd


'''#读取Excel文件（这里我按照你的情况，假设B列名为'文本类别'）
df = pd.read_excel("（验证集）725条第八组1-9.xlsx")
#为B列的每一个数据最前端拼接文本
df['语录'] = '文本分类包含M1/M2/M3共三种类别，请判断下面这句话的类别：' + df['语录']'''

# 学姐数据集验证代码（临时）
df = pd.read_excel("学姐验证数据集.xlsx")
df['语录'] = '文本特征分类包含R/False共两种类别，请判断下面这句话的类别：' + df['语录']

#将数据框写入新的Excel文件
df.to_excel("InferenceData.xlsx", index=False)