#Configuracion de una app
#Se crea un diccionario para almacenar configuraciones de una apliacion 
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True 
}
print("\nConfiguracion:", config)

#Contador de palabras
#Se utiliza un diccionario para contar la frecuencia de palabras en una lista
words = ["apple", "banana", "orange", "pear", "watermelon"]
counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
print("\nCounter of words: ", counter)
