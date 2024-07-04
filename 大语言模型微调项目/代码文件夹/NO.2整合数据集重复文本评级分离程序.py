''' 此代码用于对数据进行有效分割，筛选 误差数据 与 人工修正 数据。
误差数据的修正将使用：二分法筛选与替换。
'''
# 定义一个函数来处理文本文件，它接受输入文件路径和两个输出文件路径作为参数。


def process_text_file(input_file_path, output_file1_path, output_file2_path):
    # 初始化两个列表，用于存储将要写入两个输出文件的数据。
    output_data1 = []
    output_data2 = []

    # 使用 'with' 语句打开输入文件，确保文件在操作完成后正确关闭。
    # 'r' 表示读取模式，'encoding='gbk' 指定文件编码为 GBK。
    with open(input_file_path, 'r', encoding='gbk') as file:
        # 遍历文件中的每一行。
        for line in file:
            # 移除行尾的换行符并按空格最多分割两次，以防止评级中的空格影响分割。
            parts = line.strip().split(' ', 2)
            # 提取文本内容。
            text = parts[0]
            # 提取评级数量并转换为整数。
            count = int(parts[1])
            # 提取评级列表，将评级字符串分割为字符列表。
            ratings = [char for char in parts[2].split(',')]
            
            if count == 2:
                output_data2.append(f"{text} {count} {', '.join(ratings)}")
            else:
                # 使用字典推导式计算每个评级字符的出现次数。
                rating_counts = {char: ratings.count(
                    char) for char in set(ratings)}
                # 找到出现次数最多的评级字符。
                max_rating = max(rating_counts, key=rating_counts.get)

                # 检查出现次数最多的评级字符是否超过评级列表长度的一半。
                if rating_counts[max_rating] >= len(ratings) // 2:
                    output_data1.append(f"{text} {count} {', '.join(ratings)}")
                else:
                    output_data2.append(f"{text} {count} {', '.join(ratings)}")

    # 使用 'with' 语句打开第一个输出文件，以写入模式打开，并指定编码为 GBK。
    with open(output_file1_path, 'w', encoding='gbk') as output_file1:
        # 遍历 output_data1 列表，并将每个条目写入第一个输出文件，每个条目后跟一个换行符。
        for data in output_data1:
            output_file1.write(data + '\n')

    # 使用 'with' 语句打开第二个输出文件，以写入模式打开，并指定编码为 GBK。
    with open(output_file2_path, 'w', encoding='gbk') as output_file2:
        # 遍历 output_data2 列表，并将每个条目写入第二个输出文件，每个条目后跟一个换行符。
        for data in output_data2:
            output_file2.write(data + '\n')


# 定义输入文件和输出文件的路径。
input_file_path = 'SortedDuplicateText_False.txt'
output_file1_path = 'AutoCorrect_Text.txt'
output_file2_path = 'ManualCorrect_Text.txt'

# 调用 process_text_file 函数，传入文件路径。
process_text_file(input_file_path, output_file1_path, output_file2_path)
