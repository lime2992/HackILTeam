# Newsflow
#### Video Demo:  <https://youtu.be/XXXXXX>
#### Inspiration:
It is inconvenient that people will encounter problems when searching for news but there are various useless contents shown on their website. For example, when we use CNN to search for some topics about Ukraine, we have to go to the search page, and then it will display lots of news for us. However, we just want five to ten trending news so that we can immediately know about what's happening about that topic right now. The other thing is that we want to combat fake news and disinformation by using this app to expose people to various viewpoints.

#### What it does
This application will display the trending news and a search bar for users to type any words related to their desired news or articles and countries.

#### How we built it
We created a web application by using Dash which is a Python framework for building reactive web apps, and then we used newsapi to return JSON search results for current news and top headlines. After data preprocessing, we displayed the contents based on the keywords and the condition that users gave.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some modules.

```bash
pip install flask
pip install newsapi-python
```

## Preparation

Import newsapi, flask.

```python
from flask import Flask, render_template, redirect, flash, jsonify, session, request
from newsapi import NewsApiClient
```

## Execution

Run the application with:
```
(venv) $ python -m flask run
```

Then you can open http://localhost:5000 to check the program.

Now we are ready to go!

## Possible improvements

XXXXX
