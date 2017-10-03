from selenium						import webdriver
from selenium.webdriver.common.keys	import Keys
from selenium.webdriver.support.ui	import Select
from dateutil.parser				import parse
import time

#Read user and pass from file
file = open('account.key','r')
key = file.readlines()
url		= key[0].replace('url=','')
user	= key[1].replace('user=','')
pwd		= key[2].replace('pass=','')
file.close()

#Given a Webassign course page return homework 
#Return list in format {'assignment':'datetime '}
def get_hw(selenium, course):
	name = selenium.find_elements_by_xpath("//span[@class='rowLeft']")
	due = selenium.find_elements_by_xpath("//span[@class='rowRightNarrow']")
	hw = dict(zip([option.text for option in name], [option.text for option in due]))
	hw.pop('Name')
	return hw

#Sets up browser
selenium = webdriver.Chrome()
selenium.get(url)
selenium.implicitly_wait(5)

#Sends username and pass
userfield=selenium.find_element_by_id("email").send_keys(user)
pwdfield= selenium.find_element_by_id("cengagePassword").send_keys(pwd)

#Counter index for list of classes as first two options aren't courses
class_num = 2

homework={}

#Loops thru dropdown menu 
while(True):
		select = selenium.find_element_by_id('course') #Gathers array of courses
		options = select.find_elements_by_tag_name("option") #Gets lenght for break 
		course=options[class_num].text
		options[class_num].click()
		homework[course]=get_hw(selenium,course) #stores assingments in form of {'class':{'hw','due'}}
		class_num += 1
		selenium.back()
		if(class_num > len(options)-1): break

selenium.close()

for course, assignment in homework.items():
    for homework, due in assignment.items():
            print('{}: ({},{})'.format(course, homework, due))






