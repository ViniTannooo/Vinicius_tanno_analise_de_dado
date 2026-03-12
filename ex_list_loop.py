# 1 - Crie uma lista frutas contendo as seguintes frutas: "maçã", "banana", "laranja", "uva".
frutas = ["maçã", "banana", "laranja", "uva"]

# 2 - Imprima o primeiro e o último elemento da lista.
frutas[0]
frutas[-1]

# 3 - Adicione a fruta "manga" ao final da lista.
frutas.append("manga")

# 4 - Remova a fruta "banana" da lista.
frutas.remove("banana")

# 5 - Substitua "laranja" por "abacaxi".
frutas[1] = "abacaxi"
frutas

# 6 Crie uma lista numeros contendo os números de 1 a 10.
nums = list(range(1,11))

# 7 Calcule e imprima a soma de todos os números da lista.
sum(nums)

# 8 - Encontre e imprima o maior e o menor número da lista.
max(nums)
min(nums)

# 9 - Inverta a ordem dos elementos na lista e imprima a lista invertida.
nums.reverse()
print(nums)


# 10 - Crie uma lista cidades contendo as seguintes cidades: "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba".
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]

# 11 - Ordene a lista cidades em ordem alfabética.
cidades.sort()
cidades

# 12 - Adicione a cidade "Porto Alegre" ao final da lista.
cidades.append("Porto Alegre")

# 13 - Encontre o índice da cidade "Curitiba" na lista.
cidades.index("Curitiba")

# 14 - Remova a cidade "Rio de Janeiro" da lista.
cidades.remove("Rio de Janeiro")

# 15 - Crie duas listas lista1 e lista2, onde lista1 contém os números [1, 2, 3] e lista2 contém os números [4, 5, 6].
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# 16 - Concatene lista1 e lista2 em uma nova lista lista3.
lista3 = lista1 + lista2

#17 - Imprima lista3.
print(lista3)

# 18 - Crie duas listas animais_domesticos e animais_selvagens, onde animais_domesticos contém ["cachorro", "gato", "coelho"] e animais_selvagens contém ["leão", "tigre", "urso"].
animais_domesticos = ["cachorro", "gato", "coelho"]
animais_selvagens = ["leão", "tigre", "urso"]

# 19 - Concatene as duas listas em uma nova lista todos_animais.
todos_animais = animais_domesticos + animais_selvagens

# 20 - Imprima todos animais
print(todos_animais)
