#Esse programa não conta o valor que o cliente possui na conta, apenas o valor disponível dentro ATM.
class Caixa:
    def __init__(self, banco, saldo):
        self.y = [0, 0, 0, 0, 0, 0]
        self.banco = banco
        self.saldo = saldo
    def carregar_notas(self):
        self.y[0] = int(input("Insira a quantidade de notas de 100 que deseja colocar.\n"))
        self.y[1] = int(input("Insira a quantidade de notas de 50 que deseja colocar.\n"))
        self.y[2] = int(input("Insira a quantidade de notas de 20 que deseja colocar.\n"))
        self.y[3] = int(input("Insira a quantidade de notas de 10 que deseja colocar.\n"))
        self.y[4] = int(input("Insira a quantidade de notas de 5 que deseja colocar.\n"))
        self.y[5] = int(input("Insira a quantidade de notas de 2 que deseja colocar.\n"))

        self.saldo = (self.y[0]*100) + (self.y[1]*50) + (self.y[2]*20) + (self.y[3]*10) + (self.y[4]*5) + (self.y[5]*2) + self.saldo
        self.banco[0] = self.banco[0] + self.y[0]
        self.banco[1] = self.y[1] + self.banco[1]
        self.banco[2] = self.y[2] + self.banco[2]
        self.banco[3] = self.y[3] + self.banco[3]
        self.banco[4] = self.y[4] + self.banco[4]
        self.banco[5] = self.y[5] + self.banco[5]

    def retirar_notas(self):
        self.y = [0, 0, 0, 0, 0, 0]

        temp = int(input("Insira a quantidade de notas de 100 que deseja retirar.\n"))
        if (self.banco[0] - temp) < 0:
            print("Não há notas de 100 suficientes.")
        elif(self.saldo - (temp*100)) < 0:
            print("VALOR EXCEDIDO, SELECIONE NOTAS MENORES.")
        else:
            self.y[0] = temp
            self.banco[0] = self.banco[0] - self.y[0]
            self.saldo = self.saldo - (temp*100)

        temp = int(input("Insira a quantidade de notas de 50 que deseja retirar.\n"))
        if (self.banco[1] - temp) < 0:
            print("Não há notas de 50 suficientes.")
        elif (self.saldo - (temp * 50)) < 0:
            print("VALOR EXCEDIDO, SELECIONE NOTAS MENORES.")
        else:
            self.y[1] = temp
            self.banco[1] = self.banco[1] - self.y[1]
            self.saldo = self.saldo - (temp * 50)

        temp = int(input("Insira a quantidade de notas de 20 que deseja retirar.\n"))
        if (self.banco[2] - temp) < 0:
            print("Não há notas de 20 suficientes.")
        elif (self.saldo - (temp * 20)) < 0:
            print("VALOR EXCEDIDO, SELECIONE NOTAS MENORES.")
        else:
            self.y[2] = temp
            self.banco[2] = self.banco[2] - self.y[2]
            self.saldo = self.saldo - (temp * 20)

        temp = int(input("Insira a quantidade de notas de 10 que deseja retirar.\n"))
        if (self.banco[3] - temp) < 0:
            print("Não há notas de 10 suficientes.")
        elif (self.saldo - (temp * 10)) < 0:
            print("VALOR EXCEDIDO, SELECIONE NOTAS MENORES.")
        else:
            self.y[3] = temp
            self.banco[3] = self.banco[3] - self.y[3]
            self.saldo = self.saldo - (temp * 10)

        temp = int(input("Insira a quantidade de notas de 5 que deseja retirar.\n"))
        if (self.banco[4] - temp) < 0:
            print("Não há notas de 5 suficientes.")
        elif (self.saldo - (temp * 5)) < 0:
            print("VALOR EXCEDIDO, SELECIONE NOTAS MENORES.")
        else:
            self.y[4] = temp
            self.banco[4] = self.banco[4] - self.y[4]
            self.saldo = self.saldo - (temp * 5)

        temp = int(input("Insira a quantidade de notas de 2 que deseja retirar.\n"))
        if (self.banco[5] - temp) < 0:
            print("Não há notas de 2 suficientes.")
        elif (self.saldo - (temp * 2)) < 0:
            print("VALOR EXCEDIDO.")
        else:
            self.y[5] = temp
            self.banco[5] = self.banco[5] - self.y[5]
            self.saldo = self.saldo - (temp * 2)

        saque = (self.y[0]*100) + (self.y[1]*50) + (self.y[2]*20) + (self.y[3]*10) + (self.y[4]*5) + (self.y[5]*2)
        if saque > self.banco[6]:
            self.banco[6] = saque
        elif saque < self.banco[7]:
            self.banco[7] = saque

        self.banco[9] = self.banco[9] + saque
        self.banco[10] = self.banco[10] + 1
        self.banco[8] = self.banco[9] / self.banco[10]
        print("O valor retirado foi: " + str(saque))



    def retornar_saldo(self):
        return self.saldo
    def retornar_notas(self):
        return self.banco



