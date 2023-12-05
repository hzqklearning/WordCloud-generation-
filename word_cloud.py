#coding=utf-8

import wordcloud
from PIL import Image
import numpy as np
import jieba
from jieba import posseg
import os

print('请确保遮掩图片和要生成词云的文件都放在了正确的文件夹,生成的图片将保存到文件夹wordcloud_image里')
mask_image_name=input('请输入遮掩图片的文件名(包含扩展名),输入1表示默认\n')
if mask_image_name=='1':
    mask_image_name='test.png'
content_name=input('请输入要生成词云的txt文件(不包含扩展名txt),输入1表示默认\n')
if content_name=='1':
    content_name='斗罗大陆'

#导入遮掩图片并转化为ndarray形式   #颜色设置（设置为图片颜色)
mask_image_path='./mask_image/'+mask_image_name
mask_image=Image.open(mask_image_path)
mask_image=np.asarray(mask_image)
image_colors=wordcloud.ImageColorGenerator(mask_image)

#导入文本并对中文词进行分词处理
content_path='./txt_content/'+content_name+'.txt'
content=open(content_path,encoding='utf-8').read()
# content=jieba.cut(content)
# content=' '.join(content)
#提取名词 只考虑名词
jieba.load_userdict('./user_dict.txt')
content=posseg.cut(content)
t=''
for word,tag in content:
    if tag.find('n')!=-1 or tag=='x':
        t=' '.join([t,word])
content=t

#导入中文停词
stopwords=open('./cn_stopwords.txt',encoding='utf-8').read()
stopwords=stopwords.split('\n')


#词云生成并保存
wc=wordcloud.WordCloud(font_path='./SIMKAI.TTF',mask=mask_image,background_color='white',stopwords=stopwords,max_font_size=150,scale=5,color_func=image_colors)
wc.generate(content)
image=wc.to_image()
image.show()
files=os.listdir('./wordcloud_image')
file_num=len(files)
image.save(f'./wordcloud_image/{content_name}{file_num+1}.png')
