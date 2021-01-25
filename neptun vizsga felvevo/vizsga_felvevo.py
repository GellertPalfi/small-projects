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
driver = webdriver.Chrome(executable_path="C:/Users/assas/Desktop/chromedriver.exe")
driver.get("https://web8.neptun.u-szeged.hu/hallgato/login.aspx")


def bejelentkezes():
    # neptun kód
    username = driver.find_element_by_id("user")
    username.clear()
    username.send_keys("")

    # neptun jelszó
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
    time.sleep(0.1)


def vizsga_felvetel():
    # vizsgák oldalra váltás, azt 500db/oldalra hogy biztos meglegyen az adott vizsga
    driver.find_element_by_id("mb1_Vizsgak").click()
    driver.find_element_by_id("mb1_Vizsgak_Vizsgajelentkezes").click()
    driver.find_element_by_id("h_exams_gridExamList_ddlPageSize").click()
    driver.find_element_by_xpath("//*[ text() = '500' ]").click()
    time.sleep(0.5)

    """
    mivel fogalmam sincs, hogy ezeket az id-kat mennyire szeretik változtatgatni,
    ezért validációs célból bekerült a vizsga változó amihez az if-ben neked kell beírni
    a vizsga nevét, ha ez nem fog egyezni az xpathban kapott tárggyal nem fog kurzust felvenni
    sajnos ehhez a vizsga xpath-jét is megkell adni:
    1. a megfelelő vizsganevére jobb klikk a listában
    2. inspect element
    3. kijelölt html kódra jobb klikk
    4. copy -> xpath
    5. vizsga változóban paste a "" jelek közé
    """
    """
    minden vizsga gombjanak van egy 'xpath'-ja ezt kell az üres zárójelek közé bemásolni.
    neptunban az adott vizsgánál a + gombra jobb kattintva:
    1. inspect element
    2. kijelölt html kódra jobb klikk
    3. copy -> xpath
    4. paste a "" jelek közé
    """

    vizsga = driver.find_element_by_xpath("").text

    if vizsga == "":
        driver.find_element_by_xpath("").click()
        driver.find_element_by_xpath("//*[ text() = 'Jelentkezés' ]").click()
    else:
        print("a vizsga nem az amit felszeretnél venni, próbáld meg újra kimásolni a megfelelő xpathet")

    # ha folyamatosan futtatod, ezt a sleepet nyugodtan ki lehet kommentezni
    time.sleep(1)
    driver.close()


def kurzus_felvetel():
    # tárgyak oldalra váltás
    driver.find_element_by_id("mb1_Targyak").click()
    driver.find_element_by_id("mb1_Targyak_Targyfelvetel").click()
    driver.find_element_by_id("upFilter_cmbTerms").click()

    # megfelelő félév kiválasztása
    driver.find_element_by_xpath("//*[ text() = '2020/21/2' ]").click()

    # mivel a félév kiválasztásánál megváltozik a DOM, várni kell egy kicsit még betölti az újat
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='upFilter_expandedsearchbutton']").click()

    # 500 kurzusra/lap -ra váltás
    time.sleep(1)
    driver.find_element_by_id("h_addsubjects_gridSubjects_ddlPageSize").click()
    driver.find_element_by_xpath("//*[ text() = '500' ]").click()

    """
    mivel fogalmam sincs, hogy ezeket az id-kat mennyire szeretik változtatgatni,
    ezért validációs célból bekerült a targy változó amihez az if-ben neked kell beírni
    a tárgy nevét, ha ez nem fog egyezni az xpathban kapott tárggyal nem fog kurzust felvenni
    sajnos ehhez a targy xpath-jét is megkell adni:
    1. a megfelelő tárgy nevére jobb klikk a listában
    2. inspect element
    3. kijelölt html kódra jobb klikk
    4. copy -> xpath
    5. paste a "" jelek közé
    """
    targy = driver.find_element_by_xpath("").text

    if targy == "":
        """
        xpath móka megint, adott tárgy "Felvesz" gombjának kell az első üres zárójelek közé az xpath
        második pedig a tárgy megfelelő kurzusának fehér kis checkboxa
        """
        driver.find_element_by_xpath("").click()
        time.sleep(0.2)
        driver.find_element_by_id("").click()
        driver.find_element_by_id("function_update1").click()
    else:
        print("a tárgy nem az amit felszeretnél venni, próbáld meg újra kimásolni a megfelelő xpathet")

    # ha folyamatosan futtatod, ezt a sleepet nyugodtan ki lehet kommentezni
    time.sleep(1)
    driver.close()


# annak megfelelően vedd ki a kommentekez ahogy futtatni szeretnéd
# while True:
# bejelentkezes()
# kurzus_felvetel()
# vizsga_felvetel()

