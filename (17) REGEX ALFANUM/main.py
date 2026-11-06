import re
codigo = input("Digite o código:")

while not re.fullmatch(r"[a-z0-9]{5}", codigo):
    codigo = input("Código inválido! Digite o código novamente:")

print("Código válido!")
