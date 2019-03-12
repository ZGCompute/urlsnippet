# file: snippet.py
# Description: 
#
# This file contains the UrlSnippet class providing a restful
# API for retreiving text snippets from a user specified url.
# 
# Arguments:
# 
#     url: Command-line option to specify url
#          to retreieve a text snippet from. 
#          No default.
#
#     max_age: Command-line option to specify number
#              of seconds to hold previous request
#              result in requests cache
#              default param is 200 sec.   
# 
# Usage: curl -G "http://localhost:4444/snippet" \
#        --data-urlencode "url=https://en.wikipedia.org/wiki/Cheese" \
#        --data-urlencode "max_age=3600
#
# Author: Zack Greenberg
# Date last edited: 03/11/19

from flask import Flask, request, requests_cache
from flask_restful import Resource, Api
from flask.ext.jsonpify import jsonify
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort
from sqlalchemy import create_engine
import BeautifulSoup
import re

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)
Newlines = re.compile(r'[\r\n]\s+')

class UrlSnippet(Resource):

    """REST service for retreiving text snippet from a given URL
       with request caching to improve performance, and sqlite 
       backend for persistence.
    """
    snippet_args = {"url": fields.Str(required=True), \
                    "max_age": fields.Int(required=True, validate=validate.Range(min=1))}

    @use_kwargs(snippet_args)
    def getText(self, url, max_age):
        """REST get method for retreiving url snippet"""
        requests_cache.install_cache(cache_name='snippet_cache',\
                                     backend='sqlite', expire_after=max_age)
        response_dict = requests.get(url) 
        bs = BeautifulSoup.BeautifulSoup(response_dict.text,\
                                         convertEntities=BeautifulSoup.BeautifulSoup.HTML_ENTITIES)
        for s in bs.findAll('script'): 
            s.replaceWith('')
        txt = bs.find('body').getText('\n')
        return Newlines.sub('\n', txt.replace("\n", " ")[:1024])


# This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err, req, schema, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
       a JSON error response to the client.
    """
    abort(error_status_code, errors=err.messages)

if __name__ == '__main__':
    api.add_resource(UrlSnippet, '/urlsnippet') 
    app.run(host='0.0.0.0')
