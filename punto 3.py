def initial_msg():
    print("Buen día, recibo una lista de números enteros y le indico cuáles de ellos son primos")

def final_msg():
    print("Programa finalizado, hasta pronto.")

def ask_num(msg):
    n = int(input(msg))
    while n < 0:
        print("Recuerde, debe ser un número positivo válido.")
        n = int(input(msg))
    return n

def create_list():
    lista = ask_num("¿Cuántos números va a ingresar? ")  
    li = []
    for x in range(lista):
        num = ask_num(f"Número # {x+1}: ")
        li.append(num)
    return li

def check_prime(li):
    final=[]
    for x in range(len(li)):
        if li[x]>1:
            for i in range (2,li[x]):
                if li[x]%i==0:
                    break
            else:
                final.append(li[x])
    return (final)

def give_info(info):
    print("Los números primos encontrados son: ", info)

def main():
    initial_msg()
    li = create_list()
    info = check_prime(li)
    give_info(info)
    final_msg()
main()
