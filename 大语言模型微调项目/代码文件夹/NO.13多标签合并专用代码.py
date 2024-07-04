# 多标签合并专用代码
import pandas as pd

# 加载两个excel文件
df1 = pd.read_excel(r'C:\Users\LZH\Desktop\学姐数据\（R二元分类）InderenceData_Output.xlsx')
df2 = pd.read_excel(r'C:\Users\LZH\Desktop\学姐数据\updated_Multiple_Union_SQDA.xlsx') # 将'second_file.xlsx'替换为你第二个文件的文件名

# 使用Python字典进行快速映射和查询
mapping_dict = pd.Series(df1.AutoResults.values,index=df1.语录).to_dict()

# 结果应用到第二个文件
df2['AutoResult_R'] = df2['content'].map(mapping_dict).fillna("未找到匹配类别")

# 保存更新后的DataFrame到新的excel文件
df2.to_excel(r"C:\Users\LZH\Desktop\学姐数据\updated_Multiple_Union_SQDAR.xlsx", index=False) 