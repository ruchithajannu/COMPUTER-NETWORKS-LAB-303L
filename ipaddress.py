#AP21110010140
def get_ip_class(ip_address):
    first_octet = int(ip_address.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'Class A'
    elif 128 <= first_octet <= 191:
        return 'Class B'
    elif 192 <= first_octet <= 223:
        return 'Class C'
    elif 224 <= first_octet <= 239:
        return 'Class D'
    elif 240 <= first_octet <= 255:
        return 'Class E'
    else:
        return 'Invalid IP Address'

def generate_subnet(ip_address, subnet_bits):
    octets = ip_address.split('.')
    subnet_mask = [0, 0, 0, 0]

    for i in range(subnet_bits):
        subnet_mask[i // 8] += 2**(7 - (i % 8))

    subnet_ip = []
    for i in range(4):
        subnet_ip.append(int(octets[i]) & subnet_mask[i])

    return '.'.join(map(str, subnet_ip))


# Get IP address from the user
ip_address = input("Enter the IP address: ")

# Get subnet bits from the user
subnet_bits = int(input("Enter the number of subnet bits: "))

# Display IP class
ip_class = get_ip_class(ip_address)
print(f"IP Address Class: {ip_class}")

# Generate and display subnet IP
subnet_ip = generate_subnet(ip_address, subnet_bits)
print(f"Subnet IP Address: {subnet_ip}")
