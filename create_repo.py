#!/usr/local/bin/python3

import colored
from time import sleep
from selenium import webdriver
from stdiomask import getpass

print(colored.stylize("\n---- | Create GitHub Repo | ----\n", colored.fg("red")))

username = input("Username on GitHub: ")
# Hide password in CLI
password = getpass(prompt = "Password on GitHub: ")
repoName = input("Repository name: ")
print()

class CreateRepo:
    def __init__(self, username, password, repoName):
        self.username = username
        self.password = password
        self.repoName = repoName

        # Select webdriver (here Safari, otherwise you can use Chrome())
        self.driver = webdriver.Safari()

        # Access GitHub Login Page
        self.driver.get("https://github.com/login")

        # Log in to GitHub
        self.driver.find_element_by_id("login_field").send_keys(self.username)
        sleep(2)
        self.driver.find_element_by_id("password").send_keys(self.password)
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]").click()
        sleep(2)

        # Create New Repository
        self.driver.find_element_by_xpath("//*[@id='repos-container']/h2/a").click()
        sleep(2)
        self.driver.find_element_by_id("repository_name").send_keys(self.repoName)
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='new_repository']/div[4]/button").click()
        sleep(2)

CreateRepo(username, password, repoName)
