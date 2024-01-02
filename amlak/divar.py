from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import pickle
import time
import traceback


class Divar:

    def __init__(self, URL):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options)
        self.URL = URL
        self.terms_agreement_done = False
        self.driver.get(URL)
        time.sleep(6)

    def __del__(self):
        self.driver.close()
        self.driver.quit()

    def login(self, phone, cookie=None):
        if cookie == None:
            self.driver.implicitly_wait(10)
            my_divar = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/div[3]/div/button").click()
            self.driver.implicitly_wait(5)
            login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/div[3]/div/div/div/button").click()
            self.driver.implicitly_wait(10)
            phone_input = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/form/div/input").send_keys(phone)
            two_FA_input = input("2FA >>> ")
            two_FA = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/form/div/input").send_keys(two_FA_input)
            time.sleep(7)
            notif_message = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div/div[2]/button").click()


        else:
            self.load_cookie(cookie)
            self.driver.get(self.URL)
            time.sleep(7)
            notif_message = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div/div[2]/button").click()
            print("we are in\n")

    def first_post(self):
        first = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div[2]/div/div/div[1]/a")
        return first.get_attribute("href")

    def all_posts(self):
        time.sleep(7)


        posts = self.driver.find_elements(By.XPATH, "//a[@class='']")
        all_posts_links = []
        for i in posts:
            all_posts_links.append(i.get_attribute("href"))

        del all_posts_links[0]
        return all_posts_links


    def post_details(self, post, type):
        details = []
        self.driver.get(post)
        phone_button = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[1]/div[2]/button[1]").click()
        time.sleep(3)
        if self.terms_agreement_done == False:
            agree_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/footer/button[2]").click()
            self.terms_agreement_done = True

        def sell():
            try:
                title = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[1]/div[1]/div/div[1]").text
            except:
                title = None
            try:
                year = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[1]/div[2]/span[2]").text
            except:
                year = None
            try:
                room = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[1]/div[3]/span[2]").text
            except:
                room = None
            try:
                m2 = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[1]/div[1]/span[2]").text
            except:
                m2 = None
            try:
                price = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[2]/div[2]/p").text
                #price = price.replace("تومان","")
                #price = price.replace("٬","")
                #price = price.replace(" ","")
            except:
                price = None
            try:
                m2_price = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[3]/div[2]/p").text
                #m2_price = price.replace("تومان","")
                #m2_price = price.replace("٬","")
                #m2_price = price.replace(" ","")
            except:
                m2_price = None
            try:
                floor_number = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[5]/div[2]/p").text
            except:
                floor_number = None
            try:
                elevator = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[7]/div[1]/span").text
            except:
                elevator = None
            try:
                warehouse = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[1]/div[4]/div[7]/div[3]/span").text
            except:
                warehouse = None
            try:
                parking = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[1]/div[4]/div[7]/div[2]/span").text
            except:
                parking = None
            try:

                phone = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[1]/div[3]/div[1]/div/div[2]/a").text
            except:
                phone = None


            return [title, year, room, m2, price, m2_price, floor_number, elevator, warehouse, parking, phone, post]

        def rent():

            title = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[1]/div[1]/div/div[1]").text
            try:
                year = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[1]/div[2]/span[2]").text
            except:
                year = None
            try:
                room = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[1]/div[3]/span[2]").text
            except:
                room = None
            try:
                m2 = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[1]/div[1]/span[2]").text
            except:
                m2 = None
            try:
                price = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[2]/div[2]/p").text
                price = price.replace("تومان","")
                price = price.replace("٬","")
                price = price.replace(" ","")
            except:
                price = None
            try:
                rent = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[3]/div[2]/p").text
                rent = rent.replace("تومان","")
                rent = rent.replace("٬","")
                rent = rent.replace(" ","")
            except:
                m2_price = None
            try:
                floor_number = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[5]/div[2]/p").text
            except:
                floor_number = None
            try:
                elevator = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[4]/div[7]/div[1]/span").text
            except:
                elevator = None
            try:
                warehouse = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[1]/div[4]/div[7]/div[3]/span").text
            except:
                warehouse = None
            try:
                parking = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[1]/div[4]/div[7]/div[2]/span").text
            except:
                parking = None
            try:

                phone = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div[1]/div[3]/div[1]/div/div[2]/a").text
            except:
                phone = None

            res = {
            'title':title,
            'year':year,
            'room':room,
            'm2':m2,
            'price':price,
            'm2_price':m2_price,
            'floor_number':floor_number,
            'elevator':elevator,
            'warehouse':warehouse,
            'parking':parking,
            'phone':phone,

            }
            return res

        if type == "اچاره":
            return rent
        if type == "فروش":
            return sell

    def save_cookie(self, path):
        time.sleep(5)
        cookie1 = self.driver.get_cookies()
        with open(path, 'wb') as filehandler:
            pickle.dump(self.driver.get_cookies(), filehandler)
        print("\n done")
        print(cookie1)

    def load_cookie(self, path):
         with open(path, 'rb') as cookiesfile:
             cookies = pickle.load(cookiesfile)
             for cookie in cookies:
                 self.driver.add_cookie(cookie)
