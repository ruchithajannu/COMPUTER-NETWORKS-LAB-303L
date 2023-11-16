#AP21110010140 
import scapy.all as scapy

def traceroute(destination, max_hops=30):
    for ttl in range(1, max_hops + 1):
        # Create an ICMP packet with the specified TTL
        packet = scapy.IP(dst=destination, ttl=ttl) / scapy.ICMP()

        # Send the packet and wait for a response
        reply = scapy.sr1(packet, verbose=False, timeout=1)

        if reply is None:
            # No response received, print an asterisk (*)
            print(f"{ttl}\t*")
        else:
            # Response received, print the IP address of the responding host
            print(f"{ttl}\t{reply.src}")

            # Check if the destination is reached
            if reply.src == destination:
                break

if __name__ == "__main__":
    # Get destination IP address from the user
    destination = input("Enter the destination IP address: ")

    # Perform traceroute
    traceroute(destination)
