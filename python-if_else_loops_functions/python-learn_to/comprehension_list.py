#Ejercicios:
#Doble de los Números
lista = [1, 2, 3, 4, 5]
doble = [ i * 2 for i in lista]
print(doble)

#Filtrar y Transformar en un Solo Paso
word = ["sol", "mar", "montaña", "rio", "estrella"] 
new_words = [word.upper() for word in word if len(word) > 3]
print(new_words)

#Crear un Diccionario con List Comprehension
keys = ["nombre", "edad", "ocupación"]
values = ["Juan", 30, "Ingeniero"]
dictionary = {keys[i] : values[i] for i in range(len(keys))}
print(dictionary)

#Anidación de List Comprehensions
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = [[column[i] for column in matrix] for i in range(len(matrix[0]))]
print(transposed)

#Extraer Información de una Lista de Diccionarios
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

nombres_madrid = [persona["nombre"] for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30]
print("Nombres de personas en Madrid mayores de 30 años:", nombres_madrid)