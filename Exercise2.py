from machine import Pin
from time import sleep 
import socket


p4 = Pin(14, Pin.OUT)
p4.value(True)


relay = Pin(5, Pin.OUT)

def web_page():
  if relay.value() == 1:
    relay_state="ON"
  else:
    relay_state="OFF"
  
  html = """
    <html>
        <head><title>IoT Exercise 2</title></head>
        <body style="margin-top: 500px;"><center>
            <h1><b>LED state: """ + relay_state + """</b></h1>
            <a href="/?relay=on"><button>ON</button></a>
            <a href="/?relay=off"><button style="background-color: red;">OFF</button></a>
        </center></body>
        <style>
        button {
            height: 100px; width: 200px; background-color: green; font-size: 40px; color: white;
        }
        h1 { font-size: 35px; }
        </style>
    </html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  request = conn.recv(1024)
  request = str(request)
  led_on = request.find('/?relay=on')
  led_off = request.find('/?relay=off')
  if led_on == 6:
    relay.value(True)
  if led_off == 6:
    relay.value(False)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
