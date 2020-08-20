from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from userinfo import username,password
import time


class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.followers = []
        self.following = []
        time.sleep(1)
    
    def logIn(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(5)

    def getFollowers(self):
        self.driver.get("https://www.instagram.com/" + self.username)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)
        dialog = self.driver.find_element_by_css_selector("div[role=dialog] ul")
        action = webdriver.ActionChains(self.driver)
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        dialog.click()
        while True:
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements_by_css_selector("li"))
            if newCount != followerCount:
                followerCount = newCount
                print(followerCount)
            else:
                break
        users = dialog.find_elements_by_css_selector("li")
        for user in users:
            self.followers.append(user.find_element_by_css_selector("a").get_attribute("href"))
        with open(f"{self.username} s instagram followers.txt","w",encoding="utf-8") as file:
            for follower in self.followers:
                file.write(follower + "\n")

    def getFollowing(self):
        self.driver.get("https://www.instagram.com/" + self.username)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)
        dialog = self.driver.find_element_by_css_selector("div[role=dialog] ul")
        action = webdriver.ActionChains(self.driver)
        followingCount = len(dialog.find_elements_by_css_selector("li"))
        dialog.click()
        while True:
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements_by_css_selector("li"))
            if newCount != followingCount:
                followingCount = newCount
                print(followingCount)
            else:
                break
        users = dialog.find_elements_by_css_selector("li")
        for user in users:
            self.following.append(user.find_element_by_css_selector("a").get_attribute("href"))
        with open(f"{self.username} s instagram following.txt","w",encoding="utf-8") as file:
            for i in self.following:
                file.write(i + "\n")
    

    def whoDontFollowMeBack(self):
        with open(f"{self.username} who dont follow me back.txt","w",encoding="utf-8") as file:
            for i in self.following:
                if i not in self.followers:
                    file.write(i + "\n")
        self.driver.close()




instagram = Instagram(username,password)
instagram.logIn()
instagram.getFollowers()
instagram.getFollowing()
instagram.whoDontFollowMeBack()
