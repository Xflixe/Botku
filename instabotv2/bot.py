from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from random import choice
from colorama import Fore
from selenium.common import exceptions  
from selenium.common.exceptions import NoSuchElementException     


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
class bot():
    while True:
        def cretor():
            browser1 = webdriver.Chrome(executable_path=r'yourpath', options=options)
            browser2 = webdriver.Chrome(executable_path=r'yourpath', options=options)
            # get mail
            browser1.get("https://10minutemail.com")
            time.sleep(1)
            mail = browser1.find_element_by_css_selector("#copy_address > span").click()

            # ınstagram creator
            browser2.get("https://www.instagram.com/accounts/emailsignup/")
            time.sleep(3)
            kharf = ["a","b","c","d","e","f","g","h","k","l","m","n","o","p","r","s","t","u","v","y","z"]
            bharf = ["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","T","U","V","Y","Z"]
            sayı = [1,2,3,4,5,6,7,8,9,0]
            k = 0
            while k<1:
                gift = "eagledev"
                for i in range(8):
                    gift += str(choice(kharf + bharf + sayı))


                k+=1
                password = gift + "656565"
            mailarea = browser2.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(4) > div > label > input").send_keys(Keys.CONTROL, "v")
            userarea = browser2.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(5) > div > label > input").send_keys(gift)
            namearea = browser2.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(6) > div > label > input").send_keys(gift)
            passwordarea = browser2.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(7) > div > label > input").send_keys(password)
            button = browser2.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(8) > div > button").click()
            time.sleep(1)
            select = browser2.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select").click()
            option = browser2.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select > option:nth-child(20)").click()
            button2 = browser2.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.g6RW6 > button").click()
            time.sleep(25)
            browser1.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            time.sleep(3)
            message = browser1.find_element_by_css_selector("#mail_messages_content > div > div.message_top").click()
            copy = browser1.find_element_by_css_selector("#email_content > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2)").text
            browser2.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div:nth-child(1) > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > form > div > div:nth-child(1) > input").send_keys(copy)
            browser2.find_element_by_css_selector("#react-root > div > div > section > main > div > div > div:nth-child(1) > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > form > div > div:nth-child(2) > button").click()
            time.sleep(15)
            with open('account.txt', 'a') as f:
                f.write(f'{gift}:{password}\n')
            print(f'{Fore.LIGHTGREEN_EX}Account Created\n')
            browser1.close()
            browser2.close()
        cretor()