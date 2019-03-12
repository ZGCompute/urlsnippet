
UrlSnippet
===========

This repository contains a REST service for requesting text snippets from a given url. The primary GET method requires the user to input two parameters, url and max_age. The first time the service is called with a given URL, it will fetch the supplied URL and extract the text. But if it is called on a URL that has been used before and the last cached page is less than max_age seconds old, it will return the cached copy. URL snippets are persisted via the python requests_cache and sqlite backend, so if your service restarts, you don’t have to fetch everything again.


Specification
===============

- https://docs.google.com/document/d/1h0FbJe954OaGbI54G-Lmd2e1zvs8pafucz09FHxp1to/edit?ts=5c7daadd

  
Dependencies
===============

- reuests
- requests_cache
- flask
- BeautifullSoup
- sqlalchemy
- webargs


Recommendations
===============


Python 2 or 3?
--------------

- Develop your code under Python 3, test it for both Python 2 and Python 3
  but consider Python 3 to be the default




