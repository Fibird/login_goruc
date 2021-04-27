# ==============================================
# Author: Liu Chaoyang
# Email: chaoyanglius@outlook.com
# reference: https://pypi.org/project/selenium/,
# https://www.geeksforgeeks.org/how-to-install-selenium-in-python/,
# https://pythonbasics.org/selenium-firefox-headless/
# ==============================================
import sys, io
import getpass
from selenium import webdriver

def login_by_firefox():
    firefox_options = webdriver.firefox.options.Options()
    firefox_options.add_argument('-headless')
    browser = webdriver.Firefox(executable_path='./geckodriver', options=firefox_options)

    return browser

def login_by_chrome():
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)

    return browser

def login_by_phantomjs():
    browser = webdriver.PhantomJS()

    return browser

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'd':
        type_id = '0'
    else:
        type_id = input('Enter your explorer type id (Firefox: 0, Chrome: 1, PhantomJS: 2, default 0): ')

    student_id = input('Enter your student id: ')
    student_pwd = getpass.getpass('Enter you password: ')
    #sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

    try:
        if type_id == '1':
            browser = login_by_chrome()
        elif type_id == '2':
            browser = login_by_phantomjs()
        else:
            browser = login_by_firefox()
        url = r'https://go.ruc.edu.cn/srun_portal_pc?ac_id=6&theme=ruc'
        browser.get(url)
        browser.implicitly_wait(3)

        username = browser.find_element_by_id('username')
        username.send_keys(student_id)
        password = browser.find_element_by_id('password')
        password.send_keys(student_pwd)

        login_button = browser.find_element_by_id('login-account')
        login_button.click()
        skip_button = browser.find_element_by_id('skip-for-now')
        skip_button.click()

        browser.save_screenshot('web_page.png')
        print("login succeeded, enjoy:)!")
    except:
        print("login failed: please check your username and password!")
        raise
    finally:
        try:
            browser.close()
        except:
            pass

