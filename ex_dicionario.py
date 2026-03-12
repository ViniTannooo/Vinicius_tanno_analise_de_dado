# Exercício 1

aluno = {
    'nome': 'Vinícius Tanno',
    'idade': 19,
    'curso': 'Administração'
}

print(f"{aluno['nome']}\n{aluno['idade']}\n{aluno['curso']}")

#---------------------------------------------
# Exercício 2

produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}

produto['marca'] = 'Logitech'
produto['preco'] = 320.00
produto['estoque'] -= 2
produto.pop('marca')

print(produto)

#---------------------------------------------
# Exercício 3

notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}

soma = 0
for nome, nota in notas.items():
    print(f"{nome}: {nota}")
    soma += nota

media = soma / len(notas)
print(f"Média: {media:.2f}")

#---------------------------------------------
# Exercício 4

numeros = {"a": 10, "b": 20, "c": 30}
soma_total = sum(numeros.values())

print(soma_total)

#---------------------------------------------
# Exercício 5

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}

for item in lista:
    frequencia[item] = frequencia.get(item, 0) + 1

print(frequencia)

#---------------------------------------------
# Exercício 6

produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
produtos_filtrados = {}

for produto, preco in produtos.items():
    if preco > 50:
        produtos_filtrados[produto] = preco

print(produtos_filtrados)

#---------------------------------------------
# Exercício 7

tradutor = {
    "apple": "maçã",
    "book": "livro",
    "deal": "acordo",
    "growth": "crescimento"
}

palavra = input("Digite uma palavra em inglês: ").lower()
print(tradutor.get(palavra, "Palavra não encontrada"))

#---------------------------------------------
# Exercício 8

lista_compras = {}

lista_compras["Câmera"] = 1
lista_compras["Iluminação"] = 2
lista_compras["Iluminação"] = 4 
lista_compras.pop("Câmera")

print(lista_compras)

#---------------------------------------------
# Exercício 9

turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}

turma["Lucas"] = {"idade": 20, "notas": [7, 8, 9]}

maior_media = 0
melhor_aluno = ""

for aluno, dados in turma.items():
    media = sum(dados['notas']) / len(dados['notas'])
    print(f"{aluno}: Média {media:.1f}")
    
    if media > maior_media:
        maior_media = media
        melhor_aluno = aluno

print(f"Melhor aluno: {melhor_aluno}")

#---------------------------------------------
# Exercício 10

funcionarios = {}

def cadastrar_funcionario(nome, cargo, salario):
    funcionarios[nome] = {"Cargo": cargo, "Salário": salario}

def consultar_funcionario(nome):
    return funcionarios.get(nome, "Funcionário não encontrado no sistema.")

cadastrar_funcionario("Rafael", "Gestor de Tráfego", 4500)
cadastrar_funcionario("Mendes", "Produtor de Conteúdo", 4500)

print(consultar_funcionario("Rafael"))
