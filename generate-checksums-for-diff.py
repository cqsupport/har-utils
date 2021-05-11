#!/usr/bin/python

import sys  
import json
import re
import md5
import difflib

reload(sys)  
sys.setdefaultencoding('utf8')

if len(sys.argv) < 2 :
    print ""
    print "Specify the path of the har file you want to read as a parameter"
    print "e.g. script.py path/to/harfile.har"
    print ""
    exit(1)


with open(sys.argv[1]) as fh:
    a = json.load(fh)
    # loop through all requests in the har
    for entry in a['log']['entries']:
        try:
            # remove common cache bypassing querystring parameters
            url = re.sub(r"(ch)?_(ck|ch)?=[0-9]+&?", r"", entry['request']['url'])
            # remove any trailing questionmark where there is no querystring left
            url = re.sub(r"\?$", r"", url)
            # remove the scheme and host part of the URL leaving the URI path (e.g. remove https://site.com)
            url = re.sub(r"^.*://.*?\/", r"/", url)
        except:
            pass
        if 'text' in entry['response']['content']:
            # take an md5 hash of the response body
            m = md5.new()
            m.update(entry['response']['content']['text'])
            thehash = m.hexdigest()
            # output: url{tab}md5hash
            print "%s\t%s" % (url, thehash)
