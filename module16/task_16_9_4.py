# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
# Вам необходимо написать программу, которая позволит составить список гостей.
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
#
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Client:
    def __init__(self, name, last_name, city, balance):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.last_name}. {self.city}. Баланс: {self.balance} руб.'

    def get_info(self):
        return f'{self.name} {self.last_name} из города {self.city}'



ivan = Client('Иван', 'Петров', 'Москва', 50)
timofei = Client('Тимофей', 'Егоров', 'Надым', 100)
marfa = Client('Марфа', 'Александрова', 'Казань', 70)

clients = [ivan, timofei, marfa]
for client in clients:
    print(client.get_info())

