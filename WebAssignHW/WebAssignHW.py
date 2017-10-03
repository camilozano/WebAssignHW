from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#Read API Key from file
file = open('account.key','r')
key = file.readlines()
url		= key[0].replace('url=','')
user	= key[1].replace('user=','')
pwd		= key[2].replace('pass=','')
file.close()


def get_hw(selenium, course):
	homework={}
	name = selenium.find_elements_by_xpath("//span[@class='rowLeft']")
	due = selenium.find_elements_by_xpath("//span[@class='rowRightNarrow']")
	hw = dict(zip([option.text for option in name], [option.text for option in due]))
	hw.pop('Name')
	homework[course]=hw
	return homework




selenium = webdriver.PhantomJS()
selenium.get(url)
selenium.implicitly_wait(5)

userfield=selenium.find_element_by_id("email").send_keys(user)
pwdfield= selenium.find_element_by_id("cengagePassword").send_keys(pwd)

#selenium.find_element_by_name("Login").click()


class_num = 2

homework={}

while(True):
		select = selenium.find_element_by_id('course')
		options = select.find_elements_by_tag_name("option")
		course=options[class_num].text
		options[class_num].click()
		#time.sleep(2)
		homework.update(get_hw(selenium,course))
		class_num += 1
		selenium.back()
		if(class_num > len(options)-1): break

print(homework)

selenium.close()


