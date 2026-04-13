#Se define modularmente los mensajes de bienvenida y solicitud de número
def initial_msg():
    print("Buen día, recibo una lista de números enteros y le indico cuál es la mayor suma entre dos elementos consecutivos.")

def final_msg():
    print("Programa finalizado, hasta pronto.")

def ask_num(msg):
    n=int(input(msg))
    while n<0:
        print("Recuerde, debe ser un número positivo válido.")
        n=int(input(msg))
    return n

#Dado que el ejercicio retorna la mayor suma entre dos elementos consecutivos, es necesario verificar que al menos se ingresen 2 números
def create_list():
    lista=ask_num("¿Cuántos números va a ingresar? ")  
    while lista<2:
        print("Debe ingresar al menos 2 números.")
        lista=ask_num("¿Cuántos números va a ingresar?: ")
    li = []
    for x in range(lista):
        num=ask_num(f"Número # {x+1}: ")
        li.append(num)
    return li

#Se recorre la lista tomando los primeros dos elementos. Si existen una suma de otros dos números mayor que la anterior, se reeemplaza.
#La función devuelve los dos números y su respectiva suma
def check_sum(li):
    i=li[0]+li[1]
    num1=li[0]
    num2=li[1]
    for x in range(len(li)-1):
        suma=li[x]+li[x+1]
        if suma>i:
            i=suma
            num1=li[x]
            num2=li[x+1]
    return (i, num1, num2)

def give_info(info):
    print("La mayor suma encontrada corresponde a ", info[0],", la cual resulta de los números", info[1], "y", info[2], ".")
#Se agrupa todo en un main
def main():
    initial_msg()
    li = create_list()
    info = check_sum(li)
    give_info(info)
    final_msg()
main()
