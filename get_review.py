import time

def get_text(browser):

    #全て表示へGO
    all_review = browser.find_element_by_css_selector('#reviews-medley-footer > div.a-row.a-spacing-large > a')
    all_review_url = all_review.get_attribute('href')
    browser.get(all_review_url)

    time.sleep(1)

    all_text = ''
    #次ページがある限りレビュー取得
    print('レビュー取得中・・・')
    while True:
        try:
            #レビュー取得
            reviews = browser.find_elements_by_class_name('review-text')
            #レビュー内のテキストを抽出
            for cls in reviews:
                text = cls.text
                text = text.replace('\n','').replace('\t','')
                all_text += text

            next = browser.find_element_by_class_name('a-last')
            next_url = next.find_element_by_tag_name('a').get_attribute('href')
            browser.get(next_url)

            time.sleep(3)


        except:
            print('レビュー取得おわり')
            break
    browser.quit()

    return all_text
