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
 The website is based on a fictional FOXX GAMES website, the website theme is based on vintage Atari, Nintendo and Sega games.The user will be able to 
 scroll through the web page, buy games and preview the classic 1979 Asteroid game in AI Mode, while the 2020 Asteriod game will be in play mode.
 I went through two tutorials and implemented the code, the results was two fully functional games, I also took a tutorial on Neural networks for 
 the 1979 Asteriod game and managed to  build a Neural network that enabled my computer to learn how to play the game, this resulted in an Artifical 
 inteligent software that became better over time as I allowed the computer to playing the game, the first score was 80,789 level 15 utilizing all 3 lives, 
 the second attempt was 97,980 level 17 utilizing all 3 lives, I now have a good understanding of neural networks and the math associated with neural networks, 
 I intend to continue improving on my skills by taking a course with intellipat and IBM on machine learning and eventually become certified for Machine learning and 
 Artifical Intelligence. This project is supposed to showcase my skills in HTML, CSS, JavaScript & Jquery. Other features include the intigation of Pay 
 Pal and emailjs API into the webdesign.The development of this website is purely for educational purposes and not intended for commercial use.
 
----------------------------
 ## User-stories

 ### Requirement Gathering
 
 The table below will breifly describe the user stories for the functional and non-functional requirements, the user stories decribed in
 **Table 1.0 Requirement Traceability Catalog** will be Independent, Negotiable, Valuable, Estimable, Smart and Testable, **INVEST** in nature and composition.

 *Table 1.0 Requirement Traceability Catalog*

HLR   |  HLR Ref# |    HLR Description    |                              User Stories                                                    |                                                      Acceptance criteria                                                                                        |                                MoSCoW                                                                                                                |
------|---------- |-----------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------| 
Home  | H-1.0     | Gain access to Foxx games website   | **As a** user **I want** to access the web page  **so that** I can gain access to the site content.| **Given** that the user is on Foxx Games web page, **When** they click on the Nav links Home **then** the system will take the user to the home section of the web page. |     M   |
Games | GA-2.0| Gain access to Foxx games website | **As a** user **I want** to access the games section  **so that** I can have access to New upcoming games section.| **Given**  that the user is on Foxx Games web page, **When** they click on the Nav link games **then** the system will scroll down to the  new section and display the information |    M   |
Buy  | BL-3.0| Gain access to Foxx games website | **As a** user **I want** to access the Buy game section  **so that** I can have access to buy game section.| **Given**  that the user is on Foxx Games web page, **When** they click on the Nav link Buy **then** the system will scroll down to the buy game section and display the information |    M   |
Contact | CON-4.0| Gain access to Foxx games website | **As a** user **I want** to access the contact and blog section  **so that** I can have access the contact btn and blog section.| **Given**  that the user is on Foxx Games web page, **When** they click on the Nav link contact **then** the system will scroll down to the contact us and blog section where the user will be able ta access the blog information and the contact us btn |    M   |
Buy btn | BBT-5.0|  Gain access to Foxx games website| **As a** user **I want** to access the buy game btn **so that** I can buy the game(s) of my choice.| **Given** that the user is on Foxx Games web page, **When** they click on the buy btn **then** the system will take the user to the payment page, where the user can view the shopping cart details before they make a decision to buy the item(s) .|    M  |
Pay Pal btn | PPB-5.1| Gain access to payment page | **As a** user **I want** to access the Foxx Game payment page **so that** I can buy the items(s) in my shopping cart.| **Given** that the user is on Foxx Games payment web page **When** they click on pay pal check-out btn  **then** the system will display the users pay pal account details to complete the transaction, once this is sucessful, the system will display a payment confirmation page. If the transaction is not successfully or canceled by the user, the system will display a cancel confirmation page |    M |
Pay Pal btn | PPB-5.2| Gain access to payment page | **As a** user **I want** to access the Foxx Game payment page **so that** I can buy the items(s) in my shopping cart.| **Given** that the user is on Foxx Games payment web page **When** they click on pay pal Guest-check-out btn  **then** the system will display a drop down credit/debit card form for the user to fill in their details to complete the process, once this is sucessful, the system will display a payment confirmation page. If the transaction is not successfully or canceled by the user, the system will display a cancel confirmation page|    M |
Return to shopping link | RS-5.3| Gain access to payment page | **As a** user **I want** to access the Foxx Game payment page **so that** I can return to foxx games  website.| **Given** that the user is on Foxx Games payment web page **When** they click on the return to shopping link  **then** the system will take the user back to the home page.|    M |
Continue shopping link | CS-5.4| Gain access to the payment confirmation page | **As a** user **I want** to access the Foxx Game payment confirmation page **so that** I can  return to foxx games  website.| **Given** that the user is on Foxx Games payment confirmation web page **When** they click on the continue shopping link  **then** the system will take the user back to the home page.|    M |
Continue shopping link | CS-5.5| Gain access to the payment cancel page | **As a** user **I want** to access the Foxx Game cancel confirmation page **so that** I can  return to foxx games website.| **Given** that the user is on Foxx Games cancel confirmation web page **When** they click on the continue shopping link  **then** the system will take the user back to the home page.|    M |
Contact Us btn| CUB-6.0 | Gain access to Foxx games website | **As a** user **I want** to access the contact us btn **so that** I can access to the contact us form.| **Given** that the user is on Foxx Games web page, **When** they click on the contact us btn **then** the system will display a pop up modal form and allow the user make their inputs . |    M   |
Submit btn | SB-6.1 | Gain access to Foxx games website | **As a** user **I want** to access the contact us section **so that** I can access the contact form submit btn.| **Given** that the user is on Foxx Games contact form, **When** they click on the submit btn **then** the system will submit the message via emailjs to the seller. |    M   |
Reset btn | RB-6.2 | Gain access to Foxx games website | **As a** user **I want** to access the contact us section **so that** I can access the Reset btn.| **Given** that the user is on Foxx Games web page, **When** they click on the Reset btn **then** the system will reset the input fields. |    M   |
Login/Register | LR-7.0 | Gain access to Foxx games website | **As a** user **I want** to access the Login/Register Btn **so that** I can gain acesss to the Login/Register form.| **Given** that the user is on Foxx Games web page, **When** they click on the login/register btn**then** the system will give the user access to the Login/Register page and form. |    M   |
1979 Asteroid | ASO-8.0 | play the 1979 Asteriod Game | **As a** user **I want** to access the games section **so that** I can acesss the 1979 Asteroid game.| **Given** that the user is on Foxx Games web page, **When** they click on the press play btn **then** the system will allow the user view the 1979 Asteroid game in AI mode. |    M   |
2020 Asteroid | ASN-9.0 | play the 2020 Asteriod Game | **As a** user **I want** to access the games section **so that** I can access the 2020 Asteroid game.| **Given** that the user is on Foxx Games web page, **When** they click on the press play btn **then** the system will allow the user access and play the 2020 Asteroid game. |    M   |



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
