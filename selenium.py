from selenium import webdriver


browser = webdriver.Firefox()
# why not chrome? you need to download and install
# chrome driver for that 

browser.get('some_url')
# url will open with browser specified

tagSelected = browser.find_element_by_css_selector('here goes the copy pasted unique selector from firefox-inspect element. Make sure to get unique css selector')

tagSelected.click()


# filling the input field. 

searchElement = browser.find_element_by_css_selector('input type text or unique selector thingy')
searchElement.send_keys('string to write in input field')
searchElement.submit() 

browser.back()
browser.forward()
browser.refresh()
browser.quit()
