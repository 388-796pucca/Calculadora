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
 
