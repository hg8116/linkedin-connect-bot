import logging
import os
import time

import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Load env variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Read file
file_path = "/home/hash/Projects/linkedin-connect-bot/linkedin-links.ods"
# Change the file extension according to your need
df = pd.read_excel(file_path, engine="odf")
linkedin_urls = df["LinkedIn URL"].tolist()

# Selenium driver setup
driver = webdriver.Firefox()

# Login to Linkedin
username = os.getenv("LINKEDIN_USERNAME")
password = os.getenv("LINKEDIN_PASSWORD")
driver.get("https://www.linkedin.com/login")

username_input = driver.find_element(By.ID, "username")
username_input.send_keys(username)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)

login_button = driver.find_element(
    By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button"
)
login_button.click()

time.sleep(15)

# Open links and connect/ follow
for url in linkedin_urls:
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    # Try to send connection request
    try:
        more_button = driver.find_element(
            By.XPATH,
            '//button[contains(@aria-label, "More")]',
        )
        driver.execute_script("arguments[0].click();", more_button)

        connect_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(@aria-label, "Invite")]')
            )
        )

        driver.execute_script("arguments[0].click();", connect_button)

        send_without_note_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[contains(@aria-label, "Send")]')
            )
        )

        driver.execute_script("arguments[0].click();", send_without_note_button)
        logging.info(f"Invite sent successfully - {url}")
        time.sleep(2)

    except Exception as e:
        logging.warning(e)
        try:
            connect_button = driver.find_element(
                By.XPATH, ('//button[contains(@aria-label, "Invite")]')
            )

            driver.execute_script("arguments[0].click();", connect_button)

            send_without_note_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//button[contains(@aria-label, "Send")]')
                )
            )
            driver.execute_script("arguments[0].click();", send_without_note_button)
            logging.info(f"Invite sent successfully - {url}")
            time.sleep(2)

        except Exception as e:
            logging.warning(e)
            # Tries to follow if connection not possible
            try:
                follow_button = driver.find_element(
                    By.XPATH,
                    '//button[contains(@aria-label, "Follow")]',
                )
                driver.execute_script("arguments[0].click();", follow_button)
                logging.info(f"Followed successfully - {url}")
                time.sleep(2)

            # Throws exception if both not done
            except Exception as e:
                logging.warning(e)
                logging.warning(f"Unsuccessful - {url}")

driver.quit()
