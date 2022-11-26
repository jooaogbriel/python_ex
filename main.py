# variáveis 
minha_string = 'hello'

print(type(minha_string))

def minha_funcao():
    return 'my_function'

print(minha_funcao())

#concat

minha_string1 = 'cow'
minha_string2 = 'boy'
result = minha_string1 + minha_string2
print(result)

string = "Monty Python"
# Acessando a palavra "Monty"
string[0:5]
"Monty"
# Como queremos desde o inicio da string, podemos omitir o 0
string[:5]
"Monty"
# Perceba que o indice 5 não está compreendido no fatiamento
# Acessando a palavra "Python"
string[6:12]
'Python'
# Como queremos até o fim da string, podemos omitir o 12,
# que representa o ultimo indice da string
string[6:]
'Python'

#capitalize -> Muda o primeiro caractere da string para maiúscula e o restante para minúscula.

string = "mOnTy pYtHon"
string.capitalize()
'Monty python'

#count -> Retorna o número de ocorrências de uma determinada sub-string da string.
string = "Monty Python"
string.count("Python")
1
string.count('o')
2
string = "Monty Python"

#join 
s = "$".join(['olá', 'modulo', 'm5'])
s = 'olá$modulo$m5'

#Desenvolva a função que recebe 2 inteiros em formato de string (a e b) e retorne a soma deles, também em formato de string.
def sum_str(a, b):
    if a == '' : a = '0'
    if b == '' : b = '0'
    return str(int(a)+int(b))
