# THE PIPELINE Overview
<p align="center">
<img src="https://c.tenor.com/YaTahtedGloAAAAC/mario-pipe.gif">
</p>


__________________
#### The Pipeline is a Reddit Clone, a user-rated post threading social platform dedicated to user content, users will be able to upload content, create posts, comment on other posts, and like/dislike posts.  User's posts will be public and can aquire likes/dislikes from fellow users or if within a private group channel, posts will only be shown to other users within the private channel.  
_____________________

 ### You Will be able to:

 * Create your own Posts on your preferred group channels. 
 * Upload Images 
 * See your own posts on your profile. 
 * Browse other user's profiles/posts/comments. 
 * Save posts you're interested in. 
 * Like/Dislike Posts. 
 * Browse anonymously or logged in 
 * Personal homescreen that shows preferred posts sorting 
_____

* #### The app will display the highest rated posts by default
* #### You can also display your favorite posts on your homepage.  
_________
# Other features include

* Secure salted and hashed login
* Data Storage

# Data Model
<p align="center">
<img src="static/images/Datastructure.png">
</p>

    
## The Pipeline uses five models: 

|Users|Custom User Profiles|Groups|Posts|Friend Requests|
| ------- | -- | -- | -- |--|
|Usernames|Avatar|Post group affiliation|Titles|Sending/Receiving|
|Emails|Friends Panel|Authority within group|Text|Accepts/Declines|
|Passwords|Comments||Likes, Dislikes|
|Active Status|Private Messages||Date Published|
|Admininstrative statuses|||Comments|
||||User Images|




# Required Packages:

* django
* pillow
* django-environ
* django-heroku
* django-rest-framework
* djangorestframework
* filelock
* gunicorn
* idna
* itsdangerous
* javascript
* jinja2
* pathspec
* python-dotenv
* platformdirs
* psycopg2
* asgiref
* beautifulsoup4
* black
* certifi
* charset-normalizer
* click
* colorama
* dj-database-url
* django-admin-honeypot
* pytz
* requests
* setuptools
* soupsieve
* sqlparse
* tomli
* tzdata
* urllib3
* werkzeug
* whitenoise
* django-el-pagination
* django-treebeard
* python


# Data we will need to capture.

* User Information
* User Post Creation
* Uploaded Files
* Thread comments
* Likes/Dislikes
* User Preferences

# API Data -

* Django-Treebeard 

Django-treebeard is a library that implements efficient tree implementations for the Django Web Framework 1.8+, written by Gustavo Picón and licensed under the Apache License 2.0.

django-treebeard is:

    Flexible: Includes 3 different tree implementations with the same API:
        Adjacency List
        Materialized Path
        Nested Sets
    Fast: Optimized non-naive tree operations
    Easy: Uses Django’s Model inheritance with Abstract base classes. to define your own models.
    Clean: Testable and well tested code base. Code/branch test coverage is above 96%.

This app will be integrating a Materialized Path Tree within its SQL database to create a threadable comment system that is navigated from root to node using an encoded numbering system that assigns a depth and numchild to each comment.   



# Schedule:
### Week 1:
#### Initial Setup:
* Data Flow Chart
* Barebones Django, HTML, CSS, JavaScript
* Create area for user sign up
* Create input area for user post creation
* Create views, forms, urls, models
* Build mutiple user functionality with django.


### Week 2:

* Build user customization/setting profile.
* Integrate treebeard API
* Allow ability to view other profiles, ie. public posts/comments/avatars/usernames
* Style pages so they are not so clunky
* Responsive design for mobile application
* Build Groups/Post relation

### Week 3:

* Heroku hosting and deployment.
* Finishing touches ie. styling
* Responsive design
* AJAX Implemation




# Minimum completion:
  * Fully functional website
      * User login
      * User website styling vs Anonymous website styling
      * User post creation
      * User commenting, liking/disliking
      * Post sorting by user preferred method
  * Multiple user functionality 
  * Desktop interface (no mobile)
  * Minimal styling
  * API integration


# Essential features

* User login
* User input
* Personal homepage
* User Avatars
* User post/commenting/liking/disliking
* User image upload ability

# Really-great-to-haves

* User group associations
* Fully customizable user homescreen to show preferred group posts
* Deployment on Heroku

# Really-great-to-haves

* Fully styled site functioning on both mobile and desktop
* Private user messaging
* Admin Group moderation


