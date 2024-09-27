pal = input('Palabra?: ')
let = input('Letra?: ')

def count(palabra,letra):
    total = 0
    for char in palabra:
        if char == letra:
            total +=1
    return print(palabra + ' tiene ' + str(total) + ' letras ' + letra) 

count(pal,let)