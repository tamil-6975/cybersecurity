import socket

def scan_port(ip,port):
    try:
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       sock.settimeout(0.5)
       result = sock.connect_ex((ip,port))
       if result == 0:
           print(f"port{port}:OPEN")
       sock.close()
    except Exception as e:
        with open("errors.txt", "a") as log_file:
            log_file.write(f"Error scanning port {port}: {e}\n")

target = input("Enter target IP:")
for port in range(1,1025):
    scan_port(target,port)


