// 注意：此空间存储的是江南大学人文学院教育技术专业520实验室相关文件

/*在“代码文件夹”中，按照序号存储的是针对ChatGLM3-6B模型进行微调的前置语料处理程序。
在使用时，按照序号与命名顺序进行依次运行，每段程序都会输出对应的结果，实现过程可查。
当初始的文件格式按照要求格式准备后，接下来的步骤可以直接通过连续运行程序来实现，不需要进行额外的设置。
（PS：目前在类别补充那里还需要手动调整，其它已经完成）
*/

/*如果使用W老师提供的服务器，可以直接转移最终生成的“Finnal_Data.jsonl”文件并直接运行。（环境与相关微调程序已经部署好了）
如果使用自建服务器或者其它平台服务器，注意路径的适配！！！
*/
2024.07.02 LZH

/*在“LDA主题模型”文件夹中，包含了以下必须文件：
1、待分析文本文件"all the data.xlsx"（此文件中按照预设的格式存储你需要进行LDA分析的文本）
2、补充进行文本分割文件"自定义词库.txt"（此文件中按照预设的格式存储你需要进行分词的自定义词库）
3、中文停用词文件"cn_stopwords.txt"（此文件中存储了中文停用词用于过滤分析文本，同时进行分词保留长度的变量位于"LDA_Model_.py"脚本中）
4、LDA模型与可视化实现脚本"LDA_Model_.py"（此文件用于执行LDA模型的训练与可视化，同时进行文本分词、停用词过滤与分割长度过滤操作）

生成的可视化文件将保存在"lda_visualization.html"中，你可以通过浏览器打开浏览状态。

如果你是第一次使用LDA主题模型，请你首先确认"LDA_ModolEnviroment.yaml"文件中的依赖项已经完成安装。
（如果使用anaconda，你可以通过运行"conda env create -f LDA_ModolEnviroment.yaml"来安装依赖项）
*/
2024.11.04 LZH