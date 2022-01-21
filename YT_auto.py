from selenium import webdriver


class music():
    def __init__(self):
        self.driver = self.driver = webdriver.Chrome(executable_path="C:/Users/jayar/.wdm/drivers/chromedriver/win32/90.0.4430.24/chromedriver.exe")


    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath('//*[@id="meta"]/ytd-video-meta-block')
        video.click()