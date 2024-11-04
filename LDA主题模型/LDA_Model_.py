import pandas as pd
import jieba
from gensim import corpora, models
from gensim.models.ldamodel import LdaModel
import pyLDAvis
import pyLDAvis.gensim

# 读取数据
try:
    papers = pd.read_excel(r"all the data.xlsx", names=['content'])
    print(papers.head())
except FileNotFoundError:
    print("文件未找到，请检查文件路径。")
    exit()

# 加载自定义词库
custom_dict = set()  # 使用集合来去重
with open('自定义词库.txt', 'r', encoding='utf-8') as f:
    for line in f:
        word = line.strip()
        custom_dict.add(word)

# 将自定义词库中的词加入jieba词库
for word in custom_dict:
    jieba.add_word(word)

# 读取停用词
stopLists = list(pd.read_csv('cn_stopwords.txt', names=['w'], encoding="UTF-8")['w'].dropna())

# 创建字典和语料库
filtered_words_list = []
for content in papers.content:
    words = jieba.lcut(content)
    # 过滤停用词和长度大于3的词，保留自定义词库中的长度小于3的词（筛查可以调整这里的数字）
    filtered_words = [
        word for word in words
        if word not in stopLists and (len(word) > 3 or word in custom_dict)
    ]
    filtered_words_list.append(filtered_words)

# 创建字典和语料库
wordDict = corpora.Dictionary(filtered_words_list)
corpus = [wordDict.doc2bow(words) for words in filtered_words_list]

# 创建 LDA 模型
ldaModel = LdaModel(corpus, id2word=wordDict, num_topics=5, alpha=5, eta=0.1)

# 可视化 LDA 主题
topic_data = pyLDAvis.gensim.prepare(ldaModel, corpus, dictionary=wordDict)

# 导出为 HTML 文件
pyLDAvis.save_html(topic_data, 'lda_visualization.html')

print("可视化结果已保存为 lda_visualization.html，请在浏览器中查看。")