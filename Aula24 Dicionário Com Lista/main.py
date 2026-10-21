personagem = {
    "nome": "Link",
    "classe": "Arqueiro",
    "nivel": 1, 
    "inventario": [] # Lista dentro do dicionário
}
item1 = input("Digite um item:")
item2 = input("Digite outro item:")
personagem["inventario"].append(item1)
personagem["inventario"].append(item2)

print("Nome", personagem["nome"])
print("Classe", personagem["classe"])
print("Nível", personagem["nivel"])
print("---Inventário---")
for item in personagem["inventario"]:
    print("-", item)