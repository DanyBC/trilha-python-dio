valor_do_depósito = 1

while valor_do_depósito != 0:
    valor_do_depósito = float(input())
    if valor_do_depósito > 0:
      print(f"""Deposito realizado com sucesso! 
Saldo atual:R${valor_do_depósito:.2f}""")
    elif valor_do_depósito < 0:
      print("Valor invalido! Digite um valor maior que zero.")
    if valor_do_depósito == 0:
      print("Encerrando o programa...")
      break