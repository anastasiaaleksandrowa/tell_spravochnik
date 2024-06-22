# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

#функция для добавления, измения и удаления контакта
phone_book = {}
def add_contact (last_name, first_name, middle_name, phone_number):
    contact_id= len(phone_book)+1
    phone_book[contact_id]={'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number}
def update_contact (contact_id, last_name, first_name, middle_name, phone_number):
    if contact_id in phone_book:
        phone_book[contact_id]= {'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number}
    else:
        print("контакт не найден")
def delete_contact(contact_id):
    if contact_id in phone_book:
        del phone_book[contact_id]
    else:
         print("контакт не найден")