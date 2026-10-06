import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from atm.conta import ContaBancaria


class CaixaEletronico:

    def __init__(self):
        self.contas = {}

    def criar_conta(self, titular, saldo_inicial=0):

        if titular in self.contas:
            raise ValueError("Conta já existe")

        conta = ContaBancaria(titular, saldo_inicial)
        self.contas[titular] = conta

        return conta

    def obter_conta(self, titular):

        if titular not in self.contas:
            raise ValueError("Conta não encontrada")

        return self.contas[titular]

    def depositar(self, titular, valor):

        conta = self.obter_conta(titular)
        return conta.depositar(valor)

    def sacar(self, titular, valor):

        conta = self.obter_conta(titular)
        return conta.sacar(valor)

    def saldo(self, titular):

        conta = self.obter_conta(titular)
        return conta.consultar_saldo()
