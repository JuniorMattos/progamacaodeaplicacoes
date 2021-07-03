valores = []
total = 0
quant = 0

while quant != 20:
    quant += 1
    n = int(input("Informe um valor: "))
    
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n
    total += n

media = total/quant

print('--------------------------------------------')

print(f'Media dos valores: {media}')

print(f'Maior valores: {maior}')

print(f'Menor valores: {menor}')

"""
for i in range(20):
    valores.append(int(input("Informe um valor: "))) 

media = sum(valores)/len(valores)

print(f'Valores: {valores}')

print(f'Media dos valores: {media}')

print(f'Maior valores: {max(valores)}')

print(f'Menor valores: {min(valores)}')
"""

