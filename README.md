# har-utils
Utilities for reading and comparing har files.

# generate-checksums-for-diff.py
Generates output in this format:
[url with scheme host and port removed] [tab] [md5 hash of http response body]

For example:
/foo.html	a4e04598ef3db4cacc029d6b4340e479

Note: It also includes a regular expression replacement on the URL that removes querystring params like _ck=1553892021 or _=1553892021.  Querystring parameters like these are used by AEM as "cache killers" to avoid browser caching.  This makes diff'ing the file against ones captured from other AEM instances easier to do.

Example usage:
python generate-checksums-for-diff.py path/to/harfile1.har | sort > harfile1_sorted.txt
python generate-checksums-for-diff.py path/to/harfile2.har | sort > harfile2_sorted.txt
diff harfile1_sorted.txt harfile2_sorted.txt
