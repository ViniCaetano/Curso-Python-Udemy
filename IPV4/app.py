from Classes.calc_ipv4 import CalcIPv4

calc_ipv4 = CalcIPv4(ip = '192.168.0.1', prefixo = 24)
print(calc_ipv4.ip)
print(calc_ipv4.mascara)
print(calc_ipv4.rede)
print(calc_ipv4.broadcast)
print(calc_ipv4.prefixo)
print(calc_ipv4.numero_ips)