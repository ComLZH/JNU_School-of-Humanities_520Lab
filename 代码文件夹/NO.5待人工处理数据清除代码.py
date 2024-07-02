# 这份代码实现将需要人工处理的重复数据从数据集中删除（暂无对应修正方法）。
import pandas as pd
# 读取新的TXT文件，将需要删除的内容添加到集合中
deletion_set = set()
with open("ManualCorrect_Text.txt", "r", encoding='gbk') as f:
    for line in f:
        line = ' '.join(line.split())  # 不论文本内容和分类间有多少个空格，都根据单个空格来分割
        line_parts = line.strip().split(" ")
        deletion_set.add(line_parts[0])

#读取Excel
df = pd.read_excel("2021combined_data_modified.xlsx")

#过滤掉需要删除的行
df = df[~df['文本数据'].isin(deletion_set)]

#重新写入Excel文件
df.to_excel("2021combined_data_Correct.xlsx", index=False)