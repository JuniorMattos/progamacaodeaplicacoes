nums = [5,7,2,15,4,1,3]
maior = 0
menor = 10000000000000
total = 0

"""print('--------------------------------------------------------')
print(f'Lista original  {nums}')
print('--------------------------------------------------------')
print(f'Tamanho da lista: {len(nums)}')
print(f'Maior valor da lista: {max(nums)}')
print(f'Menor valor da lista: {min(nums)}')
print(f'Soma de todos os elementos da lista: {sum(nums)}')
print(f'Lista em ordem crescente: {sorted(nums)}')
print(f'Lista em ordem decrescente: {sorted(nums, reverse = True)}')"""

for num in nums:

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    total += num

print('--------------------------------------------------------')
print(f'Lista original  {nums}')
print('--------------------------------------------------------')
print(f'Tamanho da lista: {len(nums)}')
print(f'Maior valor da lista: {maior}')
print(f'Menor valor da lista: {menor}')
print(f'Soma de todos os elementos da lista: {total}')  

def crescente(nums):
    for i in range(0, len(nums)):
        for num in range(i, len(nums)):
            if(nums[i] > nums[num]):
                aux = nums[num]
                nums[num] = nums[i]
                nums[i] = aux

    print(f'Lista em ordem crescente: {nums}')

def descrecente(nums):
    for i in range(0, len(nums)):
        for num in range(i, len(nums)):
            if(nums[i] < nums[num]):
                aux = nums[num]
                nums[num] = nums[i]
                nums[i] = aux
    
    print(f'Lista em ordem decrescente: {nums}')

crescente(nums)
descrecente(nums)