def getDatabase():
    import csv
    try:
        f =open('Holdings.csv',newline='')
    except:
        return 'File not found'
    reader = csv.reader(f)
    database = list(reader)
    return database


def updateDatabase(stock,volume,price,action):
    from tempfile import NamedTemporaryFile
    import shutil
    import csv

    filename = 'Holdings.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    fields = ['ID',
            'Stocks',
            'Volume',
            'Price']

    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        count = 0
        for row in reader:
            count+=1
            if row['Stocks']==stock:
#Updating values
                print('updating row:', row['Stocks'])
                row['Stocks'], row['Volume'], row['Price']= \
                    stock,volume,price
                print(row)
            row = {'ID': row['ID'],\
                'Stocks': row['Stocks'],\
                'Volume': row['Volume'],\
                'Price': row['Price']}
            writer.writerow(row)
#Create a new row if the listing does not exist
        if action=='New':
            print('Creating row:', stock)
            row = {'ID': count+1,\
                'Stocks': stock,\
                'Volume': volume,\
                'Price': price,}
            print(row)
            writer.writerow(row)
    shutil.move(tempfile.name, filename)
