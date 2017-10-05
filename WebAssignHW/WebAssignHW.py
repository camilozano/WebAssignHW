from selenium						import webdriver
from selenium.webdriver.common.keys	import Keys
from selenium.webdriver.support.ui	import Select
from dateutil.parser				import parse
from dateutil.tz					import gettz
from datetime						import timedelta, datetime
from ics							import Calendar, Event
import time

#Given a Webassign course page return homework 
#Return list in format {'assignment':'datetime '}
def get_hw(selenium, course):
	name = selenium.find_elements_by_xpath("//span[@class='rowLeft']")
	due = selenium.find_elements_by_xpath("//span[@class='rowRightNarrow']")
	hw = dict(zip([option.text for option in name], [option.text for option in due]))
	hw.pop('Name')
	return hw

#Returns compiled list of homework of all classes
def all_homework(url, user, pwd):
	#Sets up browser
	try:
		selenium = webdriver.PhantomJS()
		selenium.get(url)
		selenium.implicitly_wait(5)

		#Sends username and pass
		userfield=selenium.find_element_by_id("email").send_keys(user)
		pwdfield= selenium.find_element_by_id("cengagePassword").send_keys(pwd)
	except:
		print('Could Not Connect')
		exit()

	#Counter index for list of classes as first two options aren't courses
	class_num = 2

	homework={}

	#Loops thru dropdown menu 
	while(True):
			select = selenium.find_element_by_id('course') #Gathers array of courses
			options = select.find_elements_by_tag_name("option") #Gets lenght for break 
			course=options[class_num].text
			if options>2: options[class_num].click()
			else: break
			homework[course]=get_hw(selenium,course) #stores assingments in form of {'class':{'hw','due'}}
			class_num += 1
			selenium.back()
			if(class_num > len(options)-1): break
	selenium.close()
	return homework


start_time = datetime.now()

#Read user and pass from file
file = open('account.key','r')
key = file.readlines()
url		= key[0].replace('url=','')
user	= key[1].replace('user=','')
pwd		= key[2].replace('pass=','')
tz		= key[3].replace('timezone=','')
file.close()

homework = all_homework(url,user,pwd) #Grabs all homework onto list

cal = Calendar()

for course, assignment in homework.items():
	for homework, due in assignment.items():
		time = parse(due).astimezone(gettz(tz))
		print('{} {} {}'.format(homework, due, time))
		cal.events.append(Event(name=homework,begin=time-timedelta(hours=1),end=time,description=course))

with open('WebAssign.ics', 'w') as f:
    f.writelines(cal)

end_time = datetime.now() - start_time
print(end_time)