SaldoTotal = 10000
itau = [3123, 40, 40, 40, 40, 40, 0, 1000000000, 0, 0, 0]   #Do lote 6(ou 7, se não estiver iniciando a contagem do 0) para cima, respectivamente: Maior Saque, Menor Saque, Média, Total dos Saques, Número de vezes que o banco foi selecionado
caixa = [40, 40, 40, 40, 40, 40, 0, 1000000000, 0, 0, 0]  #O primeiro é a nota de 100, depois a de 50, depois 20, 10, 5, 2
sant = [40, 40, 40, 40, 40, 40, 0, 1000000000, 0, 0, 0]
BncBr = [40, 40, 40, 40, 40, 40, 0, 1000000000, 0, 0, 0]

banco = [BncBr, sant, itau, caixa]
cancela = ""
while (cancela != "SAIR"):
    try:
        x = int(input("Insira o código do banco desejado. 1: Banco do Brasil; 2: Santander; 3: Itaú; 4: Caixa\n"))
        p1 = Caixa(banco[x-1], SaldoTotal)
    except:
        print("Código Inválido.")
    else:
        metodo = int(input("Insira o número de acordo com o que deseja. 1: Carregar notas; 2: Retirar Notas; 3: Estatísticas; 9: Sair;\n"))
        if metodo == 1:
            p1.carregar_notas()
            SaldoTotal = p1.retornar_saldo()
            banco[x-1] = p1.retornar_notas()
        elif metodo == 2:
            p1.retirar_notas()
            SaldoTotal = p1.retornar_saldo()
            banco[x-1] = p1.retornar_notas()
        elif metodo ==3:
            for i in range(0, 3):
                if banco[i][10] == 0:
                    banco[i][7] = 0

            print(f'O saldo do caixa é: {SaldoTotal}')
            print(f'---ESTATÍSTICAS DE CADA BANCO---')

            for z in range(0,3):
                if z == 0:
                    print(f'BANCO DO BRASIL:')
                elif z == 1:
                    print(f'SANTANDER:')
                elif z == 2:
                    print(f'ITAÚ:')
                elif z == 3:
                    print(f'CAIXA:')

                print(f'Notas de cem:{banco[z][0]}\nNotas de 50: {banco[z][1]} \nNotas de 20: {banco[z][2]} \nNotas de 10: {banco[z][3]} \nNotas de 5: {banco[0][4]} \nNotas de 2: {banco[0][5]}')
                print(f'Maior valor sacado: {banco[z][6]}\nMenor valor sacado:{banco[z][7]}')
                print(f'Total sacado: {banco[z][9]}\nMédia: {banco[z][10]}')

        cancela = input("Clique ENTER para Iniciar, ou digite SAIR para resetar a máquina.\n")

