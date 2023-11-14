class BankAccount:
    def __init__(self, account_num: str, account_name: str, current_balance) -> None:
        self.__account_num = account_num
        self.__account_name = account_name
        self.__current_balance = current_balance

    def add_money(self, money):
        self.__current_balance += money

    def withdraw_money(self, money):
        self.__current_balance -= money

    def show_current_balance(self):
        print(self.__current_balance)

    def show_account_information(self):
        print(self.__account_num, self.__account_name)

    def get_account_num(self):
        return self.__account_num


class NewBankAccount(BankAccount):
    def __init__(
        self, account_num: str, account_name: str, current_balance, promppay
    ) -> None:
        super().__init__(account_num, account_name, current_balance)
        self.__promppay = promppay

    def show_promppay(self):
        print(self.__promppay)

    def __str__(self):
        return f"{self.__promppay} {self.get_account_num()}"


if __name__ == "__main__":

    person_1 = NewBankAccount("1991245632", "Samai Jaisamur", 1000, "0881453222")
    person_1.add_money(500)
    person_1.show_current_balance()
    person_1.show_account_information()
    person_1.show_promppay()
    print(person_1)
