from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_browser = webdriver.Chrome(ChromeDriverManager().install())

chrome_browser.get(
    'http://localhost:3000')


query_search = chrome_browser.find_element_by_class_name('form-control')

query_search.send_keys('emtrak')

see_more_button = chrome_browser.find_element_by_class_name('card-button')

see_more_button.click()

go_back_button = chrome_browser.find_element_by_class_name(
    'product-page-button')

go_back_button.click()

print('All is Good!')

chrome_browser.quit()
