from scapy.all import IP, ICMP, sr1
import os
import socket



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()


print("---[ Network Scanner ]---")
print("")
print("1. Descubrir Hosts")
print("2. Escanear Puertos")
print("3. Escanear rango de puertos")
print("")
InputOption = input(">> ")

if InputOption == "1":
    os.system('cls' if os.name == 'nt' else 'clear')

elif InputOption == "2":
    os.system('cls' if os.name == 'nt' else 'clear')

elif InputOption == "3":
    os.system('cls' if os.name == 'nt' else 'clear')


else:
    print("Xd")




resp = sr1(IP(dst="8.8.8.8")/ICMP(), timeout=2)

if resp:
    print("¡Respuesta recibida!")
else:
    print("No hubo respuesta")