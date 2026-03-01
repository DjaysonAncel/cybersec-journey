def port_to_service(port):
    services = {22: 'SSH', 80: 'HTTP', 443: 'HTTPS', 21: 'FTP', 53: 'DNS'}
    return services.get(port, 'Service inconnu')

port = int(input('Port : '))
print(f'Port {port} → {port_to_service(port)}')