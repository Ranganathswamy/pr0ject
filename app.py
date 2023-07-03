from flask import Flask, render_template, request, redirect
import tweepy

# Create Flask app instance
app = Flask(__name__)

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Configure Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


@app.route('/')
#@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate user with Twitter credentials
        try:
            auth.set_access_token(username, password)
            api.verify_credentials()
            return redirect('/dashboard')  # Redirect to the dashboard page after successful login
        except tweepy.TweepError:
            error_msg = 'Invalid Twitter credentials. Please try again.'
            return render_template('login.html', error=error_msg)

    return render_template('login.html')

if __name__ == '__main__':
    app.run()
# Selenium code
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
time.sleep(5)
# Set up headless browsing options for Chrome
options = Options()
options.headless = True

# Initialize the WebDriver
driver = webdriver.Chrome()
url="http://127.0.0.1:5000"
# Navigate to the login page
driver.get(url)
time.sleep(2)

# Find the username and password fields and fill them in
username_field = driver.find_element('xpath','//*[@id="username"]')
password_field = driver.find_element('xpath','//*[@id="password"]')

username_field.send_keys('nagalakshmi')
password_field.send_keys('nagalakshmi@123')

# Submit the form
login_button = driver.find_element('xpath','/html/body/form/input[3]')
login_button.click()

# Wait for time
time.sleep(2)
# searching the content
search_field = driver.find_element('name','q')
search_field.send_keys('Python Web Development using Flask')
search_field.send_keys(Keys.RETURN)

# Close the browser at the end of your script
driver.quit()
import time
time.sleep(3)
tweets = driver.find_elements('xpath',"//div[@data-testid='tweet']")

for tweet in tweets:
    username = tweet.find_element('xpath',".//span[contains(@class, 'username')]").text
    content = tweet.find_element('xpath',".//div[contains(@class, 'content')]").text
    timestamp = tweet.find_element('xpath',".//time").get_attribute('datetime')

    print(f"Username: {username}")
    print(f"Content: {content}")
    print(f"Timestamp: {timestamp}")
    print("---")

import csv
data = []
for tweet in tweets:
    username = tweet.find_element('xpath',".//span[contains(@class, 'username')]").text
    content = tweet.find_element('xpath',".//div[contains(@class, 'content')]").text
    timestamp = tweet.find_element('xpath',".//time").get_attribute('datetime')
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
