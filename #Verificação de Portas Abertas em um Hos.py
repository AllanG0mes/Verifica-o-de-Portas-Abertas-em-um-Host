#Verificação de Portas Abertas em um Host:
import socket

def verifica_porta(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host, porta))
    sock.close()
    if resultado == 0:
        print(f'A porta {porta} em {host} está aberta')
    else:
        print(f'A porta {porta} em {host} está fechada')

if __name__ == "__main__":
    host_alvo = '127.0.0.1'  # Substitua pelo host que deseja verificar
    portas_alvo = [80, 443, 22, 3389]  # Lista de portas que deseja verificar
    for porta in portas_alvo:
        verifica_porta(host_alvo, porta)
