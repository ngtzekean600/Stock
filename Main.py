def changeDeviation():
    dev = input('What is your deviation: ')
    return dev

def getDatabase():
    import csv
    try:
        f =open('Holdings.csv',newline='')
    except:
        print('File not found')
    for line in f.readlines():
        print(line)
    #reader = csv.reader(f)
    #database = list(reader)
    return ''
    

def updateDatabase(stock,volume,price,target,action):
    from tempfile import NamedTemporaryFile
    import shutil
    import csv

    filename = 'Holdings.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    fields = ['ID',
            'Stocks',
            'Volume',
            'Price bought',
            'Upper price',
            'Lower Price',
            'Target price']

    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['Stocks']==stock:
#Updating values
                print('updating row', row['Stock'])
                row['Stocks'], row['Volume'], row['Price bought'],row['Upper price'], row['Lower Price'],row['Target price']= \
                    stock,volume,price,price*(1),price*(1),target
            row = {'ID': row['ID'],\
                'Stocks': row['Stocks'],\
                'Volume': row['Volume'],\
                'Price bought': row['Price bought'],\
                'Upper price': row['Upper price'], \
                'Lower Price': row['Lower Price'],\
                'Target price': row['Target price']}
            writer.writerow(row)
#Create a new row if the listing does not exist
        if action=='New':
            print('Creating row')
            row = {'ID': row['ID'],\
                'Stocks': stock,\
                'Volume': volume,\
                'Price bought': price,\
                'Upper price': price*(1), \
                'Lower Price': price*(1),\
                'Target price': target}
            writer.writerow(row)
    shutil.move(tempfile.name, filename)


def buyStock():
    stock = input('What do you want to buy: ')
    volume = input('Volume: ')
    price = input('Price: ')
    target = input('Target: ')
    #open database
    database = getDatabase()
    for row in database:
        if stock in row:
            #Add on to the row
            updateDatabase(stock,volume,price,target,'Update')
    else:
        #create new order
        updateDatabase(stock,volume,price,target,'New')
    return

    return stock
def sellStock():
    pass
def checkCapital():
    #open database
    #get captital and return
    pass

def checkStatistics():
    #return capital, deviation and volume of each stock
    pass

def currentTask():
    print(
        '1. Buy Stock'
        '2. Sell Stock'
        '3. Change deviation'
        '4. Check Statistics'
    )
    return input('What would you like to do')
    
def main():
    task = currentTask()
    if task==1:
        buyStock()
    elif task==2:
        sellStock()
    elif task==3:
        changeDeviation()
    elif task==4:
        pass
    pass




    
