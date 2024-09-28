print ('hello world')
try:
    a = input('edad?: ')
    a= int(a)
    if a <= 0:
        print('todavía no naciste')
    elif a < 120:
        print('tienes', a)
    else:
        print('ningún ser humano vive tanto')
except: 
    print('un número por favor')
