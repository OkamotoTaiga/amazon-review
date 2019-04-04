from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import time

def janome_analysis(text):
    '''
    text:レビューをまとめたもの
    return:形態素解析でwordcloudに入れるためのテキスト
    '''
    t = Tokenizer()
    words = t.tokenize(text)

    output = ''
    for w in words:
        word = w.base_form #単語基本形
        ps = w.part_of_speech.split(',')[0] #品詞抽出
        if ps in ['名詞','形容詞','動詞','副詞']:
            output += word+' '

    return output

def output_WC(WC_text, select_item_name):
    #除外する文字
    stop_words=[ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
                 u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
                 u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
                 u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'']

    fpath = 'C:\\Windows\\Fonts\\yumindb.ttf'
    wordcloud = WordCloud(background_color="white",font_path=fpath, width=900, height=500,stopwords=set(stop_words)).generate(WC_text)

    time.sleep(1)

    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    png = select_item_name+'.png'
    plt.savefig(png)
    plt.show()
