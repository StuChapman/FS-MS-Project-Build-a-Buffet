# Build-A-Buffet

 Link to the deployed wesite [heroku](https://build-a-buffet.herokuapp.com/)

 Link to the GitHub repository [github](https://github.com/StuChapman/FS-MS-Project-Build-a-Buffet)

Create a  build a full-stack site for Build-A-Buffet, providing an authentication
mechanism and paid access to facilitate the purchase of a product/service.
Build-A-Buffet is a mail order catering service that creates buffet meals for: Wedding, 
Parties, Functions and Corporate Events. They provide a selection of menus at varying price points
to suit the expectations of each event. There will also be the ability to have a menu built for the Customer;
by input a range of criteria and having the site build the menu to suit the criteria 
(e.g. No. of guests, dietary requirements etc.)

## UX

The app should be designed ‘mobile first’, and should be equally as accessible through desktop and laptop devices.
Navigation should be intuitive and errors handled gracefully.

### User Stories 

### As a Customer of Build-A-Buffet, I …

1.	… want to understand what Build-A-Buffet do; visually and quickly, without having to navigate 
    through lots of information.
2.	… want to be able to browse the different products and services.
3.	… want to be able to create a bespoke menu by selecting from all produce.
4.	… want to be able to have a menu suggested to me, based on my requirements.
5.	… want to be able to choose from different dietary requirements (e.g. vegetarion, vegan)
6.	… want to be aware of any allergy advice for each product.
7.	… want to be able to see the price of each product and the total price of my basket at any point.
8.	… want to be able to see the price per person where it is applicable.
9.	… want to be able to make online purchases of products and services.
10.	… want to be able to arrange delivery to a location in the UK of my choosing.
11.	… want to be able to create a user page, where my personal information and order history is stored.
12.	… want the site to be secure and my personal and payment information kept safe.

### As a Site-Owner of Build-A-Buffet, I …

1.	… to be able to maintain a list of products.
2.	… to be able to track orders.
3.	… to be able to track payments and webhooks

I designed the site around the following views:

**index.html** - to introduce the user to the company and provide navigation to the other areas of the site.

**allergies.html** - to understand how different dietary and allergy requirements are accomodated.

**products.html** - to list all the products based on the user's menu selection.

**search_products.html** - to return all the products based on the user's search parameters.

**product_detail.html** - to provide more detail on each product including servings and options (where applicable).

**basket.html** - to view all the products currently in the basket.

**edit_product.html** - to edit the products currently in the basket.

**checkout.html** - a secure checkout where registered and guest users can make purchases.

**order_success.html** - to show an order has been processed succesfully and to show previous orders.

**bartholemew.html** - to assist the Customer in building an appropriate buffet, based on thier requirements.

**bartholemew_output.html** - to display to the the Customer Bartholemew's suggested buffet (along with cost information).

**profile.html** - to allow the Customer to store and update personal information and view order history.

**service.html** - to contact the Site-Owner through a question form.

For the Site-Owner ...

**product_admin.html** - to modify/delete: product, option or category.

**add_product.html** - to add: product, option or category.

Allauth libraries were used for sign up, log in and email validation

### Mockups:

I produced the following mockups prior to writing any code. I had sourced the 'Grayscale' template from [start bootstrap](https://startbootstrap.com/previews/grayscale) and stock images from [pexels.com](https://www.pexels.com/)
I used this theme and these images in the mockups.

[mobile](https://github.com/StuChapman/FS-MS-Project-Build-a-Buffet/blob/9fbda7273790057f9811372369486760befb401f/mockups/Full_Stack_Frameworks_With_Django_MOBILE.pdf)

[desktop](https://github.com/StuChapman/FS-MS-Project-Build-a-Buffet/blob/9fbda7273790057f9811372369486760befb401f/mockups/Full_Stack_Frameworks_With_Django_DESKTOP.pdf)

### Colour Schemes and Fonts

The core scheme of the app is the 'Grayscale' theme from [start bootstrap](https://startbootstrap.com/previews/grayscale)

The main colour scheme is based on the 'GET STARTED' button on 'Grayscale'. I used variations of this colour to give a 'brand' to the site.

1. #303F3F for main text
2. #71B7B2 for mouseover text
2. #426765 for buttons and secondary text

The main fonts used in 'Grayscale' are:
 
 1. font-family: 'Nunito'
 2. font-family: 'Varela Round'

I used these fonts exclusively.

### Approach

The approach I took for designing the site, was to start with the small media device, portrait view, design that, then make any adaptations
for a tablet, portrait view, and finally any changes for a large size, landscape view..
I constructed the code in the mobile-first, portrait view, then added specific media queries for portrait and lanscape views.
I again used code from [stackoverflow.com]https://stackoverflow.com/questions/43589507/how-can-you-have-bootstrap-responsiveness-based-on-screen-ratio-instead-of-scree) to enable this.
Finally, I added bespoke media queries for screen sizes.
I also set font sizes to be responsive, utilising some code from [css-tricks](https://css-tricks.com/books/fundamental-css-tactics/scale-typography-screen-size/) 
and [made by Mike](https://www.madebymike.com.au/writing/fluid-type-calc-examples/)

font-size: calc([minimum size] + ([maximum size] - [minimum size]) * ((100vw - [minimum viewport width]) / ([maximum viewport width] - [minimum viewport width])));

This code, along with using vw and vh for font sizes and certain features, such as banners and images, allowed the site to be almost fully responsive across different portrait view sizes.

## Features

### Existing Features

... to understand what Build-A-Buffet do; visually and quickly, without having to navigate
1.  Navigation Menu at top of screen
2.  Link to bartholemew.html to assist the Customer in getting started
3.  A Search Bar at top of screen
4.  View of current basket
5.  Information on food
6.  A link to allergies.html for dietary info
7.  Contact info at foot of screen

... to be able to browse the different products and services.
1.  Menu list of products
2.  Ability to search products

... to be able to create a bespoke menu by selecting from all produce.
1.  Add products to Basket
2.  Edit products in Basket
3.  Delete products from Basket

... to be able to have a menu suggested to me, based on my requirements.
1.  Input requirements and output menu based on requirements

... to be able to choose from different dietary requirements (e.g. vegetarion, vegan)
1.  Dietary requirements captured
2.  Dietery information presented

... to be aware of any allergy advice for each product.
1.  Allergy requirements captured
2.  Allergy information presented

... to be able to see the price of each product and the total price of my basket at any point.
1.  Price per product is presented in the Basket
2.  Total price is presented in the Basket

... to be able to see the price per person where it is applicable.
1.  Price per person displayed only where number # of guests has been captured

... to be able to make online purchases of products and services.
1.  Full (test) payment service available

... to be able to arrange delivery to a location in the UK of my choosing.
1.  Delivery details captured

... to be able to create a user page, where my personal information and order history is stored.
1.  Personal user page available
2.  Previous orders can be viewed

... the site to be secure and my personal and payment information kept safe.
1.  Secure user info
2.  Secure payment info

... to be able to maintain a list of products.
1.  Ability to administer products
2.  Update or delete products
3.  Add products
	
... to be able to track orders.
1.  Track orders in Admin view

... to be able to track payments and webhooks.
1.  Track payments through Stripe
2.  Create Webhook orders that can be identified if used disconnects mid process
3.  Track Webhooks through Stripe

### Features Left to Implement

None

## Technologies Used

1.  [html](https://en.wikipedia.org/wiki/HTML) - to create the structure and text of each page.
2.  [css](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - to style each page centrally and individually.
3.  [javascript](https://en.wikipedia.org/wiki/JavaScript) - was used to power the Bootstrap functionality.
4.  [jquery](https://jquery.com/) - was used to power the Bootstrap functionality.
5.  [Python](https://www.python.org/) - for interactions between the app, the MongoDB database and the Azure cloud storage.
6.  [Bootstrap](https://getbootstrap.com/) plugins - Responsive grid and prebuilt components to enable more responsive design; particularly “accordion” and “toggle” collapsed (hidden) content.
7.  [Font Awesome](https://fontawesome.com/v4.7.0/icons/) - for icons.
8.  [Figma](http://www.figma.com) - to produce the mockups.
9.  [w3 validator](https://validator.w3.org/) - for html validation.
10. [pep8online](http://pep8online.com/) - for Python validation.
11. [Heroku](https://www.heroku.com/) - for the back end database.
12. [Amazon Web Services](https://aws.amazon.com/) - for cloud storage to host the uploaded images.
13. [Django](https://www.djangoproject.com/) - to provide a web framework.

## Testing

User Story id 1

```js
    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
```
to...
```js
    var navBarEl = document.getElementById('mainNav');
    if (navBarEl !== null) {
        // Collapse Navbar
        var navbarCollapse = function () {
            if ($("#mainNav").offset().top > 100) {
                $("#mainNav").addClass("navbar-shrink");
            } else {
                $("#mainNav").removeClass("navbar-shrink");
            }
        };
        // Collapse now if page is not at top
        navbarCollapse();
        // Collapse the navbar when page is scrolled
        $(window).scroll(navbarCollapse);
    }
```

### Challenges

There were a few issues that needed research before I could solve them:

1. I discovered that using the accordion method of revealing hidden content on methods.html was not a great user experience, as the revealed content was off the bottom of the viewable screen. I believe the user would be unaware of this and feel that the link was broken. I initially tried adding a second set of code to allow the revealed content to appear *above* the banners, but this created duplicate ‘id’s in the code.
    After discussion with my mentor, I decided to use the carousel method (which I had seen on the Amazon site and liked). This works much better and the user experience is much cleaner. It also inspired me to add some images to help describe the content to the user.

2. The height of the iPhone X screen was a challenge as on designing index.html, there was a lot of blank space below the footer.
    There was a similar issue on the iPad Pro. Yet, the view fitted more regular phone sizes perfectly. I decided to style and size
    the app for the iPhone X first, and allow content to scroll off the bottom of the screen for smaller phones. I looked at other sites and this seems to be the norm for users to scroll down for more content.
    A trick that I used to help with this was to set a minimum vh for the background image and text section. this kept things spaced out nicely, and responded to different screen heights.

3. When I created the large, orange "banners" that link to further content on services.html and methods.html, I wanted the text centred both horizontally and vertically.
    Researching found that it has often been an ongoing issue with vertical alignment. I found a little trick at [webdevblog](https://webdevblog.com/css-vertical-align) to set: **display: flex;**
    and **align-items: center;** which solved the problem for me.

### Bugs and Errors

There were many situations through the course of coding this project - mostly sizing and layout issues due to using Bootstrap plugins. These were usually padding or marging related and were overcome by using Safari Developer Tools too identify 
which part of the css styling needed to be adjusted to suit my own application.

for example 

    .col-xl-4 {
        max-width: 33.3%;
    }
    
    .col-xl-3 {
        max-width: 25%;
    }

To ensure that there was no unwanted wraparound of cards that I wished to fit the Bootstrap grid system.

I created more formal [Testing Matrices](https://github.com/StuChapman/UCD-MS-Project-Continuous-Engagement/blob/195ffade32fdce65d439bf33c1f11352de30da86/testing) 
to ensure that I could periodically test the features and rendering in a systematic way. This was fundamental as there are often small errors like types or missing margins
that aren't immediately obvious 

The first pass of ‘completion’ testing revealed some particular errors:
1.	Autofield on progress
2.  AWS images on Heroku
3.  The menu links are supposed to change to a slightly darker colour to indicate that the user is currently visiting that particular page
    - this functionality has broken and all pages were showing "home" as the active page. I realised that I had made some adjustments to the navbar in index.html, and copied the code
    into each of the other pages without adjusting the active pages.
4.  On checking the infographics; I realised that I had not creted hyperlinks to the methods.html page form the contact.html page. I added the hyperlinks.

### Solutions to User Stories

[Screenshots](https://github.com/StuChapman/UCD-MS-Project-Continuous-Engagement/blob/195ffade32fdce65d439bf33c1f11352de30da86/screenshots) that address the different User Stories.

## Deployment

I deployed to Heroku by the following steps:
1.  Create a new Heroku app.
2.  Click on "Reveal Config Vars" to add any hidden environment variables.
3.  Add the key of "SECRET_KEY" and the value of "*...App secret key...*", and click on Add, to set the secret key.
3.  Add the key of "DATABASE_URL" and the value of "*...Postgres database...*", and click on Add, to utilise Heroku's database.
4.  Add the key of "USE_AWS" and the value of "true", then click Add, to connect to Amazon web Services.
4.  Add the key of "AWS_S3_REGION_NAME" and the value of "eu-west-2", then click Add, to connect to Amazon web Services.
4.  Add the key of "AWS_ACCESS_KEY_ID" and the value of "*...AWS access key...*", then click Add, to connect to Amazon web Services.
4.  Add the key of "AWS_SECRET_ACCESS_KEY" and the value of "*...AWS secret key...*", then click Add, to connect to Amazon web Services.
5.  Add the key of "STRIPE_PUBLIC_KEY" and the value of "*...Stripe public key...*", then click Add, to access Stripe secure payments.
5.  Add the key of "STRIPE_SECRET_KEY" and the value of "*...Stripe secret key...*", then click Add, to access Stripe secure payments.
5.  Add the key of "STRIPE_WH_SECRET" and the value of "*...Stripe webhook key...*", then click Add, to access Stripe Webhooks.
6.  Add the key of "EMAIL_HOST_USER" and the value of "noreplybuildabuffet@gmail.com", then click Add, to create an email client.
6.  Add the key of "EMAIL_HOST_PASSWORD" and the value of "*...email password...*", then click Add, to create an email client.
8.  Set the app to automatically deploy from GitHub by selecting GitHub on the Deploy tab.
9.  Enter the repository name (FS-MS-Project-Build-a-Buffet ) and click Search.
10. Click Connect next to the repository name.

To push to Heroku from GitPod (from the command line...)
1.  pip3 freeze --local > requirements.txt to create a requirements file.
2.  echo web: python run.py > Procfile to create a Procfile.
3.  npm install -g heroku
4.  heroku login -i (enter Heroku credentials)
5.  git remote add heroku https://git.heroku.com/build-a-buffet.git
6.  heroku ps:scale web=1
7.  git push -u heroku master

#### To run the code locally;

1.  From the FS-MS-Project-Build-a-Buffet repository in Github, click ‘Clone or download’.
2.  Copy the URL to your clipboard.
3.  In Gitpod, open the terminal.
4.  Change the directory to that where you wish to place the files.
5.  Type ‘git clone’ then paste the URL.

#### To run the code in Gitpod;

1. Type into the command line:
    *  pip3 install Django
    *  pip3 install django-allauth
    *  pip3 install pillow
    *  pip3 install django-crispy-forms
    *  pip3 install django-countries
    *  pip3 install dj-database-url
    *  pip install psycopg2-binary
    *  pip install psycopg2
    *  pip install gunicorn
    *  pip3 install boto3
    *  pip3 install django-storages
    *  pip3 install stripe
    *  python3 manage.py runserver

## Credits

### Content

1.	The formula (calc(10px + (48 - 10) * ((100vw - 300px) / (1800 - 300)))) for responsive font sizing is 
    from [css-tricks](https://www.css-tricks.com/books/fundamental-css-tactics/scale-typography-screen-size/) and 
    [made by Mike](www.madebymike.com.au/writing/fluid-type-calc-examples/)
2.	The method for aligning text vertically is from [webdevblog](www.webdevblog.com/css-vertical-align/) 
3.  The method to adjust styling based on landscape or portrait orientation is from [stackoverflow](https://stackoverflow.com/questions/43589507/how-can-you-have-bootstrap-responsiveness-based-on-screen-ratio-instead-of-scree)
4.  The slider is from [w3schools](https://www.w3schools.com/howto/howto_js_rangeslider.asp)
5.  Creating a cookie in javascript is from [w3schools](https://www.w3schools.com/js/js_cookies.asp)
6.  Passing context from Django to Javascript is from [stackoverflow](https://stackoverflow.com/questions/8683922/how-can-i-pass-my-context-variables-to-a-javascript-file-in-django)
7.  Inserting a row into a database with Django is from [stackoverflow](https://stackoverflow.com/questions/23868958/django-insert-row-into-database)
8.  ObjectDoesNotExist: is from [stackoverflow](https://stackoverflow.com/questions/12572741/get-single-record-from-database-django)
9.  Get a single objects value is from [http://morozov.ca](http://morozov.ca/tip-how-to-get-a-single-objects-value-with-django-orm.html)
10. Using aggregate and dict is from [stackoverflow.com](https://stackoverflow.com/questions/42132091/using-aggregation-api-django)
11. Django model.AutoField is from [www.fullstackpython.com](https://www.fullstackpython.com/django-db-models-autofield-examples.html)
12. Order by ascending and descending is from [stackoverflow.com](https://stackoverflow.com/questions/8786175/django-order-by-on-queryset-objects) and [stackoverflow.com](https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending)
13. Limit number to 2 decimals is from [tutorialdeep.com](https://tutorialdeep.com/knowhow/limit-float-to-two-decimal-places-python/)
14. Getting the current user is from [stackoverflow.com](https://stackoverflow.com/questions/12615154/how-to-get-the-currently-logged-in-users-user-id-in-django)
15. Using an hr to mimic a br is from [stackoverflow.com](https://stackoverflow.com/questions/1409649/how-to-change-the-height-of-a-br)
16. Formatting date is from [ourcodeworld.com](https://ourcodeworld.com/articles/read/555/how-to-format-datetime-objects-in-the-view-and-template-in-django)
17. Getting the first row from a queryset is from [stackoverflow.com](https://stackoverflow.com/questions/5123839/fastest-way-to-get-the-first-object-from-a-queryset-in-django)
18. Combining two or more querysets is from [stackoverflow.com](https://stackoverflow.com/questions/431628/how-to-combine-two-or-more-querysets-in-a-django-view)
19. Getting the image from the Django form is from [stackoverflow.com](https://stackoverflow.com/questions/2236691/how-do-i-display-the-value-of-a-django-form-field-in-a-template)
20. Making a form field readonly is from [stackoverflow.com](https://stackoverflow.com/questions/41271979/read-only-field-in-django-form)
21. Get the last n chacters of a string is from [c-sharpcorner.com](https://www.c-sharpcorner.com/article/how-to-get-the-last-n-characters-of-a-string-in-python/)
22. Converting to string in templete is from [stackoverflow.com](https://stackoverflow.com/questions/27771000/django-template-convert-to-string)
23. Adding linebreaks to messages is from [stackoverflow.com](https://stackoverflow.com/questions/53151314/add-new-line-to-admin-action-message)
24. Sending html email is from [stackoverflow.com](https://stackoverflow.com/questions/2809547/creating-email-templates-with-django)
25. Making a div appear for 2 seconds is from [stackoverflow.com](https://stackoverflow.com/questions/3428766/jquery-show-for-5-seconds-then-hide)
26. Form validation is from [javascripttutorial.net](https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/)
27. Fixing the uncaught error in the navbar is from [stackoverflow.com](https://stackoverflow.com/questions/20175094/uncaught-typeerror-cannot-read-property-top-of-undefined)
28. Getting a random sample from the dataset is from [stackoverflow.com](https://stackoverflow.com/questions/32389519/django-get-10-random-instances-from-a-queryset-and-order-them-into-a-new-querys)
29. Formatting to 2 decimal points is from [stackoverflow.com](https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places)


#### Code Institute

The code for:
1.  checkout: admin.py, forms.py, models.py, views.py, checkout.css and stripe_elements.js
2.  profiles: forms.py, models.py and views.py
are all built upon code from the [Code Institute](https://codeinstitute.net/) tutorial project 'boutique-ado'

### Media

1.	All images were taken from [pexels.com](www.pexels.com)
2.  The image for Bartholemew was purchased on licence from [gettyimages](https://www.gettyimages.co.uk/)
2.  The allergy graphics were purchased on licence from [gettyimages](https://www.gettyimages.co.uk/)

### Acknowledgements

I would like to thank the following people for thier support and input:

1. My mentor, [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for his knowledge and clear direction (it was he who made it very clear that a detailed set of mockups were vital - this is knowledge I will keep with me for the rest of my career!)
2. My friends [Scott](https://www.facebook.com/scott.mckellar.399) and [Magoo](https://www.facebook.com/carlos.fandango.56232), who I consulted before I started the FSD course, and gave me the confidence to go for it!
3. Annie for being the most supportive person ever!