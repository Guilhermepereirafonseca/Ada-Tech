# > CONVERSAO DE TIPOS

# idade = '19'
# numero1 = '10'
# numero2 = '20'

# print(numero1 + numero2) # irá fazer uma concatenação (junta os textos)

idade = '19'

idade_inteira = int(idade) # de str sera convertido para int

print(idade_inteira, type(idade_inteira))

# int()
# str()
# float()
# bool()

altura = float(input('Informe sua altura: ')) # input por padrão retorna sempre str