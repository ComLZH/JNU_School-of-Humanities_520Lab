# 这份代码实现的功能：转换自动化整理后的数据集，生成可以为之后的Excel修正操作的指导数据文件。
# 定义一个函数来处理自动纠正文本文件，它接受输入文件路径和输出文件路径作为参数。
def process_autocorrect_text_file(input_file_path, output_file_path):
    # 初始化一个空列表，用于存储将要写入输出文件的数据。
    output_data = []

    # 使用 'with' 语句打开输入文件，确保文件在操作完成后正确关闭。
    # 'r' 表示读取模式，'encoding='gbk' 指定文件编码为 GBK。
    with open(input_file_path, 'r', encoding='gbk') as file:
        # 遍历文件中的每一行。
        for line in file:
            # 移除行尾的换行符并按空格最多分割两次，以防止评级中的空格影响分割。
            parts = line.strip().split(' ', 2)
            # 提取文本内容。
            text = parts[0]
            # 提取评级列表，将评级字符串分割为字符列表。
            ratings = [char for char in parts[2].split(',')]

            # 使用字典推导式计算每个评级字符的出现次数。
            rating_counts = {char: ratings.count(char) for char in set(ratings)}
            # 找到出现次数最多的评级字符。
            max_rating = max(rating_counts, key=rating_counts.get)

            # 将文本和出现次数最多的评级字符添加到 output_data 列表。
            output_data.append(f"{text} {max_rating}")

    # 使用 'with' 语句打开输出文件，以写入模式打开，并指定编码为 GBK。
    with open(output_file_path, 'w', encoding='gbk') as output_file:
        # 遍历 output_data 列表，并将每个条目写入输出文件，每个条目后跟一个换行符。
        for data in output_data:
            output_file.write(data + '\n')

# 定义输入文件和输出文件的路径。
input_file_path = 'AutoCorrect_Text.txt'
output_file_path = 'Processed_AutoCorrect_Text.txt'

# 调用 process_autocorrect_text_file 函数，传入文件路径。
process_autocorrect_text_file(input_file_path, output_file_path)