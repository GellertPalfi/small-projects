from selenium import webdriver
import time



"""
az egészet egy while true blokkba nyugodtan belehet rakni, nem lesz belőle baj mivel ha jelentkeztél vizsgára
a "jelentkezés" gomb kifog szürkülni, nem lehet rákattinatni majd igy lényegében semmit nem fog csinalni a szkript,
normális internettel kb 5-6 mp alatt végigkattinatja az egészet
"""

"""
szükséges hozzá a google chrome, illetve a 'chromedriver' letöltése
aminek a pathjét kell az 'executable_path=' -hez beilleszteni
"""

options = webdriver.ChromeOptions()
options.add_argument('headless')

# ha azt szeretnéd hogy az ablak meg is jelenjen, vedd ki az options argumentet
driver = webdriver.Chrome(executable_path="C:/Users/assas/Desktop/chromedriver.exe", options=options)
driver.get("https://web8.neptun.u-szeged.hu/hallgato/login.aspx")

# neptun kód
username = driver.find_element_by_id("user")
username.clear()
username.send_keys("")

#neptun jelszó
password = driver.find_element_by_id("pwd")
password.clear()
password.send_keys("")

driver.find_element_by_name("btnSubmit").click()
time.sleep(1.5)

# kommentezd ki ezt a sort ha csak egy képzést csinálsz, ilyenkor nincs ilyen popup window
driver.find_element_by_id("TrainingUpdatePanel1_upmodalTrainingChoose_upFootermodalTrainingChoose_footerbtn_modalTrainingChoose_ok").click()
time.sleep(1.5)

# kommentezd ki ezt a sort ha nincsen "önnek kiteltendő kérdőive van"
driver.find_element_by_id("upSystemParams_upmodalSystemParams_upFootermodalSystemParams_footerbtn_modalSystemParams_Vissza").click()

# vizsgák oldalra váltás, azt 500db/oldalra hogy biztos meglegyen az adott vizsga
driver.find_element_by_id("mb1_Vizsgak").click()
driver.find_element_by_id("mb1_Vizsgak_Vizsgajelentkezes").click()
driver.find_element_by_id("h_exams_gridExamList_ddlPageSize").click()
driver.find_element_by_xpath("//*[ text() = '500' ]").click()
time.sleep(0.5)

"""
minden vizsga gombjanak van egy 'xpath'-ja ezt kell az üres zárójelek közé bemásolni
chromeban a + gombra jobb kattintva:
1. inspect element
2. kijelölt html kódra jobb klikk
3. copy -> xpath
"""
driver.find_element_by_xpath().click()
driver.find_element_by_xpath("//*[ text() = 'Jelentkezés' ]").click()
time.sleep(1)
driver.close()
