# В проекте «Дом питомца» добавим новую услугу — электронный кошелек. Необходимо создать класс «Клиент»,
# который будет содержать данные о клиентах и их финансовых операциях. О клиенте известна следующая информация:
# имя, фамилия, город, баланс.
#
# Далее сделайте вывод о клиентах в консоль в формате:
# «Иван Петров. Москва. Баланс: 50 руб.»

class Client:
    def __init__(self, name, last_name, city, balance):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.last_name}. {self.city}. Баланс: {self.balance} руб.'



ivan = Client('Иван', 'Петров', 'Москва', 50)
print(ivan)

