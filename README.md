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

I designed the site around the following views:

**index.html** - to introduce the user to the company and provide navigation to the other areas of the site.

**register.html** - to register for account services.

**login.html** - to log in to the site.

**menus.html** - to list all the produce based on the user's search parameters.

**account.html** - to allow the Customer to store and update personal, shipping, order and payment information.

**basket.html** - to view all the products currently in the basket.

**checkout.html** - a secure checkout where registered and guest users can make purchases.

**customer-service.html** - contact information

### Mockups:

I produced the following mockups prior to writing any code. I found that tremendously useful as I made a lot 
    of design and functionality decisions up front. I also researched a particular Bootstrap 
    capability – [Accordion/Collapse](https://getbootstrap.com/docs/4.1/components/collapse/#accordion-example) 
    as when I was designing the methods.html layout, I felt the best method would be to hide and reveal relevant 
    content on the page (rather than navigate to separate pages)

[mobile](...)

[desktop](...)

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
for a tablet, portrait view, and finally any changes for a large size, landscape view. I did this in the mockups first, then as I built the app.
I constructed the code in the mobile-first, portrait view, then added media queries purely for large size, landscape view.
I didn't want to have a multuitude of media queries for different sizes, I preferred to have a completely responsive approach.
For that, I set font sizes to be responsive, utilising some code from [css-tricks](https://css-tricks.com/books/fundamental-css-tactics/scale-typography-screen-size/) 
and [made by Mike](https://www.madebymike.com.au/writing/fluid-type-calc-examples/)

font-size: calc([minimum size] + ([maximum size] - [minimum size]) * ((100vw - [minimum viewport width]) / ([maximum viewport width] - [minimum viewport width])));

This code, along with using vw for font sizes and certain features, such as banners and images, allowed the site to be almost fully responsive across different portrait view sizes.

## Features

### Existing Features

1.	A Navigation bar, that is standard across all pages. It is made up of 3 sections:
    
    a.	A collapsed “burger” style menu that allows the user to access every page on the site from the top left corner of any page, in all media device sizes.
    
    b.	A “brand image” that allows the user to hyperlink to the home page from an page, in all media device sizes.
    
    c.	A menu that allows the user to navigate to any page from any page and also see which page they are currently on by means of differentiated font color. The menu shrinks to icons only on smaller media devices in landscape orientation and the “contact us” icon only in portrait orientation.

2.	A background image that gives the user a feeling of ‘business’ and ‘commerce’.
3.	A large font mission statement for each page that succinctly gets across to the user what the company/page does (excluding the “contact us” page which is self-explanatory).
4.	Supporting, smaller font text to supplement the mission statement.
5.	3 infographics that repeat across the “index”, “methods (expanded)” and “contact (large size, landscape view only) that summarise the 3 main areas of expertise of the company.
6.	A footer which shows the user the regulatory information for the company.
7.	4 “photolinks” on the “index” page to allow quick navigation to services.html
8.	4 banners on the “services” page that allow the user to navigate, via a Bootstrap “accordion” example, to the 4 different services the company offers, with supporting text. These are block rows on portrait screens and inline columns for landscape.
9.	3 banners on the “methods” page that allow the user to navigate, via a Bootstrap “accordion” example on small/medium sized media devices, and a Bootstrap “carousel” for large media devices, to the 3 main areas of expertise of the company, with supporting text. These are block rows on portrait screens and inline columns for landscape.
10.	A Bootstrap “carousel” on the “services” and/or “methods” pages to present the collapsed information in an even more UX friendly way.
11.	4 Case Studies on the “case-studies” page to showcase examples of the success of the methods to the user. These are block rows in small/medium media devices, and 2 x 2 inline columns on large+ media devices.
12.	An image of the company director along with contact information (name, job title email, LinkedIn and phone) to give the user options to contact the director. Email, LinkedIn and phone hyperlink to email app, LinkedIn website and phone app respectively.

### Features Left to Implement

1.	Completing the “contact us” form functionality to enable the user to submit specific information about business need.
2.	Interactive learning that brings the methods further to life for the user (multi choice quiz etc.)
3.  The ability to link from the photolinks or infographics on index.html directly to the expanded section on the services.html and methods.html pages respectively (I believe this will utilise JavaScript).

## Technologies Used

1.	[html](https://en.wikipedia.org/wiki/HTML) - to create the structure and text of each page.
2.	[css](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - to style each page centrally and individually.
3.	[Bootstrap](https://getbootstrap.com/) plugins - Responsive grid and prebuilt components to enable more responsive design; particularly “accordion” and “toggle” collapsed (hidden) content.
4.	[Font Awesome](https://fontawesome.com/v4.7.0/icons/) - for icons on contact.html.
5.	[Google Fonts](https://fonts.google.com/?query=cairo) - for the ‘Cairo’ font – used exclusively across the site.
6.	[Figma](http://www.figma.com) - to produce the mockups.

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

I deployed to Github Pages by the following steps:
1.	From the UCD-MS-Project-Continuous-Engagement repository in Github, click ‘Settings’
2.	Scroll down to ‘GitHub Pages’
3.	From the ‘source’ drop-down, select ‘master branch’
4.	The url was then presented to me as https://stuchapman.github.io/UCD-MS-Project-Continuous-Engagement/

#### To run the code locally;
1.	From the UCD-MS-Project-Continuous-Engagement repository in Github, click ‘Clone or download’
2.	Copy the URL to your clipboard
3.	In Gitpod, open the terminal
4.	Change the directory to that where you wish to place the files
5.	Type ‘git clone’ then paste the URL

## Credits



### Content

1.	The formula (calc(10px + (48 - 10) * ((100vw - 300px) / (1800 - 300)))) for responsive font sizing is 
    from [css-tricks](https://www.css-tricks.com/books/fundamental-css-tactics/scale-typography-screen-size/) and 
    [made by Mike](www.madebymike.com.au/writing/fluid-type-calc-examples/)
2.	The method for aligning text vertically is from [webdevblog](www.webdevblog.com/css-vertical-align/) 
3.  The method to adjust styling based on landscape or portrait orientation is from [stackoverflow](https://stackoverflow.com/questions/43589507/how-can-you-have-bootstrap-responsiveness-based-on-screen-ratio-instead-of-scree)
4.  The slider is from [w3schools](https://www.w3schools.com/howto/howto_js_rangeslider.asp)
5.  Creating a cookie in javascript is from [w3schools](https://www.w3schools.com/js/js_cookies.asp)
6.  Passing context fro Django to Javascript is from [stackoverflow](https://stackoverflow.com/questions/8683922/how-can-i-pass-my-context-variables-to-a-javascript-file-in-django)
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
are all built on code from the [Code Institute](https://codeinstitute.net/) tutorial project 'boutique-ado'

### Media

1.	All images were taken from www.pexels.com 
    1. [neon-signage](https://www.pexels.com/photo/neon-signage-2681319/)
    2. [group-of-people-watching-on-laptop](https://www.pexels.com/photo/group-of-people-watching-on-laptop-1595385/)
    3. [books-business-computer-connection](https://www.pexels.com/photo/books-business-computer-connection-459654/)
    4. [working-in-a-group](https://www.pexels.com/photo/working-in-a-group-6224/)
2.	The infographics and ‘brand image’ were designed and created by me

### Acknowledgements

I would like to thank the following people for thier support and input:

1. My mentor, [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for his knowledge and clear direction (it was he who made it very clear that a detailed set of mockups were vital - this is knowledge I will keep with me for the rest of my career!)
2. My friends [Scott](https://www.facebook.com/scott.mckellar.399) and [Magoo](https://www.facebook.com/carlos.fandango.56232), who I consulted before I started the FSD course, and gave me the confidence to go for it!