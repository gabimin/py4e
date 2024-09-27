import urllib.request

try:
    with urllib.request.urlopen('http://data.pr4e.org/romeo.txt') as fhand:
        for line in fhand:
            print(line.decode('utf-8').strip())
except urllib.error.URLError as e:
    print(f"Error al acceder a la URL: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")