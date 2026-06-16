while True:
 print("======================================")
 print("SISTEMA: CALCULADORA E CAIXA ")
 print("======================================")
 print("1-Resolver quatro operações básicas !")
 print("2-fluxo de caixa (cálculo de troco)")
 print("3-multiplicação de matriz (2x2)")
 print("0-sair")

 opcao=input("\nDigite o número da opção desejada (0 a 3): ")

#=================================================
#opcao 4 : SAIR DO PROGRAMA
#=================================================
 if opcao=="0":
  print("\n Sistema encerrado com sucesso ")
  break 
#==================================================
# OPÇÃO 1 :AS QUATROS OPERAÇÕES BÁSICAS
#==================================================
 elif opcao =="1":
   print ("\n---QUATRO OPERAÇÕES---")
   try:
      n1= float(input("digite o primeiro número: "))
      n2= float(input("digite o segundo número: "))

      print("Escolha a operacao: (+, -, *, /)")
      operacao= input("operação: ")

#condicionais para decidir a operação
      if operacao == "+":
        resultado = n1 + n2
        print(f"Resultado da soma é : {resultado}")
      elif operacao == "-":
        resultado = n1 - n2    
        print(f"Resultado da subtração é: {resultado} ")
      elif operacao =="*":
        resultado = n1*n2
        print (f"Resultado da multiplicação é:{resultado}")   
      elif operacao == "/":
        if n2 == 0:
           print ("Não é possível dividir por zero.")
        else:  
         resultado = n1/n2   
         print(f"resutado da divisão: {resultado}")
      else:
        print("Operações inválida")  
      
   except ValueError:   
      print ("\n você inseriu letras ou caracteres inválidos!")
   input("\n pressione ENTER para voltar ao menu...")
 
#===================================================
# OPÇÃO 2: FLUXO DE CAIXA (CÁLCULO DE TROCO)
#=================================================== 
 elif opcao == "2":
  print("\n--- MENU: FLUXO DE CAIXA (TROCO) ---")
  try:
       valor_total = float(input("Digite o valor total da compra: R$ "))
       valor_pago = float(input("Digite o valor pago pelo cliente: R$ "))

       if valor_pago < valor_total:
          print("\n Erro no Caixa: O valor pago é menor que o total da compra!")
       else:
          # Transforma o troco em centavos inteiros para evitar erros de arredondamento do Python
         troco = round((valor_pago - valor_total) * 100)
         print(f"\nTroco total: R$ {troco / 100:.2f}")
         print("-----------------------------------------")
         print("Cédulas e Moedas a serem entregues:")

                # Execução do Algoritmo Guloso (testando da maior nota até a menor moeda)
       if troco >= 20000:
          print(f"- {troco // 20000} nota(s) de R$ 200,00")
          troco %= 20000
       if troco >= 10000:
          print(f"- {troco // 10000} nota(s) de R$ 100,00")
          troco %= 10000
       if troco >= 5000:
          print(f"- {troco // 5000} nota(s) de R$ 50,00")
          troco %= 5000
       if troco >= 2000:
          print(f"- {troco // 2000} nota(s) de R$ 20,00")
          troco %= 2000
       if troco >= 1000:
          print(f"- {troco // 1000} nota(s) de R$ 10,00")
          troco %= 1000
       if troco >= 500:
         print(f"- {troco // 500} nota(s) de R$ 5,00")
         troco %= 500
       if troco >= 200:
          print(f"- {troco // 200} nota(s) de R$ 2,00")
          troco %= 200
       if troco >= 100:
          print(f"- {troco // 100} moeda(s) de R$ 1,00")
          troco %= 100
       if troco >= 50:
          print(f"- {troco // 50} moeda(s) de R$ 0,50")
          troco %= 50
       if troco >= 25:
          print(f"- {troco // 25} moeda(s) de R$ 0,25")
          troco %= 25
       if troco >= 10:
          print(f"- {troco // 10} moeda(s) de R$ 0,10")
          troco %= 10
       if troco >= 5:
          print(f"- {troco // 5} moeda(s) de R$ 0,05")
          troco %= 5
       if troco >= 1:
          print(f"- {troco} moeda(s) de R$ 0,01")

  except ValueError:
    print("\n Erro de Digitação: Insira valores numéricos válidos (ex: 50.50)!")

input("\nPressione ENTER para voltar ao menu...")

#=================================================
# OPÇÃO 3: MULTIPLICAÇÃO DE MATRIZ 2X2
#=================================================
if opcao == "3":
   print("\n---MENU: MULTIPLICAÇÃO DE MATRIZES 2X2---")
   try:
      
      print("\nInsira os dados da Matriz A:")
      a11 = float(input("Posição [1][1]: "))
      a12 = float(input("Posição [1][2]: "))
      a21 = float(input("Posição [2][1]: "))
      a22 = float(input("Posição [2][2]: "))

      print("\nInsira os dados da Matriz B:")
      b11 = float(input("Posição [1][1]: "))
      b12 = float(input("Posição [1][2]: "))
      b21 = float(input("Posição [2][1]: "))
      b22 = float(input("Posição [2][2]: "))

      res11 = (a11 * b11) + (a12 * b21)  # Linha 1 de A x Coluna 1 de B
      res12 = (a11 * b12) + (a12 * b22)  # Linha 1 de A x Coluna 2 de B
      res21 = (a21 * b11) + (a22 * b21)  # Linha 2 de A x Coluna 1 de B
      res22 = (a21 * b12) + (a22 * b22)  # Linha 2 de A x Coluna 2 de B

      print("\nResultado Final da Matriz (A x B):")
      print(f"[ {res11}   {res12} ]")
      print(f"[ {res21}   {res22} ]")

   except ValueError:
      print("Erro de Digitação: Use apenas números inteiros ou decimais!")
   input("\nPressione ENTER para voltar ao menu...")