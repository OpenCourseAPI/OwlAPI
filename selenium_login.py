# NOTE: With the latest updates to fhda, this script is currently in a broken state
#       Since `scrape_advanced.py` does not require selenium anymore, use it directly

import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=300,400")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://myportal.fhda.edu/cp/home/displaylogin")


def scrape_cookies():
    driver.execute_script(f"document.getElementById('user').value='{os.environ['MP_USER']}'")
    driver.execute_script(f"document.getElementById('pass').value='{os.environ['MP_PASS']}'")

    try:
        driver.execute_script("doLogin()")
        WebDriverWait(driver, 3).until(
            EC.title_is("MyPortal / Foothill-De Anza College District")
        )

        driver.get(
            "https://myportal.fhda.edu/render.UserLayoutRootNode.uP?uP_tparam=utf&utf=%2fcp%2fip%2flogin%3fsys%3dsctssb%26url%3dhttps%3A%2F%2Fbanssb.fhda.edu%2FPROD%2Fbwskfcls.p_sel_crse_search")

        WebDriverWait(driver, 3).until(
            EC.title_is("MyPortal / Foothill-De Anza College District")
        )
    finally:
        cookies_list = driver.get_cookies()

    return get_cookies(cookies_list)


def get_cookies(cookies_list):
    cookies_dict = {}
    for cookie in cookies_list:
        cookies_dict[cookie['name']] = cookie['value']
    return cookies_dict


def kill_driver():
    driver.quit()


if __name__ == '__main__':
    scrape_cookies()
