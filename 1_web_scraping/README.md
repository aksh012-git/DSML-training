Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works
with your favourite parser to provide idiomatic ways of navigating, searching, and modifying
the parse tree.


Beautiful Soup is a Python library for getting data out of HTML, XML, and other markup
languages. Say you’ve found some webpages that display data relevant to your research, such
as date or address information, but that do not provide any way of downloading the data
directly. Beautiful Soup helps you pull particular content from a webpage, remove the HTML
markup, and save the information. It is a tool for web scraping that helps you clean up and
parse the documents you have pulled down from the web.


-Install beautifulsoup version 4

-conda install beautifulsoup4


Once this beautifulsoup gets installed, the next need is to have parser to parse the HTML
content. You will need to install a “parser” for interpreting the HTML. There are different
parsers and that may provide you a different results depending on the HTML page you are
trying to parse.


There is small differences between parsers and they can return different results depending
upon their capabilities. If HTML page is going to be well organized, then these differences
are not going to matter. But HTML with not proper structure, it creates a difference, as they
have different approaches to fill up the missing information.

So, after going through list of parsers, suggestion is to go with lxml parser.

-pip install lxml

You can also install html5lib parser

-pip install html5lib


To fetch the data from html web page, we also require requests library

-pip install requests

Now, before we scrap any data from any website, let me just create one dunny HTML web
page and let’s experiment on it.

Afterwards, check python script