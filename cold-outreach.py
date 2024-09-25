import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import openai
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Google Sheets API configuration
scope_of_access = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope_of_access)  # Your credentials file
sheets_client = gspread.authorize(credentials)

# Load the Google Sheet with LinkedIn profile links
sheet_id = 'your_sheet_id'  # Your Google Sheets ID
worksheet = sheets_client.open_by_key(sheet_id).sheet1  # Open the first sheet
linkedin_urls = worksheet.col_values(1)  # Assuming LinkedIn URLs are in the first column

# Set up Selenium WebDriver
service = Service('/path/to/chromedriver')  # Adjust path to your ChromeDriver
browser = webdriver.Chrome(service=service)

# Log into LinkedIn
browser.get('https://www.linkedin.com/login')
time.sleep(2)

# Input LinkedIn credentials
browser.find_element(By.ID, 'username').send_keys('your_email@example.com')  # Your LinkedIn email
browser.find_element(By.ID, 'password').send_keys('your_password')  # Your LinkedIn password
browser.find_element(By.XPATH, '//*[@type="submit"]').click()
time.sleep(3)

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

# Configure email parameters
sender_email = "your_email@example.com"
email_password = "your_email_password"

# SMTP configuration for sending emails
smtp_host = "smtp.gmail.com"
smtp_port = 587

# Loop through each LinkedIn profile link to scrape data
for profile_url in linkedin_urls:
    browser.get(profile_url)
    time.sleep(3)

    try:
        # Extract user details from the LinkedIn profile
        name = browser.find_element(By.XPATH, '//h1[contains(@class, "text-heading-xlarge")]').text
        title = browser.find_element(By.XPATH, '//div[contains(@class, "text-body-medium")]').text
        company = browser.find_element(By.XPATH, '//p[contains(@class, "pv-entity__summary-info")]/span[1]').text
        
        # Placeholder for email extraction (not typically available)
        email_address = browser.find_element(By.XPATH, '//a[contains(@href, "mailto:")]').text

        # Create a prompt for OpenAI to generate a personalized message
        outreach_prompt = (
            f"Draft a personalized outreach message for {name}, who is a {title} at {company}. "
            "The objective is to introduce Taskformer, a business automation tool, and request a demo."
        )
        
        # Call OpenAI to generate the message
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": outreach_prompt}]
        )

        outreach_message = response['choices'][0]['message']['content'].strip()

        # Prepare the email
        email_subject = f"Let's Connect: Schedule a Demo for Taskformer, {name}"
        email_content = MIMEMultipart()
        email_content['From'] = sender_email
        email_content['To'] = email_address
        email_content['Subject'] = email_subject
        email_content.attach(MIMEText(outreach_message, 'plain'))

        # Send the email
        with smtplib.SMTP(smtp_host, smtp_port) as smtp_server:
            smtp_server.starttls()  # Secure the connection
            smtp_server.login(sender_email, email_password)
            smtp_server.sendmail(sender_email, email_address, email_content.as_string())

        print(f"Email successfully sent to {name} at {email_address}\n")

    except Exception as error:
        print(f"Error while processing {profile_url}: {error}")

# Close the browser session
browser.quit()
