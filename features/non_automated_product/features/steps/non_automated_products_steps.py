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

    link = 'https://www.adidas.com/us/nite-jogger-shoes/CG5950.html'
    item_field = context.browser.find_element_by_name('url').send_keys(link)
    time.sleep(5)  # sleeping 5 seconds so the item link is processed


@then(u'the product details should Not be loaded')
def product_details(context):
    
    category = context.browser.find_element_by_xpath('//*[@id="categoryContainer"]/div[1]/a').text
    assert category == 'Select Category'
    
    item_name = context.browser.find_element_by_xpath('//*[@id="categoryContainer"]/div[2]/input').text
    assert item_name == ''
    
    price = context.browser.find_element_by_xpath('//*[@id="product-price"]').text
    assert price == ''
    
    color = context.browser.find_element_by_xpath('//*[@id="product-color-text"]').text
    assert color == ''

    size = context.browser.find_element_by_xpath('//*[@id="product-size-text"]').text
    assert size == ''



@then(u'i have to insert all product details')
def product_details(context):

    category_field = context.browser.find_element_by_xpath('//*[@id="categoryContainer"]/div[1]/a').click()
    category = context.browser.find_element_by_xpath('//*[@id="category-container"]/div[5]').click()  # value of 'Cloth / Textile'

    item_name = context.browser.find_element_by_xpath('//*[@id="categoryContainer"]/div[2]/input').send_keys('Adidas')

    unit_price = context.browser.find_element_by_xpath('//*[@id="product-price"]').send_keys('100')

    color = context.browser.find_element_by_xpath('//*[@id="product-color-text"]').send_keys('black')

    size = context.browser.find_element_by_xpath('//*[@id="product-size-text"]').send_keys('40')
    time.sleep(2)

@then(u'i click on the Add item button')
def add_item(context):
    submit = context.browser.find_element_by_xpath('//*[@id="sb-site"]/div[1]/div[1]/div[2]/div/div[2]/form/div[2]/div/div[2]/input[1]').click()
    time.sleep(5)

@then(u'the cart icon should has positive value')
def cart_counter(context):
    cart_counter = context.browser.find_element_by_id('cartCounter')
    print(cart_counter.text)
    assert cart_counter.text ==  '1'

