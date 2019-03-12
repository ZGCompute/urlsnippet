
UrlSnippet
===========

This repository contains a REST service for requesting text snippets from a given url. The primary GET method requires the user to input two parameters, url and max_age. The first time the service is called with a given URL, it will fetch the supplied URL and extract the text. But if it is called on a URL that has been used before and the last cached page is less than max_age seconds old, it will return the cached copy.

URL snippets are persisted via the python requests_cache and sqlite backend, so if your service restarts, you don’t have to fetch everything again.


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

Notes on Development, Deployment, Testing, and Scalability
===============

- This package was developed using Python flask/requests for its simple REST functionality and quick time to implement.

- flask is great for quickstart dev/test, but not so ideal in terms of scalability. To address this shortcoming, the 'threaded' or' proceesses' arg can be set in the call to app.run():

  if __name__ == '__main__':
     app.run(threaded=True)
     # Or
     # app.run(processes=3)

- Still, this will not be ideal for handling many asynchronous clinet requests on a production server, as python's GIL limits the effectiveness of multi-threading. 

- For scalable deployment, AWS elestic beanstalk and/or Gunicorn/nginx can be utilized for spawning asynchronous workers to speed up the app.

- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
- https://gunicorn.org/
- http://nginx.org/en/
  
Recommendations
===============


Python 2 or 3?
--------------

- Code developed under Python 3, tested for both Python 2 and Python 3
  but consider Python 3 to be the default




