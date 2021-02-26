from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")


def getLinks(url):
    driver = webdriver.Chrome(
        options=options, executable_path=r'C:\webdrivers\chromedriver.exe')
    driver.get(url)

    links = driver.find_elements_by_xpath("//a[@href]")

    for link in links:
        print(link.get_attribute('href'))

    driver.quit()


getLinks('https://www.bbc.com/')
