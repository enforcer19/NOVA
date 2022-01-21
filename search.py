from selenium import webdriver

class sear():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/jayar/.wdm/drivers/chromedriver/win32/90.0.4430.24/chromedriver.exe")

    def get_infoo(self, query):
        self.query = query
        self.driver.get(url="https://google.co.in")
        searchh = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        searchh.click()
        searchh.send_keys(query)
        searchh.submit()