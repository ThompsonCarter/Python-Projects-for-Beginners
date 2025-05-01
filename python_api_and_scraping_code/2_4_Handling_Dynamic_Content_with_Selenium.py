# Handling Dynamic Content with Selenium
# Install Selenium: pip install selenium
# You also need a web driver like ChromeDriver to control the browser.

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get("https://www.bbc.com")

# Get page content
page_content = driver.page_source
print(page_content)

# Don't forget to quit the driver once done
driver.quit()
