from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#Use Facebook accoun to log in Tinder
EMAIL = "YOUR FB EMAIL"
PW = "YOUR FB PASSWORD"

#Go to Tinder website and click log in
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

time.sleep(2)
log_in_button = driver.find_element(By.LINK_TEXT, value="Log in")
log_in_button.click()

#Reject Tinder cookies
time.sleep(2)
tinder_cookie = driver.find_element(By.XPATH, '//*[@id="q-340338318"]/main/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
tinder_cookie.click()

#Click log in with FB account
time.sleep(2)
fb_button = driver.find_element(By.XPATH, '//*[@id="q-340338318"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
fb_button.click()

#Switch to FB window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Rejetc FB cookies
time.sleep(2)
reject_fb_cookies = driver.find_element(By.XPATH, "//button[@data-testid='cookie-policy-manage-dialog-accept-button' and @title='Decline optional cookies']")
reject_fb_cookies.click()

#Enter FB log in details
time.sleep(2)
fb_email = driver.find_element(By.ID, "email")
fb_email.send_keys(EMAIL)
fb_pw = driver.find_element(By.ID, "pass")
fb_pw.send_keys(PW)
fb_pw.send_keys(Keys.ENTER)

#switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(8)

#Allow location
time.sleep(5)
allow_location = driver.find_element(By.XPATH, '//*[@id="q-340338318"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location.click()

#Disable notication
time.sleep(3)
disable_notification = driver.find_element(By.XPATH,'//*[@id="q-340338318"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
disable_notification.click()

#Maybe later
time.sleep(3)
maybe_later = driver.find_element(By.XPATH, '//*[@id="q-340338318"]/main/div/div/div[3]/button[2]/div[2]/div[2]')
maybe_later.click()

time.sleep(5)

#Setting up the right click/swipe action for Tinder
actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_RIGHT).perform()

#Swipe and like
for n in range(5):
    time.sleep(5)

    try:
        #like_button.click()
        actions.send_keys(Keys.ARROW_RIGHT).perform()
    #deal with the case where there is a match popup
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()
        #wait for the loading
        except NoSuchElementException:
            time.sleep(5)
