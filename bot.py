from selenium import webdriver
import os
import time
import configparser
# print(os, webdriver, "os")


class InstaBot:

    def __init__(self, username, password):
        """
        Initializes an instance of the InstaBot class

        Call the login method to authenticate a user with Instagram

            Args:
                username: str: The Instagram username for a user
                password:str: The Instagram password for a user

            Attributes:
                Driver: Selenium.webdriver.Chrome: the chromedriver which is used to automate the browser actions.
        """

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'

        # open the chrome browser
        self.driver = webdriver.Chrome("./chromedriver.exe")

        # open the instagram homepage
        # self.driver.get("https://www.instagram.com")
        self.login()

    def login(self):
        # open the instagram login page from the login url
        # self.driver.get("https://www.instagram.com/accounts/login/")

        self.driver.get('{}/accounts/login/'.format(self.base_url))

        # selecting the username/email input feild and adding the username into it
        self.driver.find_element_by_name('username').send_keys(self.username)

        # selecting the username/email input feild using x path
        # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')

        # selecting the password input feild and adding the password into it
        self.driver.find_element_by_name('password').send_keys(self.password)

        # selecting the password input feild using x path
        # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input');

        # selection of submit button and then apply onclick on that
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()

        # selecting the div with login text an clicking on it
        # self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

        # delay after loging in for 2 sec it is nessasary otherwise program won't work
        # time.sleep(2)

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))
        # self.driver.get()

    def follow_user(self, user):
        self.nav_user(user)
        follow_btn = self.driver.find_element_by_xpath(
            "//botton[contains(text(), 'Follow')]")
        print(follow_btn, "follow_btn")
        follow_btn.click()

    def unfollow_user(self, user):
        self.nav_user(user)
        unfollow_btn = self.driver.find_element_by_xpath(
            "//botton[contains(text(), 'Following')]")
        print(unfollow_btn, "unfollow_btn")
        unfollow_btn.click()


if __name__ == "__main__":

    config_path = './config.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config_path)

    # username = cparser['AUTH']['USERNAME']
    # password = cparser['AUTH']['PASSWORD']

    # ig_bot = InstaBot(username, password)
    ig_bot = InstaBot("username", "password")

    # ig_bot.nav_user('sam')
    print(ig_bot.username)
