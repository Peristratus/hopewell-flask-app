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
Get Started btn | H-1.1| Gain access to Medstar website | **As a** user **I want** to access home page   **so that** I can have access to the get started button.| **Given**  that the user is on MedStar web page, **When** they click on the get started button **then** the system will take the user to the user login/ register page |    M   |
Contact us btn | H-1.2| Gain access to Medstar website | **As a** user **I want** to access home page   **so that** I can have access to the contact us button.| **Given**  that the user is on MedStar web page, **When** they click on the contact us button **then** the system will take the user to the contact us page |    M   |
Read more btn | H-1.3| Gain access to Medstar website | **As a** user **I want** to access the department page   **so that** I can have access to the read more button.| **Given**  that the user is on MedStar web page, **When** they click on the read more button **then** the system will take the user to the about us page |    M   |
Play btn | H-1.4| Gain access to Medstar website | **As a** user **I want** to access home page   **so that** I can have access to the Play button.| **Given**  that the user is on MedStar web page, **When** they click on the play btn **then** the system will display a promotional video about MediStar |    M   |
Contact floating btn | H-1.5| Gain access to Medstar website | **As a** user **I want** to access home page    **so that** I can have access to the AI Chat bot.| **Given**  that the user is on MedStar web page,  **When** they click on the contact us ICON **then** the system will take the user to the AI page to speak with the AI Bot |    M   |
Social Media | H-1.6| Gain access to Medstar website | **As a** user **I want** to access home page   **so that** I can access the social media section of the web page.| **Given**  that the user is on MedStar home page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
Services | S-2.0|   Gain access to Medstar website| **As a** user **I want** to access the services page  **so that** I can access the services provided by Medstar.| **Given** that the user is on MedStar  service page, **When** they click on the service nav link **then** the system will take the user to the service page, where the user can view the services provided by Medstar .|    M  |
Services hover effect | S-2.1|   Gain access to Medstar website| **As a** user **I want** to access the services page  **so that** I can access the services provided by Medstar.| **Given** that the user is on MedStar  service page, **When** they hover over the service nav link **then** the system will display a drop down list of services provided by Medstar.|    M  |
Get Started btn | S-2.2| Gain access to Medstar website | **As a** user **I want** to access service page   **so that** I can have access to the get started button.| **Given**  that the user is on MedStar service page, **When** they click on the get started button **then** the system will take the user to the user login/ register page |    M   |
Contact floating btn | S-2.3| Gain access to Medstar website | **As a** user **I want** to access service page    **so that** I can have access to the AI Chat bot.| **Given**  that the user is on MedStar service page,  **When** they click on the contact us ICON **then** the system will take the user to the AI page to speak with the AI Bot |    M   |
Social Media | H-2.4| Gain access to Medstar website | **As a** user **I want** to access service page   **so that** I can access the social media section of the service page.| **Given**  that the user is on MedStar home page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
Department | D-3.0|   Gain access to Medstar website| **As a** user **I want** to access the department page  **so that** I can access the informatin on each department.| **Given** that the user is on MedStar  department page, **When** they click on the department nav link **then** the system will take the user to the department page, where the user can view Medstar hospital departments .|    M  |
Contact us btn | H-3.1| Gain access to Medstar website | **As a** user **I want** to access the department page   **so that** I can have access to the contact us button.| **Given**  that the user is on MedStar web page, **When** they click on the contact us button **then** the system will take the user to the contact us page |    M   |
Social Media | H-3.2| Gain access to Medstar website | **As a** user **I want** to access department page   **so that** I can access the social media section of the web page.| **Given**  that the user is on MedStar department page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
Read more btn | H-3.3| Gain access to Medstar website | **As a** user **I want** to access the department page   **so that** I can have access to the read more button.| **Given**  that the user is on MedStar web page, **When** they click on the read more button **then** the system will take the user to the about us page |    M   |
About Us | A-4.0|   Gain access to Medstar website| **As a** user **I want** to access the about us  page  **so that** I can access the informatin on the about us page.| **Given** that the user is on MedStar about us page, **When** they click on the about us nav link **then** the system will take the user to the about us page, where the user can view more information about MedStar .|    M  |
Get Started btn | A-4.1| Gain access to Medstar website | **As a** user **I want** to access about us  page   **so that** I can have access to the get started button.| **Given**  that the user is on MedStar about us page, **When** they click on the get started button **then** the system will take the user to the user login/ register page |    M   |
Read more btn | A-4.2| Gain access to Medstar website | **As a** user **I want** to access the about us page   **so that** I can have access to the read more button.| **Given**  that the user is on MedStar web page, **When** they click on the read more button **then** the system will take the user to the about us page |    M   |
Play btn | A-4.3| Gain access to Medstar website | **As a** user **I want** to access the about use page  **so that** I can have access to the Play button.| **Given**  that the user clicks on the play btn **then** the system will display a promotional video about MediStar hospital |    M   |
Social Media | A-4.4 | Gain access to Medstar website | **As a** user **I want** to access about use page   **so that** I can access the social media section of the web page.| **Given**  that the user is on MedStar department page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
Blog | B-5.0|   Gain access to Medstar website| **As a** user **I want** to access the blog page  **so that** I can access the informatin on the blog page.| **Given** that the user is on the blog page, **When** they click on the blog nav link **then** the system will take the user to the about blog, where the user can view blog information about MedStar .|    M  |
Social Media | B-5.1 | Gain access to Medstar website | **As a** user **I want** to access the blog use page   **so that** I can access the social media section of the blog page.| **Given**  that the user is on MedStar department page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
Contact Us | CU-6.0|   Gain access to Medstar website| **As a** user **I want** to access the contact us  page  **so that** I can access the contact us form.| **Given** that the user is on MedStar contact us page, **When** they click on the contact us nav link **then** the system will take the user to the contact us page, where the user can access the contac form .|    M  |
Submit btn | CU-6.1 | Gain access to Medstar website | **As a** user **I want** to access the contact us page **so that** I can access the contact form submit btn.| **Given** that the user is on Medstar website, **When** they click on the submit btn **then** the system will submit the message via emailjs to the client . |    M   |
Reset btn | CU-6.2 | Gain access to Medstar website | **As a** user **I want** to access the contact us page **so that** I can access the Reset btn.| **Given** that the user is on Medstar contact form, **When** they click on the Reset btn **then** the system will reset the input fields. |    M   |
Social Media | CU-6.2 | Gain access to Medstar website | **As a** user **I want** to access the contact use page   **so that** I can access the social media section of the contact us page.| **Given**  that the user is on MedStar contact us  page, **When** they scroll down **then** the system will take the user to the social media icons, if the user clicks on any of the social media icon the system will link them with the social media for Medstar Hospital  |    M   |
User Login | L-7.0 | Gain access to Medistar website | **As a** user **I want** to access the Login Btn **so that** I can gain acesss to the Login form.| **Given** that the user is on the medi web page, **When** they click on the login btn**then** the system will authenticate the users credentials and deny or give the user access to their profile page, task manager and logout navlinks. |    M   |
User Login | L-7.1 | Gain access to Medistar website | **As a** user **I want** to access the profile nav link **so that** I can gain acesss to the my profile page.| **Given** that the user is on the medi web page, **When** they click on the profile nav-link**then** the system will give the user access to the Task manger tool,to communicate with their doctor. |    M   |
User Login | L-7.2 | Gain access to Medistar website | **As a** user **I want** to access the home nav link **so that** I can gain acesss to the login home page.| **Given** that the user is on the medi web page, **When** they click on the home nav-link**then** the system will give the user access to the login user home page. |    M   |
User Login | L-7.3 | Gain access to Medistar website | **As a** user **I want** to access the New task link **so that** I can gain acesss to the Task manager.| **Given** that the user is on the medi web page, **When** they click on the New Task nav-link**then** the system will give the user access to their profile page. |    M   |
Doctor Login | L-7.3.1 | Gain access to Medistar website | **As a** user **I want** to access the edit task btn **so that** I can gain access to the edit Categories page.| **Given** that the user is on the medi web page, **When** they click on the edit categories btn**then** the system will take the doctor to the edit categories page. | M |
Doctor Login | L-7.3.2 | Gain access to Medistar website | **As a** user **I want** to access the delete task btn **so that** I can delete a task.| **Given** that the user is on the medi web page, **When** they click on the delete task btn**then** the system will delete the task the task. | M |
User Login | L-7.4 | Gain access to Medistar website | **As a** user **I want** to access the logout navlink **so that** I can logout.| **Given** that the user is on the medi web page, **When** they click on the logout nav-link**then** the system will log the user out. |    M   |
User Register | R-8.1 | Gain access to Medistar website | **As a** user **I want** to access the Register form **so that** I can gain acesss to Register btn.| **Given** that the user is on the medi web page, **When** they click on the register btn**then** the system will validate their inputs and either decline or submit their information to mongodb. |    M   |
Doctor Login | L-9.0 | Gain access to Medistar website | **As a** doctor **I want** to access the Login form **so that** I can gain acesss to the Login btn.| **Given** that the user is on the medi web page, **When** they click on the login btn**then** the system will authenticate the users credentials and deny or give the user access to their profile page, task manager and logout navlinks. |    M   |
Doctor Login | L-9.1 | Gain access to Medistar website | **As a** doctor **I want** to access the profile nav link **so that** I can gain acesss to the my profile page.| **Given** that the user is on the medi web page, **When** they click on the profile nav-link**then** the system will give the user access to the Task manger tool,to communicate with their doctor. |    M   |
Doctor Login | L-9.2 | Gain access to Medistar website | **As a** doctor **I want** to access the home nav link **so that** I can gain acesss to the login home page.| **Given** that the user is on the medi web page, **When** they click on the home nav-link**then** the system will give the user access to the login user home page. |    M   |
Doctor Login | L-9.3 | Gain access to Medistar website | **As a** doctor **I want** to access the New task link **so that** I can gain acesss to the New Task .| **Given** that the user is on the medi web page, **When** they click on the New Task nav-link**then** the system will give the user access to the new task manager to communicate with their patient or nurse. |    M   |
Doctor Login | L-9.4 | Gain access to Medistar website | **As a** doctor **I want** to access the lab work navlink **so that** I can fill in the lab work form.| **Given** that the user is on the medi web page, **When** they click on the medical test nav-link**then** the system will display a medical test form which will validate all inputs and either decline or submit the valid inputs to Mongodb. |    M   |
Doctor Login | L-9.4.1 | Gain access to Medistar website | **As a** doctor **I want** to access the edit task btn **so that** I can gain access to the edit Categories page.| **Given** that the user is on the medi web page, **When** they click on the edit categories btn**then** the system will take the doctor to the edit categories page. | M |
Doctor Login | L-9.4.2 | Gain access to Medistar website | **As a** doctor **I want** to access the delete task btn **so that** I can delete a task.| **Given** that the user is on the medi web page, **When** they click on the delete task btn**then** the system will delete the task the task. | M |
Doctor Login | L-9.5 | Gain access to Medistar website | **As a** doctor **I want** to access the prescription navlink **so that** I can fill in prescription forms.| **Given** that the user is on the medi web page, **When** they click on the logout nav-link**then** the system will log the user out. |    M   |
Doctor Login | L-9.6 | Gain access to Medistar website | **As a** doctor **I want** to access the prescription navlink **so that** I can fill in prescription forms.| **Given** that the user is on the medi web page, **When** they click on the logout nav-link**then** the system will log the user out. |    M   |
Doctor Login | L-9.7 | Gain access to Medistar website | **As a** doctor **I want** to access the procedure navlink **so that** I can fill in the procedure forms.| **Given** that the user is on the medi web page, **When** they click on the procedure nav-link**then** the system will display a medical procedure form which will validate all inputs and either decline or submit the valid inputs to Mongodb. | M |
Doctor Login | L-9.8 | Gain access to Medistar website | **As a** doctor **I want** to access the AI Diagnostic navlink **so that** I can gain access to the application.| **Given** that the user is on the medi web page, **When** they click on the AI Diagnostic nav-link**then** the system will take the doctor to the AI diagnostic tool for diabetes and Heart Disease . | M |
Doctor Login | L-9.9 | Gain access to Medistar website | **As a** doctor **I want** to access the Manage Categories navlink **so that** I can gain access to the manage Categories page.| **Given** that the user is on the medi web page, **When** they click on the manage categories nav-link**then** the system will take the doctor to the manage categories page. | M |
Doctor Login | L-9.10 | Gain access to Medistar website | **As a** doctor **I want** to access the Manage Categories navlink **so that** I can gain access to the manage Categories page.| **Given** that the user is on the medi web page, **When** they click on the manage categories nav-link**then** the system will take the doctor to the manage categories page. | M |


