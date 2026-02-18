def initial_msg():
    print("Buen día. De una lista de palabras que ingrese, le indico cuáles de ellas contienen las mismas letras.")

def final_msg():
    print("Programa finalizado, hasta pronto.")

def ask_str(msg):
    m=str(input(msg))
    return m

def ask_num(msg):
    n=int(input(msg))
    while n<0:
        print("Recuerde, debe ser un número positivo válido.")
        n=int(input(msg))
    return n

def create_list():
    lista=ask_num("¿Cuántas palabras va a ingresar? ")
    li=[]
    for x in range(lista):
        w=ask_str(f"Palabra # {x+1}: ")
        li.append(w)
    return li

def check_word(li):
    final=[]
    l=len(li)
    for x in range(l):
        for y in range(x+1, len(li)):
                if sorted(li[x])==sorted(li[y]):
                    final.append((li[x], li[y]))
    return final

def main():
    initial_msg()
    lista = create_list()
    resultado = check_word(lista)
    if len(resultado) == 0:
        print("No hay palabras que contengan las mismas letras.")
    else:
        print("Las palabras que contienen las mismas letras son:")
        for par in resultado:
            print(par[0], "y", par[1])
    final_msg()
main()