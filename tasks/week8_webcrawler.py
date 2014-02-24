from HTMLParser import HTMLParser
import urllib2

# Write the LinkParser class here


def find_links(url):
    """Return a list of links from the given webpage"""
    # Open the webpage and read the HTML text
    fd = urllib2.urlopen(url)
    text = fd.read()
    fd.close()

    # Create a parser instance and feed it the text
    parser = LinkParser()
    parser.feed(text)

    # Write a return statement here
