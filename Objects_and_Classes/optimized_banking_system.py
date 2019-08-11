class Bank_account:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


    def print_account(self):
        return f'{self.name} -> {self.balance:.2f} ({self.bank})'

def create_account(data_list):
    return Bank_account(name=data_list[1], bank=data_list[0], balance=float(data_list[2]))


def sort_accounts(data_list):
    new_list = sorted(data_list, key=lambda account: (-account.balance, len(account.bank)))
    for item in new_list:
        print(item.print_account())

accounts_list = []

while True:
    data_list = input().split(' | ')
    if data_list[0] == 'end':
        break

    new_account = create_account(data_list)
    accounts_list.append(new_account)

sort_accounts(accounts_list)

