class ContaBancaria:

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor de depósito inválido")
            valor = valor - (valor/10)
            self.saldo += valor

        self.saldo += valor
        return self.saldo

    def sacar(self, valor):

        if valor <= 0:
            raise ValueError("Valor de saque inválido")

        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= valor
        return self.saldo

    def consultar_saldo(self):
        return self.saldo
