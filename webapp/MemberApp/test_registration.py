import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

project_dir = os.path.dirname(os.path.abspath('../../'+__file__))
firefox_dir = '/'.join([project_dir, 'drivers/geckodriver'])
browser = webdriver.Firefox(executable_path=firefox_dir)
browser.get('http://localhost:8000/member/registration')

# Find elements
prefix = Select(browser.find_element_by_id('id_prefix'))
first_name = browser.find_element_by_id('id_first_name')
last_name = browser.find_element_by_id('id_last_name')
citizen_id = browser.find_element_by_id('id_citizen_id')
gender = Select(browser.find_element_by_id('id_gender'))
date_birthday = browser.find_element_by_id('id_date_birth')
phone_no = browser.find_element_by_id('id_phone_no')
house_no = browser.find_element_by_id('id_house_no')
resident_name = browser.find_element_by_id('id_resident_name')
village_no = browser.find_element_by_id('id_village_no')
road = browser.find_element_by_id('id_road')
alley = browser.find_element_by_id('id_alley')
area = Select(browser.find_element_by_id('id_area'))
subarea = Select(browser.find_element_by_id('id_sub_area'))
province = browser.find_element_by_id('id_province')
post_code = browser.find_element_by_id('id_post_code')
email = browser.find_element_by_id('id_email')
reference_person = browser.find_element_by_id('id_reference_person')
submit = browser.find_element_by_id('id_submit')

# Sendkey Text
first_name.send_keys('อาคาเณย์')
last_name.send_keys('ขมิ้นเครือ')
citizen_id.send_keys('1103000026999')
phone_no.send_keys('0919594945')
house_no.send_keys('207')
resident_name.send_keys('AdaFactor')
village_no.send_keys('1')
road.send_keys('มหาดไทย')
alley.send_keys('-')
province.send_keys('นครราชสีมา')
post_code.send_keys('30000')
email.send_keys('adadesions@adafactor.com')
reference_person.send_keys('r00191')

# Sendkey to Select
prefix.select_by_visible_text('นาย')
gender.select_by_visible_text('ชาย')
time.sleep(0.5)
area.select_by_index(1)
time.sleep(0.5)
subarea.select_by_index(1)
