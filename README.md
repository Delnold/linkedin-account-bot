# Linkedin-account-bot allows you to autofill your LinkedIn profile.

## The following steps to use the script
1) Git clone the project
2) If you need to change the data for autofilled accounts, you need to manually edit JSON files in exact syntax as provided.
3) Export env variables (EMAIL, PASSWORD) or create .env file in the project folder and include them there. 
Example with export:
   ```bash 
   export EMAIL=YOUR_LINKEDIN_EMAIL
   export PASSWORD=YOUR_LINKEDIN_PASSWORD
4) Run the following command
   ```bash 
   docker-compose up
5) Wait for the process to begin, you can see the process by yourself following next steps:
   - Visit http://localhost:4444/ui
   - Click on the starting session. The password for the session: **secret**

## How it works, and what it does?

The are basically 4 JSON files which are located under "DataRelated" folder, which are responsible for different input fields, they are named after the fields itself.
Also, there are 4 functions written like (add_******) which are related to these JSON files. The functions read the JSON data and enter in its specified sections, and then process to save it. All these activities performed by Selenium WebDriver.

## Current issues/bugs/inconvenience
1) Can`t bypass LinkedIn confirmation page (Captcha/Verification)
2) Inability to add profile icon (Selenium WebDriver couldn`t locate elements responsible for that)
3) Summaries specify only the first entry of JSON file
4) Account can be auto filled only by using the JSON files, which is quite inconvenient

## Examples
Example of an account auto-filled with this script: https://www.linkedin.com/in/semblamance-vinol-155a06262/

### About
![image](https://user-images.githubusercontent.com/91605867/228281831-c017d508-be1e-4cf5-aefe-9f0fcfa42c78.png)
### Experience
![image](https://user-images.githubusercontent.com/91605867/228282104-5bedb51c-e729-4e84-b18b-a1559fb57b78.png)
### Education
![image](https://user-images.githubusercontent.com/91605867/228282188-cd0387d9-c6bb-4df2-93bd-4aea8aa608da.png)
### Skills
![image](https://user-images.githubusercontent.com/91605867/228282252-088cd906-7ef4-4a7d-8a09-daaab5ad6731.png)

