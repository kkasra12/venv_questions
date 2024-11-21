from wordcloud import WordCloud
from matplotlib import pyplot as plt

text = "Python data science AI machine learning"
wc = WordCloud().generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
