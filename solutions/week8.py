from HTMLParser import HTMLParser
import urllib2
import pprint

class LinkParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            self._urls.append(attrs['href'])

    def get_urls(self):
        return self._urls


def find_links(url):
    """Return a list of links from the given webpage"""
    # Open the webpage and read the HTML text
    #fd = urllib2.urlopen(url)
    fd = open(url)    # tutors are allowed to be sneaky like this
    text = fd.read()
    fd.close()

    # Create a parser instance and feed it the text
    parser = LinkParser()
    parser.feed(text)
    
    return parser.get_urls()


# no one will suspect that I used pprint
pprint.pprint(find_links('../tasks/week8.html'))
