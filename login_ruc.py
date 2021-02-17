import requests
import sys
import io
import getpass
from selenium import webdriver

student_id = input('Enter your student id: ')
student_pwd = getpass.getpass('Enter you password: ')

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

browser = webdriver.PhantomJS()


url = r'https://go.ruc.edu.cn/srun_portal_pc?ac_id=6&theme=ruc'
browser.get(url)

browser.implicitly_wait(3)

username = browser.find_element_by_id('username')
username.send_keys(student_id)

password = browser.find_element_by_id('password')
password.send_keys(student_pwd)

login_button = browser.find_element_by_id('login-account')
login_button.click()

browser.save_screenshot('web_page.png')
# print(browser.page_source.encode('utf-8').decode())

browser.quit()
