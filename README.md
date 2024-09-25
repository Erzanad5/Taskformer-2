# Automated LinkedIn Outreach Tool

## Project Description

This project automates the extraction of LinkedIn profile data from a Google Sheet, crafts personalized outreach messages using OpenAI, and facilitates email delivery to potential leads. The primary focus is on introducing a business automation solution and scheduling demonstrations with interested clients.

## Key Features

- **Profile Data Extraction:** Automatically scrapes vital information such as names, job titles, companies, and emails from LinkedIn profiles.
- **Custom Message Generation:** Utilizes OpenAI's GPT-3.5-turbo model to produce tailored outreach messages.
- **Automated Emailing:** Sends the personalized messages directly via email.
- **Google Sheets Integration:** Retrieves LinkedIn profile URLs from a specified Google Sheet.

## Prerequisites

Before using this tool, ensure you have the following:

1. **Google Sheets API Setup:**
   - Activate the Google Sheets API and download the `credentials.json` file from the Google Cloud Console.
   - Place the credentials file in the root folder of your project.

2. **Selenium WebDriver:**
   - Download the correct version of ChromeDriver for your operating system.
   - Verify that the ChromeDriver path is correctly specified in your script.

3. **OpenAI API Key:**
   - Acquire an API key from [OpenAI](https://platform.openai.com/account/api-keys) and insert it into your script.

4. **SMTP Configuration:**
   - Use an email account (e.g., Gmail) that has SMTP enabled for sending emails.
   - For Gmail, ensure that "Less secure app access" is enabled or use OAuth2 for more secure authentication.

## Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/repo-name.git
   cd repo-name
# LinkedIn Outreach Automation

## Features
- Scrapes LinkedIn profiles for contact information.
- Generates personalized outreach messages using OpenAI.
- Sends emails to contacts via SMTP.
- Stores LinkedIn profile URLs in Google Sheets.

## Prerequisites
- Python 3.x installed on your machine.
- Basic knowledge of using APIs and email configurations.

## Installation Steps

### 1. Install Required Libraries
Create a `requirements.txt` file with the following content:

```plaintext
gspread
oauth2client
selenium
openai
```

# LinkedIn Outreach Automation

## Table of Contents
1. [Installation](#installation)
2. [Configure Google Sheets API Credentials](#configure-google-sheets-api-credentials)
3. [Environment Configuration](#environment-configuration)
4. [ChromeDriver Setup](#chromedriver-setup)
5. [Configuration Details](#configuration-details)
6. [How to Execute](#how-to-execute)
7. [Expected Output](#expected-output)
8. [Troubleshooting Guide](#troubleshooting-guide)
9. [Implementation Steps](#implementation-steps)

## Installation
Install the required libraries using:

```bash
pip install -r requirements.txt
```
# Google Sheets LinkedIn Outreach Automation

## Configure Google Sheets API Credentials
Follow the [Google Sheets API documentation](https://developers.google.com/sheets/api/quickstart/python) to set up your credentials. Place your credentials JSON file in the project directory and update your script accordingly.

## Environment Configuration
Modify the script or create a `.env` file with the following credentials:

- OpenAI API key
- Email account (SMTP) details
- Google Sheets API credentials

## ChromeDriver Setup
Download ChromeDriver that matches your Chrome version. Ensure the path to the ChromeDriver executable is correctly set in your script.

## Configuration Details
Before executing the script, update the following placeholders in the code:

- `path/to/your/credentials.json` - Path to your Google Sheets API credentials.
- `your_google_sheet_id` - The ID of the Google Sheet containing LinkedIn profile URLs.
- `your_linkedin_email` - Your LinkedIn email address.
- `your_linkedin_password` - Your LinkedIn password.
- `your_openai_api_key` - Your OpenAI API key.
- `your_email@example.com` - Your email for sending outreach messages.
- `your_email_password` - Your email account password for SMTP authentication.

## How to Execute
Run the script with:

```bash
python linkedin_outreach.py
```
# Project Overview

## Expected Output
The script will scrape LinkedIn profiles, generate personalized messages, and send emails to the respective contacts.

## Troubleshooting Guide

### Email Sending Failures
- Confirm that your SMTP settings are correct and your email provider allows automated emails.
- For Gmail, enable "Less secure apps" or set up OAuth2 for enhanced security.

### LinkedIn Scraping Challenges
- Be aware that LinkedIn may block automated scraping attempts or require captcha verification.
- If email extraction fails, ensure that the XPath selectors in the script are up-to-date with LinkedIn’s current structure.

### Google Sheets API Issues
- Double-check that your API credentials are valid and the spreadsheet link is accurately referenced in the script.

## Implementation Steps
1. Create a file named `README.md` in your project directory.
2. Copy and paste the above content into the file.
3. Adjust the repository link and any placeholders as necessary.

This README provides a comprehensive guide to the project, including features, prerequisites, installation steps, usage instructions, and troubleshooting tips.
