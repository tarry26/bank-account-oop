# Class rekening bank

class BankAcct:

    def __init__(self):
        self.__saldo = 0
        print("Aplikasi Perbankan untuk menerima Setoran dan Penarikan")

    # setter
    def set_saldo(self, saldo):
        self.__saldo = saldo

    # getter
    def get_saldo(self):
        return self.__saldo

    def deposit(self):
        jumlah = float(input("Masukkan jumlah uang yang akan disetor: "))
        self.__saldo += jumlah
        print("\nJumlah yang disetor:", jumlah)

    def withdraw(self):
        jumlah = float(input("Masukkan jumlah uang yang akan ditarik: "))
        if self.__saldo >= jumlah:
            self.__saldo -= jumlah
            print("\nJumlah yang ditarik:", jumlah)
        else:
            print("\nSaldo tidak mencukupi")

    def showoutput(self):
        print("\nSaldo yang tersedia =", self.get_saldo())