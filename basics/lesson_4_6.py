horas = float(input('Horas: '))
tarifa = float(input('Tarifa: '))

def computepay(h,r):
    if h > 40:
        h = 40 + (h-40) * 1.5
    return h * r

print('Pay', computepay(horas, tarifa))