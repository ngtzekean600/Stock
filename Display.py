def displayDatabase():
    from Db import getDatabase
    for line in getDatabase():
        print(line)

def currentTask():
    print(
        '1. Buy Stock'
        '2. Sell Stock'
        '3. Change deviation'
        '4. Check Statistics'
    )
    return input('What would you like to do')
