""" cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars) """

#Ordenando uma lista temporaria com o sorted
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)


print("\nHere is the sorted list:")
print(sorted(cars))

cars.reverse()
print(cars)

# Descobrindo o tamanho de uma lista

print(len(cars))
