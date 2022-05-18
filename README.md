# THE PIPELINE Overview
![alt text](https://www.pinpng.com/pngs/m/79-791112_8-bit-mario-8-bit-mario-transparent-hd.png)

The Pipeline is a Reddit Clone, a user-rated post threading social platform dedicated to user content, users will be able to upload content, create posts, comment on other posts, and like/dislike posts.  User's posts will be public and can aquire likes/dislikes from fellow users or if within a private group channel, posts will only be shown to other users within the private channel.  

# You Will be able to:

    Create your own Posts on your preferred group channels.
    Upload Images
    See your own posts on your profile.
    Browse other user's profiles/posts/comments.
    Save posts you're interested in.
    Like/Dislike Posts.
    Browse anonymously or logged in
    Personal homescreen that shows preferred posts sorting


    The app will display the highest rated posts by default, or if logged in, you can also display your favorite posts on your homepage.  

# Other features include

    Secure salted and hashed login
    Data Storage

# Data Model

    The Pipeline uses four models:
        The Admin model, which will manage:
            usernames;
            emails;
            passwords;
            and admininstrative statuses;

        The Groups model, which will manage:
            Post group affiliation;
            Authority within group;

        The User Profile, which manages:
            Avatar;
            Friends Panel;
            Comments;
            Private Messages;

        The Post Model, which manages:
            Titles;
            Text;
            Likes, Dislikes;
            Date Published;
            Comments;
            and User Images;

        and The Friend Request Model, which manages;
            Sending/Receiving friend requests;
            accepts/declines;



# Required Packages:
    Django 4.0
    Python 3.1.0
    Pillow

# Data we will need to capture.

    User login credentials needed for:

        Creating post threads;
        Commenting;
        Liking, Disliking;
        Having a home page which holds displays posts from user's favorite groups.

    User preferences.
    
# API Data -

    Third-party API to route file uploads through a malware/malicious content detector before uploading to django database.

    Image-Resizing API

    NASA - Astronomy Picture of the Day will be utilized with JavaScript to create automatically generated posts every day with image and description.  


# Schedule
# Week 1:
    Initial Setup:
        -Data Flow Chart
        -Barebones Django, HTML, CSS, JavaScript
        -Create area for user sign up
        -Create input area for user post creation
        -Create views, forms, urls, models
        -Build mutiple user functionality with django.


# Week 2:

        -Build user customization/setting profile.
        -Integrate an API
        -Allow ability to view other profiles, ie. public posts/comments/avatars/usernames
        -Style pages so they are not so clunky
        -Responsive design for mobile application
        -Build Groups/Post relation

# Week 3:

        -Heroku hosting and deployment.
        -Finishing touches ie. styling
    



# Minimum completion:
        -Fully functional website
            * User login
            * User website styling vs Anonymous website styling
            * User post creation
            * User commenting, liking/disliking
            * Post sorting by user preferred method
        -Multiple user functionality 
        -Desktop interface (no mobile)
        -Minimal styling
        -API integration


# Essential features

    -User login
    -User input
    -Personal homepage
    -User Avatars
    -User post/commenting/liking/disliking
    -User image upload ability

# Really-great-to-haves

    -User group associations
    -Fully customizable user homescreen to show preferred group posts
    -Deployment on Heroku

# Really-great-to-haves

    -Fully styled site functioning on both mobile and desktop
    -Private user messaging
    -Admin moderation


