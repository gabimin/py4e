""" 
Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
"""

import socket

def parse_url(url):
    # Remove the protocol (http:// or https://) if present
    if url.startswith('http://'):
        url = url[7:]
    elif url.startswith('https://'):
        url = url[8:]
    
    # Split the remaining string into host and path
    parts = url.split('/', 1)
    host = parts[0]
    path = '/' + parts[1] if len(parts) > 1 else '/'
    
    return host, path

def get_web_page(url):
    try:
        # Parse the URL
        host, path = parse_url(url)

        # Create a socket
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))

        # Send the GET request
        cmd = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode()
        mysock.send(cmd)

        # Receive and print the response
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(), end='')

        mysock.close()

    except socket.gaierror:
        print("Error: Invalid hostname. Please check the URL and try again.")
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Prompt the user for the URL
url = input("Enter the URL you want to retrieve: ")

# Call the function to get and display the web page
get_web_page(url)