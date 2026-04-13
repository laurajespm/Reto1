def ask_str(msj):
    m=str(input(msj))
    return m
#Se recorre la palabra y se verifica de atrás hacia adelante si coincide con la debida letra, algo así como un proceso espejo.
def check_word(w):
    l=len(w)  
    for x in range(l):
        if w[x]!=w[l-x-1]:
            return False
    return True

def msg(a,w):
    if a:
        print("La palabra",w, "es palíndroma.")
    else:
        print("La palabra",w, "no es palíndroma.")

def initial_msg():
    print("Buen día, ingrese una palabra y le diré si es palíndroma o no.")

def final_msg():
    print("Programa finalizado, hasta pronto.")

#Se une todo en el main
def main():
    initial_msg()
    w=ask_str("Ingrese la palabra a continuación: ")
    cond=check_word(w)
    msg(cond, w)
    final_msg()
main()
