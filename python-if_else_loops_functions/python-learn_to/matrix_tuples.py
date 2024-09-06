#Lista de dos dimensiones
matrix = [[1, 2, 3], [3, 4, 5], [7, 8 ,9]]
print("Matrix: ", matrix)
for column in matrix:
    for element in column:
        print(element, end=' ')
    print()
#3 dimensiones
tensor = [[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]]
print("\ntensor: ", tensor)
for bloque in tensor:
    for column in tensor:
        for element in column:
            print(element, end=' ')
        print()
    print()

#Tuples
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print("tupla1: ", tupla1)
print("tupla2: ", tupla2)

#tupla concatenada
print("tupla concatenada: ", tupla1 + tupla2)