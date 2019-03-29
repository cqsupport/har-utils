# har-utils
Utilities for reading and comparing har files.

# generate-checksums-for-diff.py
Generates output in this format:
[url with scheme host and port removed] [tab] [md5 hash of http response body]

For example:
/foo.html	a4e04598ef3db4cacc029d6b4340e479

Note: It also includes a regular expression replacement on the URL that removes querystring params like _ck=1553892021 or _=1553892021 which are used as "cache killers" in AEM author environments to avoid caching of certain URLs in the browser.  This makes diff'ing the file against ones captured from other AEM instances easier to do.
