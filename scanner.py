from scapy.all import IP, ICMP, sr1
import os
import socket


# OBTENER IP HOST
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()







'''  
# AÑADIR NODO ( X.X.X.X )
def SimpleNodeScan():

    
# AÑADIR MULTIPLES NODOS ( X.X.X.X/24 ) 
def NetworkNodeScan():
'''




InputedIP = input(">> ")


if "/" in InputedIP:
    DiscoverHosts(InputedIP)
else:
    #SimpleNodeScan(InputedIP)
    print(Ping(InputedIP))
    
    


def Ping(DestIP):
    ICMPRequest = IP(dst=DestIP) / ICMP()
    response = sr1(ICMPRequest, timeout=2, verbose=0)
    if response: 
        return True
    else: 
        return False




def DiscoverHosts(network):
    """Scans a network for active hosts using ICMP Echo Requests."""
    network_obj = ipaddress.ip_network(network)
    active_hosts = []

    for ip_address in network_obj.hosts(): # Iterate through all usable host IPs in the network
        ip_str = str(ip_address)
        icmp_request = IP(dst=ip_str) / ICMP()
        response = sr1(icmp_request, timeout=1, verbose=0)

        if response:
            active_hosts.append(ip_str)
            print(f"Host {ip_str} is up.")
        else:
            print(f"Host {ip_str} is down.")

    return active_hosts









print("---[ Network Scanner ]---")
print("")
print("1. Descubrir Hosts")
print("2. Escanear Puertos")
print("3. Escanear rango de puertos")
print("4. Trazar ruta a destino")
print("5. Is alive IP?")
print("")
InputOption = input(">> ")

if InputOption == "1":
    os.system('cls' if os.name == 'nt' else 'clear')


elif InputOption == "2":
    os.system('cls' if os.name == 'nt' else 'clear')

elif InputOption == "3":
    os.system('cls' if os.name == 'nt' else 'clear')

elif InputOption == "4":
    os.system('cls' if os.name == 'nt' else 'clear')


elif InputOption == "5":
    os.system('cls' if os.name == 'nt' else 'clear')
    DestIp = input("Introduce la ip del pc destino: ")

    if Ping(DestIp):
        print("¡Respuesta recibida!")
    else:
        print("No hubo respuesta")


else:
    print("Xd")



class Nodo():
    def __init__(self, id, hostname="", ip="", mac="", mask="255.255.255.255"):
        
        # [ DATOS NODOS ] 
        self.id = id
        self.hostname = hostname
        self.ip = ip
        self.mac = mac

        self.online = False
        self.mask = mask

        self.properties = {
            "os": None,
            "services": [],
            "latency": None
        }

        self.connections = [] 



        # [  NODOS ] 


    # [ Facil conversion a JSON ]
    def Data(self):
        return {
            "ID": self.id,
            "IP": self.ip,
            "Hostname": self.hostname,
            "MAC": self.mac,
            "Online": self.online,
            "Mask": self.mask,
            "OS": self.properties["os"],
            "Services": self.properties["services"],
            "Latency": self.properties["latency"],
        }

    

    def DrawNode():


        






def DisoverHosts():




def PortScan(NodoDestino):
if NodoDestino.online:
    print("Podemos escanear")
else:
    print("El equipo no esta disponible")






MiPC = Nodo()
print(MiPC.Data())

