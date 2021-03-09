## Medistart Hospital Web app
![Project Image](/static/images/medistar.png)

--------

### Table of Content

-  [Description](#description)
 - [User-stories](#user-stories)
 - [User-Acceptance-Testing](#User-Acceptance-Testing)
 - [Technologies](#technologies)
 - [Deployment](#Deployment)
 - [References](#References)
 - [Licenses](#licenses)
 - [Author](#author)

------------------------
 ## Description

 This milestone project is part of my on going Full Stack Software Developer course at Canadian Business college in collaboration with the Code Instititute.
 The website is based on a fictional Medistar Hospital Flask app, the app's theme is based on a hospital and their services to the general public.The user(s) will be able to 
 navigate through the site, register as a patient, Doctor, nurse or admin, the information will be submitted into Mongodb database. The user wull also be able to interact
 with an Artificial Intelligent chat bot that speaks to the user(s), at this momment the AI is able to have a meaningful conversation and respond to a 
 Covid-19 emergency, dispatch paramedics to the patients residents or location, this is simulated and not a real live software, the AI has been coded 
 to look for key words and phrases which trigger a response to the user, AI is also able to book appointments and inform the users Doctor of any pertinent information,
 this is also simulated, but I hope to grow to the level where i will be able to code the AI to have these additional attributes. Once a user is registered and logs into their portal, they are paired 
 with their doctor through the Mongodb, this enables user and Doctor to send short messages between themselves to either book appoinments , remind patient to monitor blood pressure,
 Glucose level or check up with patient after surgery and etc. The Doctor is able to make request for prsecription, request for medical test(s) and procedure(s), all the information is submitted to Mongodb.
 The doctors also have two AI tools at their disposal for disgnosis of Diabetes and Heart Disease, these tools are built on datasets from Kaggle and IEEE data port. The datasets are
 based on machine learning for 400 - 1000 different individulas cases from various age groups, sex with a positive of nagative result. The AI for Diabetes is built on a threshold 1=Positive / 0= Negative.
 The AI for Heart Disease Threshold >40 positive with 70 percent accuracy < 40 negative with 70 percent accuracy.
 
 Disclaimer: The AI for diabetes , Heart Disease and AI chat bot are not built to be used for realworld applications but only developed for educational purposes, further testing and improvements are need
 to further develop these tools.
 
----------------------------
 ## User-stories

 ### Requirement Gathering
 
 The table below will breifly describe the user stories for the functional and non-functional requirements, the user stories decribed in
 **Table 1.0 Requirement Traceability Catalog** will be Independent, Negotiable, Valuable, Estimable, Smart and Testable, **INVEST** in nature and composition.

 *Table 1.0 Requirement Traceability Catalog*

HLR   |  HLR Ref# |    HLR Description    |                              User Stories                                                    |                                                      Acceptance criteria                                                                                        |                                MoSCoW                                                                                                                |
------|---------- |-----------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------| 
Home  | H-1.0     | Gain access to Medstar website   | **As a** user **I want** to access the web page  **so that** I can gain access to the site content.| **Given** that the user is on the MedStar web page, **When** they click on the Nav links Home **then** the system will take the user to the home section of the web page. |     M   |
Get Started btn | GS-1.1| Gain access to Medstar website | **As a** user **I want** to access home page   **so that** I can have access to the get started button.| **Given**  that the user is on MedStar web page, **When** they click on the get started button **then** the system will take the user to the user login/ register page |    M   |
Contact us btn | CU-1.2| Gain access to Medstar website | **As a** user **I want** to access home page   **so that** I can have access to the contact us button.| **Given**  that the user is on MedStar web page, **When** they click on the contact us button **then** the system will take the user to the contact us page |    M   |
Read more btn | RM-1.3| Gain access to Medstar website | **As a** user **I want** to access the department page   **so that** I can have access to the read more button.| **Given**  that the user is on MedStar web page, **When** they click on the read more button **then** the system will take the user to the about us page |    M   |
Play btn | PB-1.4| Gain access to Medstar website | **As a** user **I want** to access home page   **so that** I can have access to the Play button.| **Given**  that the user is on MedStar web page, **When** they click on the play btn **then** the system will display a promotional video about MediStar |    M   |
Contact floating btn | CF-1.5| Gain access to Medstar website | **As a** user **I want** to access home page    **so that** I can have access to the AI Chat bot.| **Given**  that the user is on MedStar web page,  **When** they click on the contact us ICON **then** the system will take the user to the AI page to speak with the AI Bot |    M   |
Social Media icon  | SM-1.6| Gain access to Medstar website | **As a** user **I want** to access home page   **so that** I can access the social media icons of the web page.| **Given**  that the user is on MedStar home page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
Services | S-2.0|   Gain access to Medstar website| **As a** user **I want** to access the services page  **so that** I can access the services provided by Medstar.| **Given** that the user is on MedStar  service page, **When** they click on the service nav link **then** the system will take the user to the service page, where the user can view the services provided by Medstar .|    M  |
Services hover effect | SH-2.1|   Gain access to Medstar website| **As a** user **I want** to access the services page  **so that** I can access the services provided by Medstar.| **Given** that the user is on MedStar  service page, **When** they hover over the service nav link **then** the system will display a drop down list of services provided by Medstar.|    M  |
Get Started btn | GS-2.2| Gain access to Medstar website | **As a** user **I want** to access service page   **so that** I can have access to the get started button.| **Given**  that the user is on MedStar service page, **When** they click on the get started button **then** the system will take the user to the user login/ register page |    M   |
Contact floating btn | CF-2.3| Gain access to Medstar website | **As a** user **I want** to access service page    **so that** I can have access to the AI Chat bot.| **Given**  that the user is on MedStar service page,  **When** they click on the contact us ICON **then** the system will take the user to the AI page to speak with the AI Bot |    M   |
Social Media | SM-2.4| Gain access to Medstar website | **As a** user **I want** to access service page   **so that** I can access the social media section of the service page.| **Given**  that the user is on MedStar home page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
Department | DP-3.0|   Gain access to Medstar website| **As a** user **I want** to access the department page  **so that** I can access the informatin on each department.| **Given** that the user is on MedStar  department page, **When** they click on the department nav link **then** the system will take the user to the department page, where the user can view Medstar hospital departments .|    M  |
Contact us btn | CU-3.1| Gain access to Medstar website | **As a** user **I want** to access the department page   **so that** I can have access to the contact us button.| **Given**  that the user is on MedStar web page, **When** they click on the contact us button **then** the system will take the user to the contact us page |    M   |
Social Media | SM-3.2| Gain access to Medstar website | **As a** user **I want** to access department page   **so that** I can access the social media section of the web page.| **Given**  that the user is on MedStar department page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
Read more btn | RM-3.3| Gain access to Medstar website | **As a** user **I want** to access the department page   **so that** I can have access to the read more button.| **Given**  that the user is on MedStar web page, **When** they click on the read more button **then** the system will take the user to the about us page |    M   |
About Us | AU-4.0|   Gain access to Medstar website| **As a** user **I want** to access the about us  page  **so that** I can access the informatin on the about us page.| **Given** that the user is on MedStar about us page, **When** they click on the about us nav link **then** the system will take the user to the about us page, where the user can view more information about MedStar .|    M  |
Get Started btn | GS-4.1| Gain access to Medstar website | **As a** user **I want** to access about us  page   **so that** I can have access to the get started button.| **Given**  that the user is on MedStar about us page, **When** they click on the get started button **then** the system will take the user to the user login/ register page |    M   |
Read more btn | RB-4.2| Gain access to Medstar website | **As a** user **I want** to access the about us page   **so that** I can have access to the read more button.| **Given**  that the user is on MedStar web page, **When** they click on the read more button **then** the system will take the user to the about us page |    M   |
Play btn | PB-4.3| Gain access to Medstar website | **As a** user **I want** to access the about use page  **so that** I can have access to the Play button.| **Given**  that the user clicks on the play btn **then** the system will display a promotional video about MediStar hospital |    M   |
Social Media | SM-4.4 | Gain access to Medstar website | **As a** user **I want** to access about use page   **so that** I can access the social media section of the web page.| **Given**  that the user is on MedStar department page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
Blog | B-5.0|   Gain access to Medstar website| **As a** user **I want** to access the blog page  **so that** I can access the informatin on the blog page.| **Given** that the user is on the blog page, **When** they click on the blog nav link **then** the system will take the user to the about blog, where the user can view blog information about MedStar .|    M  |
Social Media | B-5.1 | Gain access to Medstar website | **As a** user **I want** to access the blog use page   **so that** I can access the social media section of the blog page.| **Given**  that the user is on MedStar department page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
Contact Us | CU-6.0|   Gain access to Medstar website| **As a** user **I want** to access the contact us  page  **so that** I can access the contact us form.| **Given** that the user is on MedStar contact us page, **When** they click on the contact us nav link **then** the system will take the user to the contact us page, where the user can access the contac form .|    M  |
Submit btn | SU-6.1 | Gain access to Medstar website | **As a** user **I want** to access the contact us page **so that** I can access the contact form submit btn.| **Given** that the user is on Medstar website, **When** they click on the submit btn **then** the system will submit the message via emailjs to the client . |    M   |
Reset btn | RS-6.2 | Gain access to Medstar website | **As a** user **I want** to access the contact us page **so that** I can access the Reset btn.| **Given** that the user is on Medstar contact form, **When** they click on the Reset btn **then** the system will reset the input fields. |    M   |
Social Media | CU-6.2 | Gain access to Medstar website | **As a** user **I want** to access the contact use page   **so that** I can access the social media section of the contact us page.| **Given**  that the user is on MedStar contact us  page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
User Login | UL-7.0 | Gain access to Medistar website | **As a** user **I want** to access the Login Btn **so that** I can gain acesss to the Login form.| **Given** that the user is on the medi web page, **When** they click on the login btn**then** the system will authenticate the users credentials and deny or give the user access to their profile page, task manager and logout navlinks. |    M   |
User Login Profile | LP-7.1 | Gain access to Medistar website | **As a** user **I want** to access the profile nav link **so that** I can gain acesss to the my profile page.| **Given** that the user is on the medi web page, **When** they click on the profile nav-link**then** the system will give the user access to the Task manger tool,to communicate with their doctor. |    M   |
User Login home | Lh-7.2 | Gain access to Medistar website | **As a** user **I want** to access the home nav link **so that** I can gain acesss to the login home page.| **Given** that the user is on the medi web page, **When** they click on the home nav-link**then** the system will give the user access to the login user home page. |    M   |
User New Task | NT-7.3 | Gain access to Medistar website | **As a** user **I want** to access the New task link **so that** I can gain acesss to the Task manager.| **Given** that the user is on the medi web page, **When** they click on the New Task nav-link**then** the system will give the user access to their profile page. |    M   |
User  Edit Task | ET-7.3.1 | Gain access to Medistar website | **As a** user **I want** to access the edit task btn **so that** I can gain access to the edit Categories page.| **Given** that the user is on the medi web page, **When** they click on the edit categories btn**then** the system will take the doctor to the edit categories page. | M |
User Delete Task | DT-7.3.2 | Gain access to Medistar website | **As a** user **I want** to access the delete task btn **so that** I can delete a task.| **Given** that the user is on the medi web page, **When** they click on the delete task btn**then** the system will delete the task the task. | M |
User Logout | LO-7.4 | Gain access to Medistar website | **As a** user **I want** to access the logout navlink **so that** I can logout.| **Given** that the user is on the medi web page, **When** they click on the logout nav-link**then** the system will log the user out. |    M   |
User Register | R-8.1 | Gain access to Medistar website | **As a** user **I want** to access the Register form **so that** I can gain acesss to Register btn.| **Given** that the user is on the medi web page, **When** they click on the register btn**then** the system will validate their inputs and either decline or submit their information to mongodb. |    M   |
Doctor Login | DL-9.0 | Gain access to Medistar website | **As a** doctor **I want** to access the Login form **so that** I can gain acesss to the Login btn.| **Given** that the user is on the medi web page, **When** they click on the login btn**then** the system will authenticate the users credentials and deny or give the user access to their profile page, task manager and logout navlinks. |    M   |
Doctor Profile | DLP-9.1 | Gain access to Medistar website | **As a** doctor **I want** to access the profile nav link **so that** I can gain acesss to the my profile page.| **Given** that the user is on the medi web page, **When** they click on the profile nav-link**then** the system will give the user access to the Task manger tool,to communicate with their doctor. |    M   |
Doctor login home | DLH-9.2 | Gain access to Medistar website | **As a** doctor **I want** to access the home nav link **so that** I can gain acesss to the login home page.| **Given** that the doctor is on the medi web page, **When** they click on the home nav-link**then** the system will give the user access to the login user home page. |    M   |
Doctor New Task | NT-9.3 | Gain access to Medistar website | **As a** doctor **I want** to access the New task link **so that** I can gain acesss to the New Task .| **Given** that the doctor is on the medi web page, **When** they click on the New Task nav-link**then** the system will give the user access to the new task manager to communicate with their patient or nurse. |    M   |
Doctor edit task | ET-9.3.1 | Gain access to Medistar website | **As a** doctor **I want** to access the edit task btn **so that** I can gain access to the edit Categories page.| **Given** that the doctor is on the medi web page, **When** they click on the edit categories btn**then** the system will take the doctor to the edit categories page. | M |
Doctor delete task | DT-9.3.2 | Gain access to Medistar website | **As a** doctor **I want** to access the delete task btn **so that** I can delete a task.| **Given** that the doctor is on the medi web page, **When** they click on the delete task btn**then** the system will delete the task the task. | M |
Doctor Lab work | LW-9.4 | Gain access to Medistar website | **As a** doctor **I want** to access the lab work navlink **so that** I can fill in the lab work form.| **Given** that the doctor is on the medi web page, **When** they click on the medical test nav-link**then** the system will display a medical test form which will validate all inputs and either decline or submit the valid inputs to Mongodb. |    M   |
Doctor prescription | PRE-9.5 | Gain access to Medistar website | **As a** doctor **I want** to access the prescription navlink **so that** I can fill in prescription forms.| **Given** that the doctor is on the medi web page, **When** they click on the logout nav-link**then** the system will log the user out. |    M   |
Doctor procedure | PRO-9.6 | Gain access to Medistar website | **As a** doctor **I want** to access the procedure navlink **so that** I can fill in the procedure forms.| **Given** that the doctor is on the medi web page, **When** they click on the procedure nav-link**then** the system will display a medical procedure form which will validate all inputs and either decline or submit the valid inputs to Mongodb. | M |
Doctor AI Diagnostic | AID-9.7 | Gain access to Medistar website | **As a** doctor **I want** to access the AI Diagnostic navlink **so that** I can gain access to the application.| **Given** that the doctor is on the medi web page, **When** they click on the AI Diagnostic nav-link**then** the system will take the doctor to the AI diagnostic tool for diabetes and Heart Disease . | M |
Doctor Manage Categories | MC-9.8 | Gain access to Medistar website | **As a** doctor **I want** to access the Manage Categories navlink **so that** I can gain access to the manage Categories page.| **Given** that the doctor is on the medi web page, **When** they click on the manage categories nav-link**then** the system will take the doctor to the manage categories page. | M |
Doctor Logout | DLO-9.9 | Gain access to Medistar website | **As a** doctor **I want** to access the logout navlink **so that** I can logout.| **Given** that the user is on the medi web page, **When** they click on the logout nav-link**then** the system will log the user out. |  M  |
Admin login| AL-10.0 | Gain access to Medistar website | **As a** Admin **I want** to access the Admin Login link **so that** I can gain acesss to the login Form.| **Given** that the Admin is on the medi web page, **When** they click on the admin drop down link**then** the system will display an abmin icon and text, when it is clicked it will take the user to the admin login  page. |    M   |
Admin Logout | ALO-10.1  | Gain access to Medistar website | **As a** Admin **I want** to access the logout navlink **so that** I can logout.| **Given** that the Admin is on the medi web page, **When** they click on the logout nav-link**then** the system will log the admin out. |    M   |
Medstar Register | MR-10.2 | Gain access to Medistar website | **As a** medstar employee **I want** to access the Register form **so that** I can gain acesss to Register btn.| **Given** that the employee is on the medi web page, **When** they click on the register btn**then** the system will validate their inputs and either decline or submit their information to mongodb. |    M   |


## User-Acceptance-Testing

The UAT will define the criteria by which the website is considered to be "working",high, medium or low defects will be identified and cataloged for further improvements or regression testing.
The UAT critreria and results will confirm if the website can handle required task in a real-world scenarios, according to the Requirements Traceability Catalog Table 1.0.

*Table 2.0 User Acceptance Testing (UAT)*


 Test#    | User stories Ref# |        Description of task        |               Steps to evaluate    |                        Expected Result                                                                                                                                                                                                                               |            Pass / Fail / Comments                               |  
--------  |-------------------|-----------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------| 
APT-H-1.0  | H-1.0               | Home nav link                  | APT-H-1.0.0:   Click home nav link | The link should be funtional and take the user to the home page section displaying the page and information .                                                                                                                                                          |                     Pass                                      |
APT-GS-1.1  | GS-1.1             | Get started btn                | APT-GA-1.1.0:  Click Get Started Btn| The btn should be funtional and take the user to the login/register page.                                                                                                                                                                                            |                     Pass                                      | 
APT-CU-1.2  | CU-1.2             |Contact us btn                  | APT-CU-1.2.0:  Click Contact us Btn| The btn should be funtional and take the user to the contact us page.                                                                                                                                                                                                 |                     Pass                                      | 
APT-RM-1.3  | RM-1.3             |Read More btn                   | APT-RM-1.3.0:  Click Read more  Btn| The btn should be funtional and take the user to the Blog section.                                                                                                                                                                                                    |                     Pass                                      | 
APT-PB-1.4  | PB-1.4             |Play Btn                        | APT-bbt-1.4.0: Click Play Btn |The button should be functional and allow the user to a view the Medstar promotional Video.                                                                                                                                                                                |                     Pass                                      |                                                                                     
APT-CF-1.5   | CF-1.5            |contact floating btn            | APT-PP-1.5.0: Click Contact floating btn| The button should be functional and once it is clicked, it should pop-up a phone, whatsapp and chat icon when the chat icon is clicked it should take the user to the a AI chat page                                                                            |                     Pass                                      |
APT-SM-1.6  | SM-1.6           | social media btn                 | APT-PP-1.6.0: Click on the social media icon | The icon should be functional and once it is clicked , it should take the user to the relevant medstar socia media page                                                                                                                                    |                     Pass                                      |                                                                        
APT-S-2.0 | S-2.0               | services nav Link               | APT-S-2.0.0:  Click the service nav link | The link should be funtional and take the user to the service page section displaying the page and information.                                                                                                                                                 |                     Pass                                      |
APT-SH-2.1  | SH-2.1            | service hover effect            | APT-SH-2.1.0: Hover over the service nav link  | When the user is on the service page and they hover over the Service nav link a drop down menu of services is displayed for the user to select.                                                                                                          |                     Pass                                      |                                                                
APT-GS-2.2  | GS-2.2            | Get started btn                 | APT-GS-2.2.0: Click Get Started Btn| The btn should be funtional and take the user to the login/register page.                                                                                                                                                                                            |                     Pass                                      |
APT-CF-2.3  |CF-2.3            | Contact Floating btn             | APT-CF-2.3.0: Click Contact floating btn| The button should be functional and once it is clicked, it should pop-up a phone, whatsapp and chat icon when the chat icon is clicked it should take the user to the a AI chat page                                                                             |                     Pass                                      |
APT-SM-2.4  | SM-2.4            | Social media icon               | APT-SM-2.4.0: Click on the social media icon | The icon should be functional and once it is clicked , it should take the user to the relevant medstar socia media page                                                                                                                                    |                     Pass                                      |
APT-DP-3.0  | DP-3.0            | Department nav link             | APT-RB-3.0.0: Click Department nav link | The link should be funtional and take the user to the department page section displaying the page and information.                                                                                                                                              |                     Pass                                      |
APT-CU-3.1  | CU-3.1          | Contact us btn                    | APT-CU-3.1.0: Click Contact us Btn| The btn should be funtional and take the user to the contact us page.                                                                                                                                                                                                 |                     Pass                                      |
APT-SM-3.2 | SM-3.2         | Social media icon                   | APT-SM-3.2.0: Click on the social media icon | The icon should be functional and once it is clicked , it should take the user to the relevant medstar socia media page                                                                                                                                   |                     Pass                                      |
APT-RM-3.3 | RM-3.3         | Read more btn                       | APT-RM-3.3.0: Click Read more  Btn| The btn should be funtional and take the user to the Blog section.                                                                                                                                                                                                    |                     Pass                                      |
APT-AU-4.0 | AU-4.0         | About us                            | APT-AU-4.0.0: Click about us nav link | The link should be funtional and take the user to the about us  page section displaying the page and information .                                                                                                                                                |                     Pass                                      |
APT-GS-4.1  | GS-4.1        | Get started btn                     | APT-GA-4.1.0: Click Get Started Btn| The btn should be funtional and take the user to the login/register page.                                                                                                                                                                                            |                     Pass                                      | 
APT-RM-4.2  | RM-4.2        |Read More btn                        | APT-RM-4.2.0: Click Read more  Btn| The btn should be funtional and take the user to the Blog section.                                                                                                                                                                                                    |                     Pass                                      | 
APT-PB-4.3  | PB-4.3        |Play Btn                             | APT-PB-4.3.0: Click Play Btn |The button should be functional and allow the user to a view the Medstar promotional Video.                                                                                                                                                                                 |                     Pass                                      |   
APT-SM-4.4  | SM-4.4         | Social media icon                  | APT-SM-4.4.0: Click on the social media icon | The icon should be functional and once it is clicked , it should take the user to the relevant medstar socia media page                                                                                                                                   |                     Pass                                      | 
APT-BL-5.0  | BL-5.0         | Blog                               | APT-BL-5.0.0: Click Blog nav link | The link should be funtional and take the user to the blog page section displaying the page and information .                                                                                                                                                        |                     Pass                                      |
APT-SM-5.1  | SM-5.1         | Social media icon                  | APT-SM-5.1.0: Click on the social media icon | The icon should be functional and once it is clicked , it should take the user to the relevant medstar socia media page                                                                                                                                   |                     Pass                                      | 
APT-CU-6.0  | CU-6.0         | Contact Us                         | APT-CU-6.0.0: Click contact nav link | The link should be funtional and take the user to the contact page section displaying the page and information .                                                                                                                                                  |                     Pass                                      |
APT-SM-6.1  | SM-6.1         | Submit Btn                         | APT-SM-6.1.0: Click submit btn  | The btn should be functional and once it is clicked , it should submit the contact form information to Emailjs for client review.                                                                                                                                      |                     Pass                                      | 
APT-RS-6.2  | RS-6.2         | Reset Btn                          | APT-RS-6.2.0: Click Rest btn  | The btn should be functional and once it is clicked , it should Reset the contact form and clear all fields.                                                                                                                                                             |                     Pass                                      |                                                                                                                                   
APT-SM-6.3  | SM-6.3        | Social media Icon                   | APT-SM-6.3.0: Click Social media icon  | The icon should be functional and once it is clicked , it should link the user with the Medstar social media page.                                                                                                                                              |                     Pass                                      | 
APT-UL-7.0  | UL-7.0         | User login                        | APT-SM-7.0.0: Click submit btn  | The btn should be functional and once it is clicked , it should submit the contact form information to Emailjs for client review.                                                                                                                                      |                     Pass                                      | 
APT-ULP-7.1  | ULP-7.1         | Login Profile                    | APT-LP-7.1.0: Click submit btn  | The btn should be functional and once it is clicked , it should submit the contact form information to Emailjs for client review.                                                                                                                                      |                     Pass                                      | 
APT-LP-7.2  | Lh-7.2         | Login home                     | APT-LP-7.2.0:Click submit btn  | The btn should be functional and once it is clicked , it should submit the contact form information to Emailjs for client review.                                                                                                                                      |                     Pass                                      | 
APT-NT-7.3  | NT-7.3         | New Task                         | APT-NT-7.3.0:Click submit btn  | The btn should be functional and once it is clicked , it should submit the contact form information to Emailjs for client review.                                                                                                                                      |                     Pass                                      | 
APT-ET-7.4  | ET-7.4         | Edit Task                        | APT-LP-7.4.0:Click submit btn  | The btn should be functional and once it is clicked , it should submit the contact form information to Emailjs for client review.                                                                                                                                      |                     Pass                                      | 
APT-DT-7.5  | DT-7.5        |  Delete Task                    | APT-LP-7.5.0 :Click submit btn  | The btn should be functional and once it is clicked , it should submit the contact form information to Emailjs for client review.                                                                                                                                      |                     Pass                                      | 



## Technologies 

The technologies employed to develop this web application was based on the principles of Design for X (DFX) also know as Design for excellence, the basis of this methodology is based
on cost to quality, making effective use of resources to minimize cost and relay more on innovation and technical knowledge to meet the users expectations.The software's used are mostly free 
and meet the **Requirements Traceability Catalog Table 1.0** to develop this website, innovation and technical knowledge was based on my recently aquired skills based on my journey so 
far with Code institute and the Canadian Business College.

Technologies deployed on this project:

 1.  For email API plug in [emailjs](https://www.emailjs.com/)
 2.  For Payment API plug in [Paypal](https://developer.paypal.com/developer/accounts/)
 3.  For README.md file image and website images editing and styling Canva software [Canva](https://www.canva.com/)
 4.  For coding enviroment /IDE github [GitHub](http://github.com)
 5.  HTML 5 code sequence and syntax deployed for index.html,cancel.html,gmenue.html,payment1.html, payment2.html, payment3.html, success.html and cancel.html
 6.  CSS code sequence and syntax deployed for style.css,style1.css,style2.css, style3.css and style4.css
 7.  Java script code sequence and syntax deployed for index.html, asterold.html, asternew.js,neural_network.js,payment.js,smooth_scrooll.js and sendEmail.js
 8.  Jquery script code sequence and syntax deployed in index.html and sendEmails.js
 9.  Bootstrap cnd 4.4.1 [Bootstrap](https://getbootstrap.com/)
 10. Bootstrap Jquery 3.4.1 [Bootstrap](https://getbootstrap.com/)
 11. Bootstrap cnd font awesome [Bootstrap](https://www.bootstrapcdn.com/fontawesome/)
 12. For CSS plugin [Trailwind](https://tailwindcss.com/)
 13. Font Google Poppins & Yellow tail  [Fontgoogle](https://fonts.google.com/)
 14. Tutorial on [Neural-Networks](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ)
 15. Scroll effect on index.html [Smooth-scroll](http://github.com/cferdinandi/smooth-scroll )
  

---------------------------------------------

 ## Deployment
 After my User Acceptance Testing (UAT) I pushed the final version of my code to git hub , in my commit message I cataloged each change before my final push, the steps I took 
 can be seen below, my project is now live on [GitHub](https://peristratus.github.io/foxxgames/)

 1. Complete the User UAT evaluation and made sure that all codes are funtional and operational.
 2. Used git commit -m to catalog all my changes in line with UAT requirement.
 3. Used git push to push my final version to my git hub repository. 
 4. Clicked on settings on my Peristratus/bootstrap repository and scrolled down to github pages.
 5. Clicked on select branch drop down menu and then selected master.

-----------------------------------------------

## References

I would like to make references to cetain educational Youtube tutorials and certain articles that have helped with my webdesign develop my skills as a Fullstack developer.


1. Online tutorials youtube video on 1979 Asteroid game & Neural Networks [Freecode-camp](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ )
2. Online tutorials youtube video on new Asteroid game [Chris-course](https://www.youtube.com/channel/UC9Yp2yz6-pwhQuPlIDV_mjA)
3. HTML/CSS security by sqreen online article [sqreen](https://www.sqreen.com/checklists/html-css-security-checklist)
4. Input patterns online article [HTML.com](https://html.com/attributes/input-pattern/)
5. online tutorial youtube gamewebsite [Onclickmedia](https://www.youtube.com/channel/UCVY0KRdGfxPi97RBINcM5Tg/videos)

-----------------------------------------------

## Licenses

All icons,logos and videos used on my website are only for educational purposes and will not be used for the commercial version:

1. Atari, Nintendo, Sega games random images from [google](https://www.google.com/) search engine.
2. Hero images random from [google](https://www.google.com/) search engine.
3. Footer icons [fontawesome](https://fontawesome.com/v4.7.0/icons/)
4. Music for 2020 Asteriod game from Youtube [MP3music](https://www.youtube.com/watch?v=mGx_FATyasQ)
5. Music and sounds for 1979 Asteriod game from [Freecode-camp](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ)

-----------------------------------------------

## Author 

*Name: Olaorebikan Roy Abdallah*\
*Institute: Canadaian Business College (code Institute).*\
*Designation: Student.*\
*Course: Fullstack Developer.*
