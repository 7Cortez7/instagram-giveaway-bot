from selenium import webdriver
import time
import userdata as udata
import random

randomUsers = set()


class Browser:
    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser.Instagram(self)
        Browser.Login(self)
        Browser.goFollowers(self)


    def Instagram(self):
        self.browser.get(self.link)
        time.sleep(2)
    
    def goFollowers(self):
        self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(5)
        Browser.scrollDown(self)
        followers = self.browser.find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")
        for follower in followers:
            randomUsers.add(follower.text)
        print("Çekiliş başlıyor! {totaluser} kişi katılmaya hak kazandı.".format(totaluser = len(randomUsers)))
        time.sleep(5)
        randomUsersList = list(randomUsers)
        print("Kazanan:", random.choice(randomUsersList))
        time.sleep(5)
        exit()
    
    def scrollDown(self):
        jsCode = """
        page = document.querySelector(".isgrP");
        page.scrollTo(0, page.scrollHeight);
        var pageEnd = page.scrollHeight;
        return pageEnd;
        """
        
        pageEnd = self.browser.execute_script(jsCode)
        while True:
            end = pageEnd
            time.sleep(1)
            pageEnd = self.browser.execute_script(jsCode)
            if end == pageEnd:
                break

    def Login(self):
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        loginBtn = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
        username.send_keys(udata.username)
        password.send_keys(udata.password)
        time.sleep(1)
        loginBtn.click()
        time.sleep(2)
        self.browser.get(self.link + udata.username)
        time.sleep(2)
        

    
