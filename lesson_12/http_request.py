# importa el módulo socket, que proporciona una interfaz de bajo nivel para operaciones de red
import socket

# se crea un objeto socket
# AF_INET indica que usaremos IPv4
# SOCK_STREAM especifica que es un socket TCP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#establece una conexión con el servidor 'data.pr4e.org' en el puerto 80 (el puerto estándar para HTTP)
mysock.connect(('data.pr4e.org', 80))

# se construye la solicitud HTTP. Se codifica como bytes con .encode() porque los sockets transmiten datos en bytes, no en strings
# la combinación \r\n se usa para indicar el final de una línea en una solicitud o respuesta HTTP (estándar definido en las especificaciones HTTP)
# \r\n después de HTTP/1.1 marca el final de la línea de solicitud
# \r\n después de data.pr4e.org marca el final del encabezado Host
# los dos \r\n al final marcan el final de los encabezados y el inicio del cuerpo de la solicitud (que en este caso está vacío), esta secuencia es crucial para separar los encabezados del cuerpo de la solicitud o respuesta.
# el uso de \r\n en lugar de solo \n asegura que el mensaje HTTP sea compatible con diferentes sistemas operativos y servidores web, ya que algunos sistemas usan \r\n para los saltos de línea, mientras que otros usan solo \n
cmd = 'GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()

# envía la solicitud HTTP al servidor
mysock.send(cmd)

# este bucle se ejecutará continuamente hasta que se rompa explícitamente
while True:
    # recibe hasta 512 bytes de datos del servidor
    # la respuesta puede ser más grande, por eso se usa un bucle
    data = mysock.recv(512)
    # si no se reciben datos (longitud 0) la transmisión ha terminado así que salimos del bucle
    if len(data) < 1:
        break
    # decodifica los datos recibidos (de bytes a string) y los imprime
    print(data.decode())
# cierra la conexión del socket
mysock.close()


# Este código implementa un cliente HTTP básico utilizando sockets de bajo nivel, en lugar de usar bibliotecas de más alto nivel como requests o http.client. Es una buena manera de entender cómo funcionan las conexiones HTTP a un nivel más fundamental.
