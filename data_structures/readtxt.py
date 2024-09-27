# falta completar:


texto_lin = open('sprint.txt')

#texto_car = texto_lin.read()
#print(len(texto_car))
#for car in texto_car:
 #   print(car)


for linea in texto_lin:
#    print(linea)

    if linea.endswith('.\n'):
        print('no cambia:',linea)
        continue
    elif linea.endswith('\n'):
            linea = linea[:-1]
            print('cambia: ',linea) 
            
            
           # open('sprint.txt','w')   ojo!!! borra todo
            #print(linea[:-1])
    #        texto = open('sprint.txt','w')
    #        linea = linea.replace('\n', ' ')
    #        print(linea, ' cambia') 
#for linea in texto:
 #   print(linea)