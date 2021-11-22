#Go to following site using the chromedriver

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = 'https://letterboxd.com/members/popular/this/week/page/20/'

username = 'YOUR_LETTERBOX_USERNAME_HERE'
password = 'YOUR_LETTERBOX_PASSWORD_HERE'

driver = webdriver.Chrome('/Users/wiifreaki/Desktop/chromedriver')


#Script for logging in to the site

def login():

    
    driver.get(url)
    time.sleep(4)
    
    #click following xpath

    xpath = '//*[@id="tyche_cmp_modal"]/div/div/div/div[5]/div[2]'
    def click_xpath(xpath):
        driver.find_element_by_xpath(xpath).click()

    click_xpath(xpath)

    time.sleep(3)

    #click following xpath called 'sign in'
    sign_in = '//*[@id="header"]/section/div/div/nav/ul/li[1]/a/span[2]'
    def click_sign_in(sign_in):
        driver.find_element_by_xpath(sign_in).click()

    click_sign_in(sign_in)

    time.sleep(3)

    #fill in the username mnemo into the following xpath
    
    username_xpath = '//*[@id="username"]'
    def fill_username(username, username_xpath):
        driver.find_element_by_xpath(username_xpath).send_keys(username)

    fill_username(username, username_xpath)

    time.sleep(4)


    #fill in the password into the following xpath
    username_xpath = '//*[@id="password"]'
    
    def fill_password(password, username_xpath):
        driver.find_element_by_xpath(username_xpath).send_keys(password)

    fill_password(password, username_xpath)

    time.sleep(4)

    #click the following xpath called 'sign in'
    sign_in = '//*[@id="signin"]/fieldset/div/div[4]/div[1]/input'

    def click_sign_in(sign_in):
        driver.find_element_by_xpath(sign_in).click()

    click_sign_in(sign_in)

    time.sleep(5)

