# File processing

from sys        import argv, stdin
from os.path    import exists,join
from os         import environ,system
from util.tabs  import print_tab_doc, print_all_tabs
from util.wiki  import convert_html
from util.files import read_file, write_file


# Create html file contents from stdin
def page_html():
    text = stdin.read().split('\n')
    return convert_html(text)


# Create html file contents from stdin
def print_page_html():
    text = stdin.read() 
    print_all_tabs(text)


# Show the formatted document for the file
def doc_show(doc):

    path = join(environ['pd'],doc)

    if not exists(path):
        index = join(path,'Index')
        if exists(index):
            print "redirect:%s/Index" % doc
        else:
            print "redirect:%s/missing" % doc
    else:
        print convert_html(read_file(path))


# Show the user doc
def user_doc_show(user,doc):
    path = join(environ['pd'],user,doc)

    if not exists(path):
        index = join(path,'Index')
        if exists(index):
            print "redirect:%s/Index" % doc
        else:
            print "redirect:%s/missing" % doc
    else:
        print convert_html(read_file(path))


# Put the document text in storage
def doc_put(doc):
    write_file(doc, read_input())


# Get the document text from storage
def doc_get(doc):
    return read_file(doc)

