### Final Project

My final project is public mobile rating website. Users are able to register, rate mobiles and even without registering then can just look at the rating and information of the mobiles. The average rating is updated each time a new rating is given to the mobiles and when a user rates a mobile it is added to their profile. Admin can add new mobiles to the database which is displayed to everyone and only he/she can do it so that there are no duplicates and the information is verified and legit. Basically the website shows all the ratings of mobiles on a scale of 10 which are given by verified public users and each user can see what mobiles they rated.

The project was built using Django as a backend and all the information is stored in database which is SQLite.

### Installation

 - Install project dependencies by running `pip install -r requirements.txt` . It includes Django.   
 - Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate` .
 - Create superuser with `python manage.py createsuperuser` . This is a must step because only admin can add mobiles to the website along with description and default rating.
 - Run the server with `python manage.py runserver` .it gives you a link copy and paste it on your browser and it will load the website.
 - At the end of the URL type `/admin` , to get the admin login window, enter the credentials and add new mobiles for the website along with their descriptions and default rating.
 - Go to the default URL and you will be shown all the mobiles, you can register an account.
 
 ### Files and Directories
 
 - `mobilereviews` - main application directory
    - `static/mobilereviews` contains all static content
        - `styles.css` - script that sets all the style properties of the website.
    - `templates/mobilereviews` contains all application templates.
        - `layout.html` - base template which is extended by all the other templates, it contains - the header and the footer section.
        - `index.html` - this template shows all the mobiles in form of cards along with the ratings.
        - `mobilepage.html` - this template is shown when we click on any mobile in the index template to display the descripton of the mobile along with a    larger size image and provision for registered users to give their own rating for the mobile.
        - `profilepage.html` - this template shows the username of the user and all the mobiles that user has rated and this is only available to the logged in users.
        - `login.html` - this template displays a form to take input from the users to verify and log them into the website by checking the credentials in the database.
        - `register.html` - this template displays a form to take input from the user to register him/her into the database.
     - `admin.py` - here the admin classes are added for the admin to add new mobiles into the database.
     - `models.py` - it contains three models which are used in the project.
         - `User` model extends AbstractUser.
         - `UserRatings` model stores the `user` and `mobileid` to link the user and mobile which the user has rated.
         - `Mobiles` model is used to store the mobile image,title,description and rating and number of ratings.
      - `urls.py` - contains all application URLs.
      - `views.py` - contains all application views(functions which run the particular operations).
 - `capreviews` - project directory.