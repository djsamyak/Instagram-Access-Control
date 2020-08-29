# Instagram Access Control
An app based on web automation to manage the access control of an Instagram account. The app allows you to generate a 10 digit radom alpha-numeric password and have it mailed to multiple recipients.

## Requirements
- Google Chrome, or Mozilla Firefox
- Geckodriver for Mozilla Firefox, or
- ChromeDriver for Google Chrome

## How-to:
1. Edit `requirements.csv` as following:
    - The "username" field should contain the Instagram Username of the account, the "password" is self explainatory. 
    - The "NOTIF_ID" field can have multiple Email IDs stated below it (column wise). 
    - "BOT_ID" should contain the email address of the account that would be use to share the notifying mailing address.
    - "BOT_PASSWORD" should contain the password of the notifying mailing address(or, app specific password in case of GMAIL).
2. Launch bot.exe.
3. Wait for the Chrome/Firefox based automated web browser to complete.
