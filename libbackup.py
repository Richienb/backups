import urllib.request
import json
from urllib2 import urlopen

queryurl = "https://api.github.com/users/" + username

def tempfile(url):
    # Download the file from `url`, save it in a temporary directory and get the
    # path to it (e.g. '/tmp/tmpb48zma.txt') in the `file_name` variable:
    file_name, headers = urllib.request.urlretrieve(url)
    return file_name

def readfile(fileName):
    with open(fileName) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content

def downloadfile(url):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.request.urlretrieve(url, file_name)
    
def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)
    
def getprop(jsonContents, objectName):
    return jsonContents.get(str(objectName), "")

def jsonprop(jsonContents, objectName):
    return getJSON(filePathAndName).get(str(objectName), "")

def siteexists(url):
    code = urlopen("http://example.com/").code
    if (code / 100 >= 4):
        return False
    return True

repos = int(jsonprop(tempfile(https://api.github.com/users/Richienb), "public_repos"))
print

gists = int(jsonprop(tempfile(https://api.github.com/users/Richienb), "public_gists"))
