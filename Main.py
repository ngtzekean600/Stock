def main():
    import class_db
    #update scrapbook then stocks
    #input once and update rest
    name = 'OCBC'#input('What is your Stock: ')
    volume = 10 #int(input('What is your Volume: '))
    price = 5 #int(input('What is your price: '))
    S = class_db.stocks()
    s = class_db.scrapbook()
    s.insert_database('EZ',10,5)
    S.update_database('EZ',10,5)
    s.display_database()
    S.display_database()
if __name__ == '__main__':
    main()
