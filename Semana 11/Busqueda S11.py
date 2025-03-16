#Busqueda en la matriz Bidimensional
def buscar_valor(matriz,valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==valor:
                return i,j #Retorna a la posicion si esta se encuentra
    return None # retornara a none si no esta
# Matriz 3x3
matriz= [
    [15 ,30,35],
    [20 ,10 ,20],
    [40 ,50,60]
]
# Solicitar el valor a buscar
valor_buscar = int(input("Ingrese el valor que se esta buscando en la matriz:"))
resultado = buscar_valor(matriz,valor_buscar)

if resultado:
    print(f"Valor encontrado en la posicion :{resultado}")
else:
    print(f"No se encontrado el valor en la posicion :{resultado}.")