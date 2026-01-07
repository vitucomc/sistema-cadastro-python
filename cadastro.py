cadastros = []

for i in range (5):
    nome= input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    pessoa = {
        "nome": nome,
        "idade": idade
    }

    cadastros.append(pessoa)

print("\nPessoas cadastradas:")

for pessoa in cadastros:
    print(pessoa["nome"], "-", pessoa["idade"])
