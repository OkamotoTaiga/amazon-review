from selenium import webdriver
import time
import search
import get_review as gr
import WC_output as wc

browser = webdriver.Chrome(executable_path='C:/driver/chromedriver.exe')

#商品の検索
select_item_name = search.search(browser)

time.sleep(5)

#レビューテキスト作成
text = gr.get_text(browser)
print('wordcloud作成中・・・')

time.sleep(5)

#テキスト加工
WC_text = wc.janome_analysis(text)

#wordcloud出力
wc.output_WC(WC_text, select_item_name)
