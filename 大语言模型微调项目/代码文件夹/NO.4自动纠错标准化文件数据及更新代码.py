# 此段代码实现将自动纠错txt文件中的变更数据同步到Excel数据集中。

import pandas as pd

#读取TXT文件，将其转化为一个字典，键为“文本内容”，值为“文本类别”
txt_dict = {}
with open("Processed_AutoCorrect_Text.txt", "r", encoding='gbk') as f:
    for line in f:
        line = ' '.join(line.split())  # Replace multiple spaces with one space
        line_parts = line.strip().split(" ")
        txt_dict[line_parts[0]] = line_parts[1]

#读取Excel
df = pd.read_excel("2021combined_data.xlsx")

#遍历每个单元格
for index, row in df.iterrows():
    text_content = row['文本数据']
    text_category = row['分类等级']
    
    #判断单元格中的内容在TXT文件中是否存在
    if text_content in txt_dict.keys():
        if txt_dict[text_content] != text_category:
            df.loc[index, '分类等级'] = txt_dict[text_content] # 替换不同的文本类别

#重新写入Excel文件
df.to_excel("2021combined_data_modified.xlsx", index=False)