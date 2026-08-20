comando = "Equipar espada"


partes = comando.split()

acao = partes[0]
item = partes[1]

if acao == "Equipar":
    print(f"Equipando {item}")
elif acao == "Desequipar":
    print(f"Desquipando {item}")
else: 
    print("Comando desconhecido")