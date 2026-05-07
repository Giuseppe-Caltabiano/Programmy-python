import ipaddress
import random
import time
from collections import deque

def ip_to_int(ip_str):
    return int(ipaddress.ip_address(ip_str))

def int_to_ip(ip_int):
    return str(ipaddress.ip_address(ip_int))

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root is not None
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

base_ip = int(ipaddress.ip_address("192.168.0.0"))
blacklist_integers = list(set([base_ip + random.randint(0, 65535) for _ in range(1000)]))

root = None
for ip_int in blacklist_integers:
    root = insert(root, ip_int)

blacklist_samples = random.sample(blacklist_integers, 10)
nuovi_ip = []
while len(nuovi_ip) < 10:
    temp_ip = base_ip + random.randint(0, 65535)
    if temp_ip not in blacklist_integers:
        nuovi_ip.append(temp_ip)

traffic_ips = blacklist_samples + nuovi_ip
random.shuffle(traffic_ips)

packet_queue = deque()
for ip in traffic_ips:
    packet = {
        "ip_sorgente": int_to_ip(ip),
        "ip_destinazione": "10.0.0.1",
        "porta_sorgente": random.randint(49152, 65535),
        "porta_destinazione": 80,
        "protocollo": "TCP",
        "dimensione": 1500
    }
    packet_queue.append(packet)

print(f"{'IP SORGENTE':<18} | {'STATO':<10}")
print("-" * 32)

bloccati = 0
permessi = 0

while packet_queue:
    p = packet_queue.popleft()
    ip_int = ip_to_int(p["ip_sorgente"])
    
    if search(root, ip_int):
        status = "BLOCCATO"
        bloccati += 1
    else:
        status = "PERMESSO"
        permessi += 1
    
    print(f"{p['ip_sorgente']:<18} | {status}")

print("\n--- RIEPILOGO FINALE ---")
print(f"Pacchetti bloccati: {bloccati}")
print(f"Pacchetti permessi: {permessi}")

test_ips = [base_ip + random.randint(0, 65535) for _ in range(10000)]

start_bst = time.perf_counter()
for tip in test_ips:
    search(root, tip)
end_bst = time.perf_counter()
time_bst = end_bst - start_bst

start_list = time.perf_counter()
for tip in test_ips:
    _ = tip in blacklist_integers
end_list = time.perf_counter()
time_list = end_list - start_list

print(f"\n--- PERFORMANCE ---")
print(f"Tempo BST: {time_bst:.6f}s")
print(f"Tempo Lista: {time_list:.6f}s")

if time_bst < time_list:
    ratio = time_list / time_bst
    print(f"Il BST è {ratio:.2f} volte più veloce della lista.")