# web-scrapping
web scrapping using python

### we used python and some python libraries like requests, bs4 and urllib

## Steps involved in web scraping:

1. Send a HTTP request to the URL of the webpage you want to access. The server responds to the request by returning the HTML content of the webpage. For this task, we will use a third-party HTTP library
   for python requests.
2. Once we have accessed the HTML content, we are left with the task of parsing the data. Since most of the HTML data is nested, we cannot extract data simply through string processing. One needs a
   parser which can create a nested/tree structure of the HTML data.
3. There are many HTML parser libraries available but the most advanced one is html5lib.

   Now, all we need to do is navigating and searching the parse tree that we created, i.e. tree traversal. For this task, we will be using another third-party python library, Beautiful Soup. It is a Python
   library for pulling data out of HTML and XML files.


## Step1 - installing the required third-party libraries

   ####pip install requests
   ####pip install html5lib
   ####pip install bs4

## Step 2: Accessing the HTML content from webpage

   import requests
   URL = "https://www.geeksforgeeks.org/data-structures/"
   r = requests.get(URL)
   print(r.content)


*Let us try to understand this piece of code.

*First of all import the requests library.
*Then, specify the URL of the webpage you want to scrape.
*Send a HTTP request to the specified URL and save the response from server in a response object called r.
*Now, as print r.content to get the raw HTML content of the webpage. It is of ‘string’ type.

## step3 - parsing the html content
    This will not run on online IDE
   import requests
   from bs4 import BeautifulSoup
 
   URL = "http://www.values.com/inspirational-quotes"
   r = requests.get(URL)
 
   soup = BeautifulSoup(r.content, 'html5lib')
   print(soup.prettify())




