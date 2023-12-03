### 文件说明： ###
- mask_image存放了生成词云时用来遮掩的图片
- txt_content存放了需要生成词云的txt文档
- wordcloud_image存放了生成的词云图片
- word_cloud.py为生成词云图片的代码
- cn_stopwords.txt存放了中文常见停词
- test.ipynb用来测试使用
  
### 总结： ###
- jieba库可以用来进行中文分词，可以对中文字符串进行分词
- jieba.cut函数可以对中文字符串进行分词，返回包含分词的可迭代对象。jieba.posseg.cut函数不仅可以对中文字符串进行分词，还会包含分词的词性
- os.listdir函数可以返回目录里的文件名称列表

参考链接：  
1.https://github.com/fuqiuai/wordCloud/tree/master  
2.https://github.com/TommyZihao/zihaowordcloud  