Doctor Login | L-9.10 | Gain access to Medistar website | **As a** doctor **I want** to access the logout navlink **so that** I can logout.| **Given** that the user is on the medi web page, **When** they click on the logout nav-link**then** the system will log the user out. |  M  |


## User-Acceptance-Testing

The UAT will define the criteria by which the website is considered to be "working",high, medium or low defects will be identified and cataloged for further improvements or regression testing.
The UAT critreria and results will confirm if the website can handle required task in a real-world scenarios, according to the Requirements Traceability Catalog Table 1.0.

*Table 2.0 User Acceptance Testing (UAT)*


 Test#    | User stories Ref# |        Description of task        |               Steps to evaluate    |                        Expected Result                                                                                                                                                                                                                             |            Pass / Fail / Comments                             |  
--------  |-------------------|-----------------------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------| 
APT-H-1.0  | H-1.0             | Home nav link                        | APT-H-1.0.1: Click home nav link | The link should be funtional and take the user to the home page section displaying the carousel image slider.                                                                                                                                                    |                     Pass                                      |
APT-GA-2.0  | GA-2.0           | Game nav link                        | APT-GA-2.0.1: Click Game nav link| The link should be funtional and take the user to the game section.                                                                                                                                                                                               |                     Pass                                      | 
APT-BL-3.0  | BL-3.0           | Buy nav link                         | APT-BL-3.0.1: Click Buy nav link| The link should be funtional and take the user to the Buy section.                                                                                                                                                                                                   |                     Pass                                      | 
APT-CON-4.0  | CON-4.0           |Contact nav link                    | APT-CON-4.0.1: Click Contact nav link| The link should be funtional and take the user to the Contact & Blog section.                                                                                                                                                                                   |                     Pass                                      | 
APT-BBT-5.0  |BBT-5.0            | Buy Btn                            | APT-bbt-5.0.1: Click Buy Btn |The button should be functional and allow the user access to view the shopping cart.                                                                                                                                                                                     |                     Pass                                      |                                                                                     
APT-PP-5.1   | PP-5.1            |Pay pal Check-out-btn               | APT-PP-5.1.1: Click Pay pal Check-out btn| The button should be functional and allow the user access the Pay Pal pop up login window, insert their credentials, validate the inputs and complete the purchase, once the purchase is successful the system will display a payment confirmation page ,or it will display a paymemt cancel page |                     Pass                                      |
APT-PP-5.2  | PP-5.2            | Pay pal Guest-check-out-btn         | APT-PP-5.2.1: Click Pay pal Guest-check-out btn | The button should be functional and allow the user access the credit/debit card drop down form, insert their credentials, validate the inputs and complete the purchase, once the purchase is successful the system will display a payment confirmation page ,or it will display a paymemt cancel page |                     Pass  |                                                                        
APT-RS-5.3 | RS-5.3             | Retun to Shopping Link              | APT-RS-5.3.1: Click the Return to shopping link | When the user is on the payment page they can exit the page by clicking the link which will take them back to the foxx games website.                                                                                                               |                     Pass                                      |
APT-CS-5.4  | CS-5.4             | Continue Shopping Link             | APT-CS-5.4.1:Click the Continue shopping link | When the user is on the payment confirmation page they can exit the page by clicking the link which will take them back to the foxx games website.                                                                                                    |                     Pass                                      |                                                                
APT-CS-5.5  | CS-5.5            | Continue Shopping Link              | APT-CS-5.5.1: Click the Continue shopping link |  When the user is on the cancel confirmation page they can exit the page by clicking the link which will take them back to the foxx games website.                                                                                                   |                     Pass                                      |
APT-CUB-6.0  | CUB-6.0          | Contact us btn                      | APT-CUB-6.0.1:Click the Contact us Btn| The button should be functional and trigger the modal contact form to pop up , it should accept the user's details and validate their inputs.                                                                                                                                          |                     Pass                                      |
APT-SB-6.1  | SB-6.1            | Send Button                         | APT-SB-6.1.1: Click on the send button | The button should be functional, once it is clicked the system should submit the information via email.js to the seller.                                                                                                                                     |                     Pass                                      |
APT-RB-6.2  | RB-6.2            | Reset Button                        | APT-RB-6.2.1: Click on the Reset button | The button should be functional, once it is clicked the system should clear all input fields.                                                                                                                                                              |                     Pass                                      |
APT-LR-7.0  | LR-7.0            | Login/Register Button               | APT-RB-7.0.1: Click on the Login/Register button | The button should be functional, and display the login/register page for the user to register, accept the user's inputs or allow the user login using social media networks.                                                                                                                                                              |                     Pass                                      |
APT-ASO-8.0 | ASO-8.0         | 1979 Asteroid                         | APT-PAR-8.0.1: 1979 Asteroid | The game should be functional, allow the user to view the game in AI mode and allow the user exit the game by pressing the exit button , when the game starts or ends.                                                                                                |                     Pass                                      |
APT-ASO-8.1 | ASO-8.1         | 1979 Asteroid                         | APT-PAR-8.1.1: AI Software | The AI should be able to play the 1979 Asteroid game independent of any asistance from the user. The AI should keep improving its performace and score as it plyas the game over and over again.                                                                        |                     Pass                                      |
APT-ASN-9.0 | ASN-9.0         | 2020 Asteroid                         | APT-PAR-9.0.1: 2020 Asteroid| The game should be functional, allow the user to play the game and allow the user exit the game by pressing the exit buttom , when the game starts or ends.                                                                                                            |                     Pass                                      |



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
