# {{mustache}} with web.py

This is a little example application illustrating how one might use mustache templates with a web.py project

One thing to note about this example is that I used the lastest code from the master branch of the defactor pystache project. When I installed pystache using pip it seemed to be an older version.

I'd recommend using virtualenv, as the following steps will utilize it

1. Clone the repository

    git clone git@github.com:mattupstate/mustache-with-webpy.git
    
2. Setup an environment using virtual env

    cd mustache-with-webpy
    virtualenv --no-site-packages env
    source env/bin/activate
    
3. Install web.py

    pip install web.py
    
4. Run the web.py server

    python main.py

# Overview

Mustache is a logic-less templating system. This means that logic, state, behavior, etc does not reside in the template. This is often considered a good practice in web development these days.

So where does all that logic go? It goes in a view object!. The view object implements what is often called the Presentation Model pattern. This allows us to represent state and what not independently of the presentation layer.

In this example application I'm using web.py to handle HTTP requests through objects called controllers. This is a pretty common pattern amongst web frameworks. The controllers connect the data/persistance layer with the presentation layer.

If you take a look at the controllers, you'll see that they create instances of the view objects. They are then supplied with data from the application's (fake/mock) model. The view objects then have accessors for the view templates, returning the necessary data for the presentation layer.

One bit of convetion I'm using here is within the base view class. View classes are mapped to corresponding templates. Hopefully its easy enough to understand!

Enjoy.