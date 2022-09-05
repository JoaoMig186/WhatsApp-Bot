# Parte que gera uma lista com um nome padrão que pode ser substituído em "grupos_ou_pessoas" pelo nome que desejar e atribui numeração a ele
# Part that returns a list with a generic name that can be replace in "grupos_ou_pessoas" (translating: group_or_people) for the disired name and increments a number in this

# No exemplo abaixo ele foi utilizado para gerar uma lista de nomes com numerações de 1 até 10
# In exemple below it was utilited for result a list of names with numbers from 1 to 10

# Após a execução no console, basta copiar e colar os nomes gerados no vetor de nomes em "bot.py"
# After execute this in the console, you can copy and paste the generated names in the array at "bot.py"

listaDeContatos = []

for numero in range(1,11):
    grupos_ou_pessoas = "Fulano/so-and-so" + str(numero)
    listaDeContatos.append(grupos_ou_pessoas)
print(listaDeContatos)