# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
# using regular expressions
import re
# The ssl library allows this program to access web sites that strictly enforce HTTPS
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# The read method returns HTML source code as a bytes object instead of returning an HTTPResponse object
html = urllib.request.urlopen(url, context=ctx).read()
# The findall regular expression method will give us a list of all of the strings that match our regular expression, returning only the link text between the double quotes
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())
