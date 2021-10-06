#EX6 - Estruturas de Condicao - Emprestimo bancario para compra de uma casa

valorCasa = int(input("Valor da casa a ser comprada:"))
salario = int(input("Valor do salario:"))
anosPagar = int(input("Quantidade de anos a pagar a casa:"))
mesesPagar = float((12 / anosPagar))
trintaPorCentoSalario = (salario * 0.3) - salario
prestacaoCasa = float((valorCasa / mesesPagar))

print()
print("30 por cento salario:", trintaPorCentoSalario, "PRestacao casa:", prestacaoCasa)

if prestacaoCasa > trintaPorCentoSalario:
  print("Voce nao pode fazer o emprestimo.. Sorry..")
else:
  print("O emprestimo pode ser concebido")
