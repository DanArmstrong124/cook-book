# Dan's Delicious Dishes - A Cook Book

This project is an online cook book designed for a community to share their meals and recipes with eachother, they will be able to add, edit and delete their meals.

The cook book will have multiple pages with FAQ's and contact pages. Information about the website and the chef will be included to give it a personal touch.
 
## UX

- As a cook, I want to be able to find recipes to use for a meal so that I can use them in my restaurant.
- As a cook, I want to be able to share my recipes for other people to use so that I can help provide tasty food to the community.
- As a cook, I want to be able to remove my recipes so that I can keep them personal or if I have created a listing in error.
- As a cook, I want to be able to get in touch with the creator of the site so that I can advertise or to receive help for an enquiry.
- As a customer, I want to be able to see the values of this online business so that I can see if this is a good website to use.
- As a cook or customer, I want to be able to sort the meal listings by certain criteria to allow myself to find meals with ease.

The wireframes that I created using [Balsamiq](https://balsamiq.com/wireframes/) are found in the WireFrames/mobile and WireFrames/desktop folders.

## Features

### Existing Features

- All Pages:
- - Header: This is the pages header that will hold onto the links to other pages.
- - Footer: This is the pages footer that will hold onto the copyright and advertisement.
- - Bottom Page Advert: This will be the advert that is fixed into the footer.
- - Mobile Menu: This is a side-opening menu for mobile users.
- - Responsive Design: Used via [Materialize CSS](http://archives.materializecss.com/0.100.2/grid.html).

- Home Page: The home page that the user will initially see, contains the list of meals.
- - Mini Description: This is a description of the website and a small about me on the home page.
- - Meal List: This is the full list of meals, found with ease on the home page.
- - Side of Page Adverts: Only found on the home page (As it is where the meals are), this will contain adverts made by myself for the website linking to Argos for cuttlery etc.
- - List Of Meal Buttons: Contains (MAKE ME, Edit and Delete).
- - Sort By: This is a sort by that allows the user to sort the meals by Country or Desserts.

- Add Meal Page: A page that allows a user to add a meal to the database.
- - Add Meal Form: A form that allows the user to give information on their meal before pressing submit.

- Edit Meal Page: A page that allows a user to edit a meal to then copy it to the data base with amendments.
- - Edit Meal Form: A form that is Pre-Filled with the meals information taken from the database ID.

- Delete Meal Page: A page that allows a user to confirm the deletion of a meal.
- - Yes or No Buttons: Buttons to help the user decide without mistake and ease on whether or not they are sure on deleting the meal.

- Contact Page: The page a user can use to send a contact form to us.
- - Contact Page Form: A form for the user to fill out for any enquires.
- - FAQ: Some frequently asked questions and answers.

- About Page: The page a user can use for information on the site and the chef.
- - The Chef: A made up chef for the website, with details adjusted from [Gordon Ramsay Wiki](https://en.wikipedia.org/wiki/Gordon_Ramsay).
- - Our Values: Some Small Values for the pretend business.
- - Our Vision: A Small Vision for the pretend business.
- - Our Mission: A Small Mission for the pretend business.

- Sorting Pages: The pages linked into the main.html using Jinja and Flask to sort the listing for the user.
- - African, American, British Etc.
- - Contain the Side of Page Adverts.

### Features Left to Implement
- NONE

## Technologies Used

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [HTML](https://en.wikipedia.org/wiki/HTML#:~:text=Hypertext%20Markup%20Language%20(HTML)%20is,such%20as%20JavaScript%20and%20VBScript.)
    - The project uses **HTML** for the front end.

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - The project uses **CSS** for styling.

- [PYTHON](https://www.python.org/)
    - The project uses **PYTHON** for back end applications.

- [FLASK](https://palletsprojects.com/p/flask/)
    - The project uses **FLASK** with **PYTHON** for the back end applications, linking to **JINJA** template **HTML**s.

- [JINJA](https://jinja.palletsprojects.com/en/2.11.x/)
    - The project uses **JINJA** with **HTML** to create template HTML pages.

- [PYMONGO](https://pypi.org/project/pymongo/)
    - The project uses **PYMONGO** to link **PYTHON** to **MONGODB**.

- [MONGODB](https://www.mongodb.com/)
    - The project uses **MONGODB** for its database storing all the meal data.

- [HEROKU](http://heroku.com/)
    - The project uses **HEROKU** to deploy the application and all the files to, this makes it public.

- [BALSAMIQ](https://balsamiq.com/wireframes/)
    - The project used **BALSAMIQ** for its WireFrames.

- [MATERIALIZE](https://materializecss.com/)
    - The project uses **MATERIALIZE** with **CSS** & **JQUERY** for responsive design and other styles and components.

- [GITHUB](www.github.com)
    - The project uses **GITHUB** to backup the files into repositories.

- [GITPOD](www.gitpod.io)
    - The project uses **GITPOD** for its IDE.

- [FORMSPREE](https://formspree.io/)
    - The project uses **FORMSPREE** for its Mail Capability with JS.

## Testing

To begin my testing, I created the application and would use 'Python3 app.py' to run a preview in the browser. To ensure that it was an up to date version I made the port public and ran the preview inside of an incognito window.

After multiple tests we collated, I took them down and wrote them out in a simple format that others could understand. I then got my family and friends involved in testing the following, with the results below each test:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with all inputs valid and verify that a success message appears.
    4. Press 'Return to Original Site'

- Result was met, user was satisfied.

2. Add Meal form:
    1. Go to the "Add Meal" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with all inputs valid.
    4. Look for your meal at the bottom of the list.

- Result was met, user was satisfied.

3. Edit Meal form:
    1. Go to the "Edit Meal" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with all inputs valid.
    4. Look for your meal at the bottom of the list.

- Result was met, user was satisfied.

4. Sort By buttons:
    1. Go to the "Home" page
    2. Press "Sort By"
    3. Choose an option
    4. If empty choose a different filter OR add a meal with that filter and restart through steps 1-3.
    5. Verify that your meal is there.

- Result was met, user was satisfied.

5. Delete meal:
    1. Go to the "Home" page
    2. Select a meal
    3. Press the red button with the trash icon.
    4. Press yes once redirected.
    5. Verify the meal is no longer on the list.

- Result was met, user was satisfied.

6. View meal:
    1. Go to the "Home" page
    2. Select a meal
    3. Press the green "MAKE ME" button
    4. Verify the meal name and details once redirected.

- Result was met, user was satisfied.

7. Home page links:
    1. Go to the "Home" page
    2. In the mini about at the top of the "Home Page" press each link.
    3. Verify they take you to where you would expect.

- Result was met, user was satisfied.

8. Drop Downs:
    1. Go to the "Contact" page
    2. Under "FAQ" press/click a questions
    3. Verify it drops down with the answers
    4. If there is a link, verify link takes you to where you would expect.

- Result was met, user was satisfied.


Throughout the testing from my friends and family, no bugs were met, they were able to find their way around the website without asking me how to do anything.
I attempted to break my site by going between links and going back, to my best knowledge there isn't a single major bug that will affect the user experience.

I tested the responsive design myself and with friends and family and the feedback given was that you can read all text clearly, buttons are not a struggle to find and everything sits nicely.

## Deployment

I have deployed this project to Heroku.

Throughout my project I have been using git and heroku to ensure that I have a backup of the files as well as deployment.

My GitHub contains all the files, and the Heroku contains all of the files including the Procfile of which pushes it to run the application app.py to make the site live.

My values that I had to add consist of IP, PORT, MONGO_URI & MONGO_DBNAME.

The MONGO_URI and MONGO_DBNAME are found inside of an enviromental python file, of which contains "os.environ.setdefault" for both & The IP and PORT to ensure that I can then import it safely into my app.py without the chance of someone being able to access my data.

I have used a .gitignore to ensure that certain files are not for public use as they may contain DB information or anything else that does not concern the public eye.

When I need a quick preview for development, through GitPod I deploy my preview by typing "Python3 app.py" into the terminal and following the connection into an incognito browser after making the port public.


## Credits

### Content
- The chef photo contains myself and a [Google Images](https://images.google.com) of [Gordon Ramsay](https://www.google.com/search?q=gordon+ramsay&sxsrf=ALeKk01C4pp0TILt_xG0WYf6k1wdJORxfQ:1593440424326&source=lnms&tbm=isch&sa=X&ved=2ahUKEwidt9mTnKfqAhWdQkEAHa2yBI8Q_AUoAnoECCEQBA&biw=1600&bih=757#imgrc=UBi_exyulk5kgM)
- The icons used are from [Materialize Icons](https://material.io/resources/icons/?style=baseline).

### Media
- The advert photos were created by myself.
- The chef photo was photoshopped by myself, containing myself and [Gordon Ramsay](https://www.google.com/search?q=gordon+ramsay&sxsrf=ALeKk01C4pp0TILt_xG0WYf6k1wdJORxfQ:1593440424326&source=lnms&tbm=isch&sa=X&ved=2ahUKEwidt9mTnKfqAhWdQkEAHa2yBI8Q_AUoAnoECCEQBA&biw=1600&bih=757#imgrc=UBi_exyulk5kgM)

### Acknowledgements

- I received inspiration for this project from Code Institutes examples.
- I received inspiration of what was needed for a business value etc, via [Google](https://google.com) and proceeded to create my own.
- The adverts redirect to [Argos](https://argos.com).