def adding_strangers():
    #Click all xpaths
    xpath1 = '//*[@id="content"]/div/div/section/table/tbody/tr[1]/td[5]/div/a[2]/span[1]'
    xpath2 = '//*[@id="content"]/div/div/section/table/tbody/tr[2]/td[5]/div/a[2]/span[1]'
    xpath3 = '//*[@id="content"]/div/div/section/table/tbody/tr[3]/td[5]/div/a[2]/span[1]'
    xpath4 = '//*[@id="content"]/div/div/section/table/tbody/tr[4]/td[5]/div/a[2]/span[1]'
    xpath5 = '//*[@id="content"]/div/div/section/table/tbody/tr[5]/td[5]/div/a[2]/span[1]'
    xpath6 = '//*[@id="content"]/div/div/section/table/tbody/tr[6]/td[5]/div/a[2]/span[1]'
    xpath7 = '//*[@id="content"]/div/div/section/table/tbody/tr[7]/td[5]/div/a[2]/span[1]'
    xpath8 = '//*[@id="content"]/div/div/section/table/tbody/tr[8]/td[5]/div/a[2]/span[1]'
    xpath9 = '//*[@id="content"]/div/div/section/table/tbody/tr[9]/td[5]/div/a[2]/span[1]'
    xpath10 = '//*[@id="content"]/div/div/section/table/tbody/tr[10]/td[5]/div/a[2]/span[1]'
    xpath11 = '//*[@id="content"]/div/div/section/table/tbody/tr[11]/td[5]/div/a[2]/span[1]'
    xpath12 = '//*[@id="content"]/div/div/section/table/tbody/tr[12]/td[5]/div/a[2]/span[1]'
    xpath13 = '//*[@id="content"]/div/div/section/table/tbody/tr[13]/td[5]/div/a[2]/span[1]'
    xpath14 = '//*[@id="content"]/div/div/section/table/tbody/tr[14]/td[5]/div/a[2]/span[1]'
    xpath15 = '//*[@id="content"]/div/div/section/table/tbody/tr[15]/td[5]/div/a[2]/span[1]'
    xpath16 = '//*[@id="content"]/div/div/section/table/tbody/tr[16]/td[5]/div/a[2]/span[1]'
    xpath17 = '//*[@id="content"]/div/div/section/table/tbody/tr[17]/td[5]/div/a[2]/span[1]'
    xpath18 = '//*[@id="content"]/div/div/section/table/tbody/tr[18]/td[5]/div/a[2]/span[1]'
    xpath19 = '//*[@id="content"]/div/div/section/table/tbody/tr[19]/td[5]/div/a[2]/span[1]'
    xpath20 = '//*[@id="content"]/div/div/section/table/tbody/tr[20]/td[5]/div/a[2]/span[1]'
    xpath21 = '//*[@id="content"]/div/div/section/table/tbody/tr[21]/td[5]/div/a[2]/span[1]'
    xpath22 = '//*[@id="content"]/div/div/section/table/tbody/tr[22]/td[5]/div/a[2]/span[1]'
    xpath23 = '//*[@id="content"]/div/div/section/table/tbody/tr[23]/td[5]/div/a[2]/span[1]'
    xpath24 = '//*[@id="content"]/div/div/section/table/tbody/tr[24]/td[5]/div/a[2]/span[1]'
    xpath25 = '//*[@id="content"]/div/div/section/table/tbody/tr[25]/td[5]/div/a[2]/span[1]'
    xpath26 = '//*[@id="content"]/div/div/section/table/tbody/tr[26]/td[5]/div/a[2]/span[1]'
    xpath27 = '//*[@id="content"]/div/div/section/table/tbody/tr[27]/td[5]/div/a[2]/span[1]'
    xpath28 = '//*[@id="content"]/div/div/section/table/tbody/tr[28]/td[5]/div/a[2]/span[1]'
    xpath29 = '//*[@id="content"]/div/div/section/table/tbody/tr[29]/td[5]/div/a[2]/span[1]'
    xpath30 = '//*[@id="content"]/div/div/section/table/tbody/tr[30]/td[5]/div/a[2]/span[1]'

    xpath_next = '//*[@id="content"]/div/div/section/div[2]/div[2]/a'

    def click_all_xpaths():
    
        driver.find_element_by_xpath(xpath1).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath2).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath3).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath4).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath5).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath6).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath7).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath8).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath9).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath10).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath11).click()
        time.sleep(0.5)
        #scroll down a bit
        driver.execute_script("window.scrollTo(0, 720)") 
        time.sleep(2)
        driver.find_element_by_xpath(xpath12).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath13).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath14).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath15).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath16).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath17).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath18).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath19).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath20).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath21).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath22).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath23).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath24).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath25).click()
        time.sleep(2)
        #scroll down a bit
        driver.execute_script("window.scrollTo(0, 1020)") 
        time.sleep(1)
        driver.find_element_by_xpath(xpath26).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath27).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath28).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath29).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(xpath30).click()
        time.sleep(4)

    click_all_xpaths()

    #Click the xpath called next
    xpath_next = '//*[@id="content"]/div/div/section/div[2]/div[2]/a'

    def click_next():
          driver.find_element_by_xpath(xpath_next).click()

    click_next()    
    time.sleep(4)


def main():
      login()

      adding_strangers()
      time.sleep(4)
      adding_strangers()
      time.sleep(4)
      adding_strangers()
      time.sleep(4)
      adding_strangers()
      time.sleep(4)
      adding_strangers()
      time.sleep(4)
      adding_strangers()
      time.sleep(4)
      adding_strangers()
      time.sleep(4)
      adding_strangers()
      time.sleep(4)
      adding_strangers()
      time.sleep(4)
      adding_strangers()
      time.sleep(4)
      adding_strangers()
      time.sleep(4)
      
      print('Finished adding')


if __name__ == "__main__":
      main()    