# Project 4 Django - Shopping List

The shopping list product is a website which allows users to login to an application, view thier shopping lists, add items, edit items and remove items as appropriate.
The application is fully responsive and mobile friendly, so that it can easily be used on the move, while you are in the shop.  All data is realtime, so updates are immediate to help the user experience, by allowing users to know exactly what they need to purchase, and also know what has been purchased.
The user can add a description to the items incase they want a particular brand of item for exmaple, this is also fully viewable via mobile devices.
The shopping list application was designed and planned using agile methodoligies - so broken down into tangeable pieces of work, placed into iterations and worked through systematically until desired outcome achieved. 
During deisgn, planning and devlopment, due care was taken to put the user first in relation to thier needs and also user experience in terms of ease of use along with enjoyment.  The enjoyment and ease of use is through easy navigation and clear utilities.
The shopping list application was througughly tested, as will be documented and made available in this document. 
Security is also in mind when devloping this application, aloowing only looged in users to access the site and to also only allow users to see thier own data.
I think you will agree, that this application is a very useful and easy to use tool to help many shoppers!

![Web Page view](assets/images/Shop%20List.png)

# Agile Methodology/framework
- A big part of this project was to think ahead and plan, design, prioritise and timebox tasks.  It was a great way to make me think about smaller chunks of work and plan out my project.
- By more planning I felt that I could conceptulise and not get too far ahead, allowing me to focus on certain items of delivery, step by step, not to just focus on end result. 
- I learned how to use this via github and to break tasks down into manageable chunks of work, and again to focus on these as MVP vs everything I'd like to deliver. 
- CRUD - I've designed, planned and executed all of the CRUD functions.  My application allows a user to:-
    - Create - New Accounts, new shopping items
    - Read - Information is collected and stored, and is made readable on UI via the database. 
    - Update - Current stored data can be changed and updated, and again made visible on UI via database.
    - Delete - Stored information can also be deleted.  This information is then rendered on UI via database.
 

# Features

There are many features included in the shopping list application.

- __Secured Credentials__
    - A user must have login credentials to use the site
    - With login credentials, a user can only view thier own details
    - There is a create account function to allow users without login to create one and use site straight away.

<br>

- __Easy Navigation__
    - A user can easily navigate through the site via clear links and one click utilisation.
    - Pages are clear and concise, with no confusion
    - Clear instruction on options to add/edit/remove items from list.

<br>

- __Hover Over__
    - All links have a hover over function, that clearly identifes the options by highlighting in a different colour.  This adds to the user experience also.
    
<br>


- __Strike Through__
    - When an item is complete, the shooping list will clearly identify this by striking through the item - clearly allowing the user to see what is no longer required to purchase.

<br>

- __Descriptions__
    - An option to add an item description to allow the user to identify an amount, a brand or any other instructions to remind them of particulars to any item on list.

<br>

- __Mobile Friendly__
    - Application is very device friendly.  This is very important for this app in particular to allow users to use on the go, when at shops for exmaple. 

<br>

- __Notifications/Messaging__
    - When actions complete by user, messaging appears to inform of success.

<br>

# Features left to implement 

- Messaging - The messaging is not as I want it to be, it works for most pages but not all.  I would also like to have the message pop as an alert and not remain on screen

- Search - the ability to search whilst typing first number of letters.  Currently the search only works after letters are entered and search clicked.  I would like this to work a bit slicker.

- Overall better UI - I would spend more time on making the user interface a bit more fun and exciting, currently its very basic, with colours a little bland. 

- On the Add/Edit page, I'd like to distingish between when the user is adding a new item or editing.  Currently, I bring the user to the same page and therefore the button remains as 'Add' rather than 'Edit'..which would be a nice change.

- A vast improvement I would make would also be the option to mass un-complete items.  As a shopper, its likely that I will have many items in which I regularly purchase, so I do not want to totally remove.  Each shop trip, I do not want to individually un-complete each item to reset my list. 

- Another idea would be to categorise items into sections like - fridge, freezer, household etc to allow the user to focus on items to purchase for certain needs. 

- My code is not superb in a number of ways.  I found myself going down a particular path and went so far I did not feel I could go back.  My file setup is not ideal, the use of Main.html and CSS files are a bit mixed up.  I did not have a lot of styling to do initially, so used the main file for most styling.  I do not have a seperate CSS file.  This is not ideal design or setup...I realise this.  I did start to go back to change and was messing things up, and with time left, I just did not want to do this.




## Testing

- There was a lot of testing throughout this project.  Each and every small change was tested as I went.  I wanted to avoid any last minute bulk testing and therefreo refactoring, so testing as I developed my way through was how I approached this.
<br>

- A large part of my testing effort was spent whilst trying to achieve user credentials.  It was difficult for me to only only certain users view thier own shopping items, it took a lot of iterations and attempts to get this right, but evtually I got there.
<br>

