#数据集质量检查代码：检查重复出现且错误编码的文本数据
import pandas as pd
from collections import Counter

# 读取Excel文件
df = pd.read_excel('2021combined_data.xlsx')

# 找到A列中所有重复的文本
duplicates = df[df['文本数据'].duplicated(keep=False)]

# 检查重复文本对应的B列等级判断是否一致
inconsistent_rows = duplicates[duplicates.groupby('文本数据')['分类等级'].transform('nunique') > 1]

# 将不一致的文本和对应的分类等级写入到TXT文件中
with open('DuplicateText_False.txt', 'w') as f:
    for _, row in inconsistent_rows.iterrows():
        f.write(f"{row['文本数据']} {str(row['分类等级'])}\n")

# 读取TXT文件中的数据
with open('DuplicateText_False.txt', 'r') as f:
    data = f.readlines()

# 统计每个文本的出现次数
counter = Counter([line.split()[0] for line in data])

# 按照出现次数排序
sorted_data = sorted(counter.items(), key=lambda x: x[1], reverse=True)

# 将排序后的数据写入到新的TXT文件中
with open('SortedDuplicateText_False.txt', 'w') as f:
    for text, count in sorted_data:
        # 找到文本对应的分类等级
        classification_levels = [line.split()[1] for line in data if line.split()[0] == text]
        # 将文本数据、出现次数和分类等级一起写入TXT文件
        f.write(f"{text} {str(count)} {', '.join(classification_levels)}\n")

# 计算文本总数
total_count = sum(counter.values())

# 输出文本总数
print(f"文本总数：{total_count}")