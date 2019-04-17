## news-Highlights.
### By Henry Halkano

### Application Release Date:
      05/02/2019.

### Description:
News Highlights is a web application that displays a list of various news sources like BBC and CNN. On choosing a news source, it will preview the top news articles of the day. Clicking a news article will redirect the user to read it fully from the news source. It achieves this by using the News API.

You can view the site at:Heroku

### BDD:
#### This app is therefore expected to work as following:
| Behavior | Expectation|
|----------|:-------------:|
|on clicking ARTICLE tab |displays an entire article or 	Redirected to the news source's site|
|On clicking the News-highlights tab |the page load	List of various news sources is displayed in a list |



### Setup /Installation requirements:
Prerequisites
python3.6
pip
virtualenv
Cloning
In your terminal:

  $ git clone https://github.com/halkano/news-highlights/
  $ cd News-Highlights
Running the Application
Creating the virtual environment

  $ python3.6 -m venv --without-pip virtual
  $ source virtual/bin/env
  $ curl https://bootstrap.pypa.io/get-pip.py | python
Installing Flask and other Modules

  $ python3.6 -m pip install Flask
  $ python3.6 -m pip install Flask-Bootstrap
  $ python3.6 -m pip install Flask-Script
Setting up the API Key

  To be able to gather article info from the News API you will need an API Key.

  * Visit https://newsapi.org/ and register for an API key.
  * In the root directory of the project folder create a file: start.sh
  * Insert the following info into it:

          export NEWS_API_KEY='<Your-Api-Key>'
          python3.6 manage.py server

  * Insert the API Key you received from News Api where <Your-Api-Key> is.
To run the application, in your terminal:

  $ chmod +x start.sh
  $ ./start.sh
Testing the Application
To run the tests for the class files:

  $ python3.6 manage.py tests
Technologies Used
Python3.6
Flask
License
Copyright (c) 2018 Halkano

### LICENCE:
This Application is license under the MIT licence.
Get more info on my github account

Copyright © 2018;Henry Halkano.Inc.


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
