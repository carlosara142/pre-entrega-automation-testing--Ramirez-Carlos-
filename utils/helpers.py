from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json

def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def load_user_csv(user_csv_path):
    users = []
    with open(user_csv_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] and row['password']:
                users.append((row['username'], row['password']))
    return users

def load_user_jason(user_csv_path):
    users = []
    with open(user_csv_path, newline='') as file:
        data = json.load(file)  

        for user in data:
            if 'username' in user and 'password' in user:
                users.append((user['username'], user['password']))  
    return users