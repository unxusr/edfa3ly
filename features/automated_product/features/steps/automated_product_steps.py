from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

@given(u'i have a link and go to the cart page')
def open_cart(context):

    # Init web driver
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(5)
    context.browser.get("https://www.edfa3ly.com/cart")
    time.sleep(3)

@when(u'i insert the link in the item url')
def add_link(context):

    link = 'https://www.6pm.com/p/product/9409514'
    item_field = context.browser.find_element_by_name('url').send_keys(link)
    time.sleep(3)

@then(u'the product details should be loaded')
def product_details(context):

    details = context.browser.find_element_by_class_name('categoryButton').text
    assert details == 'Shoes'

@then(u'i have to insert color and size options')
def product_details(context):

   color = Select(context.browser.find_element_by_xpath('//*[@id="cart-basic-box"]/div[3]/div[5]/div[2]/div/select'))
   color.select_by_index(1)
   size = Select(context.browser.find_element_by_xpath('//*[@id="cart-basic-box"]/div[3]/div[5]/div[3]/div/select'))
   size.select_by_index(3)

@then(u'i click on the Add item button')
def submit_item(context):

    submit = context.browser.find_element_by_xpath('//*[@id="sb-site"]/div[1]/div[1]/div[2]/div/div[2]/form/div[2]/div/div[2]/input[1]').click()
    time.sleep(2)

@then(u'the cart icon should has positive value')
def check_cart(context):

    cart_counter = context.browser.find_element_by_id('cartCounter')
    assert cart_counter.text ==  '1'
