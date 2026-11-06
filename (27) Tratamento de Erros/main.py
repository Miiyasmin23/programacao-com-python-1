# print("Início")

# assert 2 > 1, "2 Deve ser maior ddo que 1"

# print ("Fim")

# try: 
#     idade = int(input("Digite sua idade"))
#     print("Sua idade é", idade)
# except:
#     print("Digite somente númeres!")
    
# try:
#     numero = int(input("Digite um número: "))
#     resultado = 10 / numero
#     print(resultado)
    
# except ValueError:
#     print("DIGITE UM NÚMERO INTEIRO!!!")
# except ZeroDivisionError:
#     print("NÃO EXISTE DIVISÃO POR ZERO")
    
try:
    numero = int(input("Digite um número"))
except ValueError:
    print("Calor inválido")
else: # Só é executado quando o except é ignorado
    print("Número correto!")
finally:
    print("Programa finalizado!!!")
