
def create_phone_number(n):
    cero = n[0]
    uno = n[1]
    dos = n[2]
    tres = n[3]
    cuatro = n[4]
    cinco = n[5]
    seis = n[6]
    siete = n[7]
    ocho = n[8]
    nueve = n[9]    
    concatenate = f"({cero}{uno}{dos}) {tres}{cuatro}{cinco}-{seis}{siete}{ocho}{nueve}"
    print(concatenate)

create_phone_number([1,2,3,4,5,6,7,8,9,0])