- Another large testing effort was when trying to add items to the list and have them render on the list.  Thi was another tough part to implement for me, and also took a lot of testing efforts.  Same can be said for the edit piece and completion.  As this was a key deliverable, I wanted to make sure it was water tight.
<br>

 - **Browser Testing** - As part of my testing I covered Browser testing across numerous platforms, Safari, chrome, firefox and IE.  I wanted to make sure my site worked and was compatible througout and for all users using different browsers.
 <br>

 - **Responsiveness** - As well as testing on browsers, it was very important that I verified that my site and all its functions behaved as expected with diffeerent screen sizes along with different devices.  This was also quite heavy lifting to make sure I got this working as expected, responsiveness is something I have struggled with in the past and continue to.. but I'm glad to say that any issues that I was finding, I was able to resolve. 
 <br>

 - **Code Validation** - Part of the testing efforts are not just about the functional side of the product, its also very important that its Accessible, Performant and the code has been written using best practises.  It is also important that the code written is in the right format and using correct syntax etc.  I did this testing through the use of a number of tools - Lighthouse, HTML and CSS validators etc.  Again, this took a bit of back and forth with fixing some items, but I feel I have got most of the way there now.  I'm still having issues with some accessibility on on one of the pages inreation to lack of labels on a form - I'm struggling with this while using inherited form inout fields in Django. 

 - **Use Case** - All the above testing is great, but its of no value if the product does not do what it is meant to do!  As mentioned, I did test throughout as I was developing, and made sure that each use case was tested to make sure I was meeting the initial use cases.  While the majority of the use cases pass the test, there were a couple of which I think could be of a better quality.

 - I have documented all of my testing artifacts [HERE](https://docs.google.com/document/d/1uQKhwsAWQFkDNJyRhFb0ZnhQMKr5agaUtXkrfFofBmo/edit) 


 ## Unfixed Bugs 

 - I have messaging on all actions, bar the Logout.  I have struggled with deriving the message with the way in which I've developed my pages and links.
 <br>

 - Similar to the previous issue - I feel that the messaging isn't great, not quite a bug, but something a customer might report as not a great experience.  I would really prefer to have this as a pop up message that then dissapears after time, instead of remaining on screen until next action.
<br>

- Unable to trigger a message to identify the removal of an item.  No message appears when this action is taken.  I hope I have left enough time to try and rectify this problem

- One big issue! If I do not logout of the application, then spin it back up again, I seem to still be logged in as last user.  I couldn't quite find a way to make sure that by closing the session out that it would also log a user out.  This is a problem.  As I write this, I'm allowing myself time to see if I can fix this...but as of now, this is a bug!


# Deployment

- In order to deploy my project and make it available to run via a visual program, I needed to synch my GitHub project through Heroku.  I had to sign up for a new account, add credentials, link to the correct repository and add some settings to allow for seemless deployment.  One thing I made sure to do was set to automatic deploys, which meant each time I pushed through gitpod, these changes would then render to the new GUI. My Heroku dashboard - 
- My project is deployed via Heroku.  My live published site - 
- My GitHub repository is housed here - https://github.com/kevinmcsherry/P4_Shop_list 
<br>

# Shopping List User
- My Admin user Credentials for the shopping list app : - Username - kevmac  Password - shop1234

# Credits

- I was venturing into unknown territory here with the use of Django and Boostrap etc.  I have to say that I did struggle to get to terms with it...as I find it quite different from the coding we have done in past projects.  I had to rely on a lot of the content from LMS program and the practise projects.  
- The todo list along with the 'I think before I blog' project aided me in many ways, from getting started with set-up of django and framework and also the database set up.  I also used a lot of the template structures to help me with getting basic designs set up. 
- I never rely on just one source for my help.  I did a lot of research online to see about other sources that could help me in the development of this project.  I came across some really helpful content and with a particular person on youtube called Denis Ivanov, thats content really helped.  He has tutorials online and also lots of content online which I could not have got to the stage I'm at without.  I used a lot of his content on his [website](https://www.dennisivy.com/), and a lot of his advice through his video content.

# Project Summary
- Tough!  I felt comfortable with past projects becuase I was comfortable doing a bit of coding.  I felt this took me out of my comfort zone and was a challenge bringing me back to HTML and CSS.  I have always struggled a little with designing and styling my front ends. 
- I had a number of different ideas in which I was going to follow, which I then backtracked becuase of the potential difficulty.  I went with a task 'to-do' app... which i began to develop, then decided it was too vanilla, so changed my mind half way through and made it a Shopping list.. Not hugely different, but slightly different spin.  As easy as that sounds it caused me some issues with naming conventions of files etc, as I had gone so far down one route and doubled back.. so the naming is a bit mixed as it stands.
- I really wanted to come up with something much more exciting for this project deliverable, so I'm a little disapointed in the end result.  I need to put more time into learning this framework and especially back into basic web site design.
- As part of the Agile practise, I really was keen to carry out the work in the correct cadence and flow.. what I unfortunately ended up doing was jumping into solutionising and coding first... which meant retro fitting the tasks which should have preceeded.  So not ideal. 
- Overall, I learned a huge amount during this project..I got a real understanding of all the things I did not appreciate about the development cycle and the effort that go into it.  The planning and forward thinking was a challenge, as I just wanted to dive right in.  I also learned a lot about other frameworks and libraries that I was not aware of and surpirsed by the power that they give in relation to work that is already done and not required to be redone!
