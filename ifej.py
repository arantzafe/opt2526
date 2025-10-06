# contador hasta 100
"""
for contador in range(10,1,-1):
    print(contador)
def mostrar_mensaje():
    return ("Hola, soy una función sin return.")

respuesta = mostrar_mensaje()
print("El valor devuelto es:", respuesta)  # None
"""
contador = 0  # variable global

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1
incrementar()
print(contador)  # 1