import time
import zenhan

def search(browser):
    #検索値入力
    query = input("商品名入力: ")

    #amazonHPへ
    browser.get('https://www.amazon.co.jp/')

    #検索値入力
    search = browser.find_element_by_id('twotabsearchtextbox')
    search.send_keys(query)

    #検索ボタン押す
    search_btn = browser.find_element_by_class_name('nav-input')
    search_btn.click()

    time.sleep(2)

    #商品一覧取得
    items = browser.find_elements_by_class_name('s-result-item')

    time.sleep(2)

    for num,item in enumerate(items):
        try:
            item_name = item.find_element_by_tag_name('h2').text
            print(num,':',item_name)
            print('-'*20)
        except:
            pass

    #商品の選択
    select_num = str(input('商品番号入力: '))
    select_item_num = 'result_'+ zenhan.z2h(select_num)

    time.sleep(1)

    select_item_html = browser.find_element_by_id(select_item_num)

    #その商品の詳細ページURL取得
    select_item = select_item_html.find_element_by_class_name('a-link-normal')
    select_item_url = select_item.get_attribute('href')
    #商品名取得
    select_item_name = select_item_html.find_element_by_tag_name('h2').text

    browser.get(select_item_url)

    time.sleep(1)

    return select_item_name
