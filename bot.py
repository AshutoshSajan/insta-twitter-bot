from selenium import webdriver
import os
import time
print(os, webdriver, "os")


class InstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        # open the chrome browser
        self.driver = webdriver.Chrome("./chromedriver.exe")

        # open the instagram homepage
        # self.driver.get("https://www.instagram.com")
        self.login()

    def login(self):
        # open the instagram login page from the login url
        self.driver.get("https://www.instagram.com/accounts/login/")

        print(self.driver, "...")
        # selecting the username input feild and adding the username into it
        self.driver.find_element_by_name('username').send_keys(self.username)

        # selecting the password input feild and adding the password into it
        self.driver.find_element_by_name('password').send_keys(self.password)


if __name__ == "__main__":
    ig_bot = InstaBot("temp_username", "temp_password")

    print(ig_bot.username)
