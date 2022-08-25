from view import *

def main():
    print('1 - CREATE, 2 - LISTING, 3 - RETRIEVE, 4 - UPDATE, 5 - DELETE')
    
    choice = input('Выберите действие (1, 2, 3, 4, 5): ')
    if choice == '1':
        print(create_product())
    elif choice == '2':
        print(list_of_products())
    elif choice == '3':
        print(get_one_product())
    elif choice == '4':
        print(update_product())
    elif choice == '5':
        print(delete_product())
    else:
        print('Такого действия нет')
        main()
    
    ask = input('Хотите продолжить(Yes/No)?: ')
    if ask.lower() == 'yes':
        main()
    else:
        print('До свидания!')
main()