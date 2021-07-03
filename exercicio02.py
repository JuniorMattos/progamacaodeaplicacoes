valores = []
quant = 0
total = 0



while quant != 4:
    quant += 1
    n = int(input("Informe um valor: "))
    total += n

media = total/quant

print(f'Valores: {valores}')

print(f'Media: {media}')

print('Media maior que 1?')

if media > 1:
    print('POSITIVO')
else:
    print('NEGATIVO')

"""for i in range(4):    
    valores.append(int(input("Informe um valor: ")))

media = sum(valores)/len(valores)

print(f'Valores: {valores}')

print(f'Media: {media}')

print('Media maior que 1?')

if media > 1:
    print('POSITIVO')
else:
    print('NEGATIVO')"""