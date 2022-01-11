from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flask import Flask
import numpy as np;
import time
import time

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get('https://www.premierleague.com/players/5178/Mohamed-Salah/stats')
time.sleep(5)

cookie_button = driver.find_element_by_class_name('js-accept-all-close')
cookie_button.click()

appearances = driver.find_element_by_class_name('statappearances').text
goals = driver.find_element_by_class_name('statgoals').text
wins = driver.find_element_by_class_name('statwins').text
losses = driver.find_element_by_class_name('statlosses').text
penalities_scored = driver.find_element_by_class_name('statatt_pen_goal').text
shoot_acc = driver.find_element_by_class_name('statshot_accuracy').text
assists = driver.find_element_by_class_name('statgoal_assist').text
#passes = driver.find_elements_by_class_name('stattotal_pass').text

names = ['appearances', 'goals', 'wins', 'losses', 'penalities_scored', 'shoot_acc', 'assists']
stats = [appearances, goals, wins, losses, penalities_scored, shoot_acc, assists]

app = Flask(__name__)

@app.route('/tracker')
def get_current_stats():
    return {'tracker': [p for p in zip(names, stats)]}
