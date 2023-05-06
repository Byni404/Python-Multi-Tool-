import socket

def ping_ip(ip_address):
    response = os.system("ping -c 1 " + ip_address)
    if response == 0:
        print(ip_address, 'is up!')
    else:
        print(ip_address, 'is down!')

def lookup_ip(domain_name):
    ip_address = socket.gethostbyname(domain_name)
    print('IP address of', domain_name, 'is', ip_address)

def main():
    while True:
        print('1. Ping IP address')
        print('2. Lookup IP address')
        print('3. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            ip_address = input('Enter IP address to ping: ')
            ping_ip(ip_address)
        elif choice == '2':
            domain_name = input('Enter domain name to lookup: ')
            lookup_ip(domain_name)
        elif choice == '3':
            print('Exiting...')
            break
        else:
            print('Invalid choice!')
        
if __name__ == '__main__':
    main()