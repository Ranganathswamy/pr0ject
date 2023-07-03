
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add code to handle the Twitter login with the captured credentials
        return f'Logged in as {username}'
    return render_template('login.html')

if __name__ == '__main__':
    app.run()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
firefox_options = Options()
firefox_options.headless = True
driver = webdriver.Firefox(options=firefox_options)
 @app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Initialize the WebDriver
        driver = webdriver.Firefox(options=firefox_options)

        # Perform the login using Selenium
        driver.get('https://www.twitter.com')
        # Find the username and password fields and populate them
        username_field = driver.find_element_by_xpath("//*[@id='username']")
        username_field.send_keys("username")
        password_field = driver.find_element_by_xpath('//*[@id="password"]')
        password_field.send_keys("password")
        # Submit the form
        password_field.send_keys(Keys.RETURN)
        submit=driver.find_element_by_xpath("/html/body/form/input[3]")
        submit.click()

        # Add code to handle the rest of your application logic

        # Quit the WebDriver
        #driver.quit()

        return f'Logged in as {username}'

    return render_template('login.html')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('https://www.twitter.com/search')
search_field = driver.find_element_by_name('q')
search_field.send_keys('Python Web Development using Flask')
search_field.send_keys(Keys.RETURN)
import time
time.sleep(3)
tweets = driver.find_elements_by_xpath("//div[@data-testid='tweet']")

for tweet in tweets:
    username = tweet.find_element_by_xpath(".//span[contains(@class, 'username')]").text
    content = tweet.find_element_by_xpath(".//div[contains(@class, 'content')]").text
    timestamp = tweet.find_element_by_xpath(".//time").get_attribute('datetime')

    print(f"Username: {username}")
    print(f"Content: {content}")
    print(f"Timestamp: {timestamp}")
    print("---")

import csv
data = []
for tweet in tweets:
    username = tweet.find_element_by_xpath(".//span[contains(@class, 'username')]").text
    content = tweet.find_element_by_xpath(".//div[contains(@class, 'content')]").text
    timestamp = tweet.find_element_by_xpath(".//time").get_attribute('datetime')
    data.append([username, content, timestamp])
csv_file = 'twitter_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Content', 'Timestamp'])
    writer.writerows(data)
@app.route('/')
def index():
    return render_template('index.html', data=data)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Assuming you have stored the scraped data for each topic in separate lists called 'topic1_data' and 'topic2_data'

# Combine the data into a single DataFrame
df = pd.DataFrame(topic1_data, columns=['Topic', 'Username', 'Content', 'Timestamp'])
df = df.append(pd.DataFrame(topic2_data, columns=['Topic', 'Username', 'Content', 'Timestamp']))

# Calculate counts for each topic
topic_counts = df['Topic'].value_counts()

# Determine the most tweeted year for each topic
df['Year'] = pd.to_datetime(df['Timestamp']).dt.year
most_tweeted_year = df.groupby('Topic')['Year'].value_counts().groupby(level=0).idxmax().apply(lambda x: x[1])
# Perform statistical calculations
# For example, calculate mean, median, and standard deviation of tweet counts for each topic
mean_counts = df.groupby('Topic')['Topic'].count().mean()
median_counts = df.groupby('Topic')['Topic'].count().median()
std_counts = df.groupby('Topic')['Topic'].count().std()

# Create graphs and charts to visualize the data
# For example, create a bar chart of tweet counts for each topic
plt.bar(topic_counts.index, topic_counts.values)
plt.xlabel('Topic')
plt.ylabel('Tweet Count')
plt.title('Tweet Count Comparison')
plt.show()
from selenium.webdriver.common.by import By

class LoginPage:
    # Define locators for elements on the page
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '/html/body/form/input[3]')

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

from selenium import webdriver
from pages.login_page import LoginPage

# Initialize the WebDriver
driver = webdriver.Firefox()

# Create an instance of the LoginPage
login_page = LoginPage(driver)

# Use the page object methods to interact with the page elements
login_page.enter_username('username')
login_page.enter_password('password')
login_page.click_login_button()
import pytest
from your_flask_app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Homepage" in response.data

def test_login(client):
    response = client.post('/login', data={'username': 'testuser', 'password': 'password'})
    assert response.status_code == 200
    assert b"Logged in as testuser" in response.data




