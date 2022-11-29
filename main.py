import math

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


#Remova o último ponto de exclamação (!) do final de uma string
def remove(s):
    return s.removesuffix('!')


#inverta todas as palavras dentro da string passada.
def reverse_words(s):
     return " ".join(s.split(" ")[::-1])


# Dadas duas palavras e uma letra,
#  retorne uma única palavra que seja uma combinação de ambas as palavras, mescladas no ponto em que a letra especificada aparece pela primeira vez em cada palavra
# . A palavra retornada deve ter o início da primeira palavra e o final da segunda, com a letra divisória no meio. Você pode presumir que ambas as palavras conterão a letra divisória.
def string_merge(string1, string2, letter):
    return string1[:string1.index(letter)] + string2[string2.index(letter):]

#Complete a solução para que retorne verdadeiro se o primeiro argumento (string) passado terminar com o 2º argumento (também uma string).
def solution(string, ending):
    return string.endswith(ending)

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false


#AO CONTRÁRIO 
def starts_with(st, prefix): 
    return st.startswith(prefix) 

#retornar uma string atribuindo a citação à pessoa no seguinte formato:
def quotable(name, quote):
    return f'{name} said: "{quote}"' 


#onde value é um número preenchido com 5 dígitos.
def solution(value):
    return f'Value is {value:05d}'



def solution(st, limit):
    if len(st) <= limit:
        return st
    return st[:limit] + '...'



def delta(a, b, c):
    return pow(b, 2) - 4 * a * c

def bhaskara(a, b, c):
    resultado_delta = delta(a, b, c)

    if resultado_delta < 0:
        return 'Delta negativo'

    raiz_delta = round(math.sqrt(resultado_delta), 2)

    x1 = round((-b + raiz_delta) / (2 * a), 2)
    x2 = round((-b - raiz_delta) / (2 * a), 2)

    return f'x1={x1}, x2={x2}'

print(bhaskara(1, 5, 2))
# x1=-0.44, x2=-4.56
print(bhaskara(3, 10, 2))
# x1=-0.21, x2=-3.12

for i in range(4):
    print(i)
# 0 
# 1 
# 2 
# 3 

minha_string = 'Churros'
for index, item in enumerate(minha_string):
    print(index,item)
# 0 C
# 1 h
# 2 u
# 3 r
# 4 r
# 5 o
# 6 s
