# 此段代码用于实现对输出文件进行自动准确率计算。

import pandas as pd

# 加载Excel文件,此处为目标Excel路径，注意标准格式。
df = pd.read_excel('（计算用）（毕设三分类V2.0-150）InderenceData_Output.xlsx')

# 找到相同的行并保存到新的Excel文件中
same_df = df[df['HumanResults'] == df['AutoResults']]
same_df.to_excel('Output_SameJudge.xlsx', index=False)

'''
# 从原始DataFrame中删除相同的行
df = df[df['HumanResults'] != df['AutoResults']]
'''

# 创建一个空字典来保存结果
results_dict = {}

# 对于每一行，计算非空数据
for _, row in df.iterrows():
    auto_result = row["AutoResults"]
    human_result = row["HumanResults"]
    if auto_result not in results_dict:
        results_dict[auto_result] = {}
    for letter in human_result:
        if letter in results_dict[auto_result]:
            results_dict[auto_result][letter] += 1
        else:
            results_dict[auto_result][letter] = 1

# 保存结果到txt文件中
with open('分类偏离报告.txt', 'w') as f:
    for result, freq_dict in results_dict.items():
        f.write(f"For AutoResults '{result}', the frequency of letters in HumanResults is:\n")
        for letter, freq in freq_dict.items():
            f.write(f"Letter: {letter}, Frequency: {freq}\n")
        f.write("\n")