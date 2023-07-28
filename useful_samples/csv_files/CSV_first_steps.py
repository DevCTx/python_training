import csv

###### READER ######

with open('contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')     # delimiter allows to define the character (coma per default)
    for row in reader :
        print(row)
    print()

with open('contacts.csv', newline='') as csvfile:   # newline to avoid errors on different platforms
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader :
        print(','.join(row))
    print()

with open('contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)                # DictReader associates keys with the identifiers of the first line
    for row in reader :
        print(row['Name'], ':', row['Phone'])
    print()

with open('contacts.csv', newline='') as csvfile:
    fieldnames = ['Name','Phone','Address']                     # If there is no header, define it before
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)     # if more keys than the file, values = None
    for row in reader :
        print(row['Name'], ':', row['Phone'], ':', row['Address'])
    print()


###### WRITER ######

with open('exported_contacts.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=',')                  # Write with a coma as separator
    writer.writerow(['Name','Phone'])
    writer.writerow(['mamie','555-888-001'])
    writer.writerow(['papy','555-888-002'])

with open('exported_contacts.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Name','Phone'])
    writer.writerow(['mamie','555-888-001'])
    writer.writerow(['papy','555-888-002'])
    writer.writerow(["pepe, meme, and the cat",'555-888-003'])  # Allows to write the coma separator character

with open('exported_contacts.csv','w',newline='') as csvfile:
    fieldnames = ['Name', 'Phone', 'Address']                   # Define a header in the CSV file
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name':'mamie','Phone':'555-888-001'})
    writer.writerow({'Name':'papy','Phone':'555-888-002'})
    writer.writerow({'Name':'Voisin','Phone':'555-888-006','Address':'near by'})
    writer.writerow({'Name':"pepe, meme, and the cat",'Phone':'555-888-003'})   # Accepts the coma separator as well
