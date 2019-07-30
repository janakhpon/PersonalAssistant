from selenium import webdriver

# prepare the option for the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('headless')

# start chrome browser
browser = webdriver.Chrome(options=options)
browser.get('http://www.google.com/xhtml')
print(browser.current_url)
browser.quit()