def main():
    import class_db
    #update scrapbook then stocks
    #input once and update rest
    name = 'OCBC'#input('What is your Stock: ')
    volume = 10 #int(input('What is your Volume: '))
    price = 5 #int(input('What is your price: '))
    S = class_db.stocks()
    s = class_db.scrapbook()
    
if __name__ == '__main__':
    main()
