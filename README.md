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

### Features Left to Implement
- NONE

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

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

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with all inputs valid and verify that a success message appears.
    4. Press 'Return to Original Site'

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X