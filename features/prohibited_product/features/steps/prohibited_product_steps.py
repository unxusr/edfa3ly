from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

@given(u'i have a prohibited product link and go to cart page')
def open_cart(context):

    # Init web driver
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(5)
    context.browser.get("https://www.edfa3ly.com/cart")
    time.sleep(3)
    assert context.browser.current_url == "https://www.edfa3ly.com/cart"

@when(u'i add the link')
def add_link(context):

    link = 'https://www.abercrombie.com/shop/wd/p/skinny-suede-belt-41330319?categoryId=12266&seq=02&faceout=prod1'
    item_field = context.browser.find_element_by_name('url').send_keys(link)

@then(u'i should be notified that this product is not available')
def prohibted_product(context):
    
    time.sleep(3)
    message = context.browser.find_element_by_tag_name('label')
    print(message.text)
    assert message.text == "we apologize, store is not available at this moment"
    
