from selenium import webdriver
import wikipedia
import pyttsx3 as p

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

class inforr():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/jayar/.wdm/drivers/chromedriver/win32/90.0.4430.24/chromedriver.exe")

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()
        results = wikipedia.summary(query, sentences=4)
        speak(results)