#Linkedin-account-bot allows you to autofill your LinkedIn profile.

##The following steps to use the script
1) Download WebDriver for your browser and move it to the project directory (By default, I include ChromeWebdriver, although, it might be old for your Chrome version)
2) If you need to change the data for autofilled accounts, you need to manually edit JSON files in exact syntax as provided.
2) Run the script, specify your WebDriver, and LinkedIn account credentials.
3) Wait for the proccess to begin, you will be able to see it all by yourself.

##How it works, and what it does?
The are basically 4 JSON files which are located under "DataRelated" folder, which are responsible for different input fields, they are named after the fields itself.
Also, there are 4 functions written like (add_******) which are related to these JSON files. The functions read the JSON data and enter in its specified sections, and then process to save it. All these activities performed by Selenium WebDriver.

##Current issues/bugs/inconvenience
1) Can`t bypass LinkedIn confirmation page (Captcha/Verification)
2) Inability to add profile icon (Selenium WebDriver couldn`t locate elements responsible for that)
3) Summaries specify only the first entry of JSON file
4) Account can be auto filled only by using the JSON files, which is quite inconvenient

##Examples
Example of an account auto-filled with this script: https://www.linkedin.com/in/semblamance-vinol-155a06262/

###About
![image](https://user-images.githubusercontent.com/91605867/228281831-c017d508-be1e-4cf5-aefe-9f0fcfa42c78.png)
###Experience
![image](https://user-images.githubusercontent.com/91605867/228282104-5bedb51c-e729-4e84-b18b-a1559fb57b78.png)
###Education
![image](https://user-images.githubusercontent.com/91605867/228282188-cd0387d9-c6bb-4df2-93bd-4aea8aa608da.png)
###Skills
![image](https://user-images.githubusercontent.com/91605867/228282252-088cd906-7ef4-4a7d-8a09-daaab5ad6731.png)

