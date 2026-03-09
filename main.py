from bank_account import BankAcct

# membuat objek
bank = BankAcct()

# set saldo awal
bank.set_saldo(1000)

# menjalankan program
bank.deposit()
bank.withdraw()
bank.showoutput()