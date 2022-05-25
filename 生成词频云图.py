import wordcloud
import matplotlib.pyplot as plt
from imageio import imread
big_pic=imread('star.jpg')
f=open("三国演义词频.txt",'r',encoding='utf-8')
text=f.read()
f.close()
wcloud=wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\simhei.ttf',
                        background_color='white',width=1000,
                        max_words=500,
                        mask=big_pic,
                        height=860,margin=2).generate(text)
wcloud.to_file('三国演义cloud.png')
plt.imshow(wcloud)
plt.axis('off')
plt.show()
 
