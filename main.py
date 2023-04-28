from selenium import webdriver
from json import load
from selenium.common import exceptions
from random import choice


file_name = "cookies.json"
driver = webdriver.Firefox()
link = "https://steamcommunity.com/sharedfiles/filedetails/?id=2017703319"  # Collection link
number = 10  # Number of items to sub
with open(file_name, "r", encoding="UTF-8") as f:
    cookie_dict = load(f)


driver.get(cookie_dict["url"])
for cookie in cookie_dict["cookies"]:
    if cookie["sameSite"] == "unspecified":
        cookie["sameSite"] = "Lax"
    elif cookie["sameSite"] == "no_restriction":
        cookie["sameSite"] = "None"
    else:
        cookie["sameSite"] = "Strict"

    driver.add_cookie(cookie)

driver.get_cookies()
driver.get(link)
buttons = driver.find_elements_by_class_name("subscribe")
for x in driver.find_elements_by_class_name("toggled"):
    try:
        buttons.remove(x)
    except ValueError:
        pass
    else:
        print("Removed an already subbed stuff.")
x = 0
while x != number:
    if not buttons:
        break
    choi = choice(buttons)
    choi.click()
    x += 1
    print(x)
    buttons.remove(choi)

print("Done")
