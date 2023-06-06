import xml.etree.ElementTree as ET

#### READING ####

tree = ET.parse('books.xml')
root = tree.getroot()

print("\nDisplay by attribute or by reference on a data")
for book in root:
    print('>','Title: ', book.attrib['title'])
    print('>','Author:', book[0].text)
    print('>','Year: ', book[1].text, '\n')

print("\nDisplay by reference on a child element")
print("print(root[0][0].text)")
print('>',root[0][0].text)

print("\nDisplay the text of the iteration on a named element (at all levels)")
print("author.text in root.iter('author')")
print(root.iter('author'))
for author in root.iter('author'):
    print('>',author.text)

print("\nDisplay the text of the iteration on a named element but only (on first level only)")
print("author.text in root.findall('author')")
print(root.findall('author'))
for author in root.findall('author'):
    print('>',author.text)
print("Returns nothing because author is under root and book : root>book>author")

print("\nTry again with another named element (on first level only)")
print("book.get('title') in root.findall('book')")
print(root.findall('book'))
for book in root.findall('book'):
    print('>',book.get('title'))

print("\nOr again with a path to the named element")
print("author.text in root.findall('book/author')")
print(root.findall('book/author'))
for author in root.findall('book/author'):
    print('>',author.text)

print("\nOr even with last() ... [but first() does not exist]")
print("root.findall('book[last()]/author')")
print(root.findall('book[last()]/author'))
for author in root.findall('book[last()]/author'):
    print('>',author.text)

print("\nFinaly, with find, we can get the first element only")
print("root.find('book').get('title')")
print('>',root.find('book').get('title'))


#### WRITING ####

def prettify(elem, level=0):
    """Recursively adds indentation and line breaks to the XML element and its children."""
    indent = "  " * level

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = "\n" + indent + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = "\n" + indent

        for child in elem:
            prettify(child, level + 1)

        if not child.tail or not child.tail.strip():
            child.tail = "\n" + indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = "\n" + indent


# This creates a book with a title as attribute and 2 elements author and year as text
def add_book(root, title, author, year) :
    """Adds book to the root structure from books.xml"""
    book = ET.SubElement(root, "book", {'title': title})    # Automatically add book to root

    book_author = ET.SubElement(book, "author")             # Automatically add author to book
    book_author.text = author

    book_year = ET.SubElement(book, "year")                 # Automatically add year to book
    book_year.text = str(year)


# Name the root Element
root = ET.Element("data")                                   # Automatically add data to root

# Add SubElement books to data
add_book(root, "My New Book", "A great Author", 2023)
add_book(root, "Another Book", "Same Author", 2022)

# Prettify the XML
prettify(root)

# ElementTree must be declared when the Elements and SubElements are ready to be written
tree = ET.ElementTree(root)                                 # Automatically add root to the XML file
tree.write("books2.xml", encoding="utf-8", xml_declaration=True)    # to add <?xml version='1.0' encoding='UTF-8'?>


#### MAY ALSO USE XML.DOM.MINIDOM ####


import xml.dom.minidom as minidom

# Create the XML document
doc = minidom.Document()

# Create the root element
root = doc.createElement("data")
doc.appendChild(root)

# Function to add a book to the XML document
def add_book(title, author, year):
    book = doc.createElement("book")
    book.setAttribute("title", title)

    author_elem = doc.createElement("author")
    author_elem.appendChild(doc.createTextNode(author))
    book.appendChild(author_elem)

    year_elem = doc.createElement("year")
    year_elem.appendChild(doc.createTextNode(str(year)))
    book.appendChild(year_elem)

    root.appendChild(book)

# Add books to the XML document
add_book("My New Book", "A great Author", 2023)
add_book("Another Book", "Same Author", 2022)

# Write the XML document to a file with proper indentation
xml_str = doc.toprettyxml(indent="  ")
with open("books3.xml", "w") as f:
    f.write(xml_str)
