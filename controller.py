import phone_book

pb = phone_book.PhoneBook('phone_book.txt')


while True:
    print(pb.menu())
    while True:
        chc = input('Выберите пункт меню: ')
        if chc.isdigit() and 0 < int(chc) <= 7:
            choice = int(chc)
            break
        else:
            print(f'Введите число от 1 до 7: ')
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите номер телефона: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input("Введите поисковый запрос: ")
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(input("Введите индекс контакта, который нужно изменить: "))
            name = input('Введите имя (или Enter - оставить без изменений): ')
            phone = input('Введите номер телефона (или Enter - оставить без изменений): ')
            comment = input('Введите комментарий (или Enter - оставить без изменений): ')
            pb.change_contact(index-1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input("Введите индекс удаляемого контакта: "))
            pb.delete_contact(index-1)
        case 6:
            pb.save()
        case 7:
            print("До встречи!")
            break