import socket
import sys
import argparse
import threading
from queue import Queue
from datetime import datetime

ascii_banner = r"""
  _____           _    _____                
 |  __ \         | |  / ____|                
 | |__) |__  _ __| |_| (___   ___ __ _ _ __  
 |  ___/ _ \| '__| __|\___ \ / __/ _` | '_ \ 
 | |  | (_) | |  | |_ ____) | (_| (_| | | | |
 |_|   \___/|_|   \__|_____/ \___\__,_|_| |_|

                     Port Scanner - by Leandro                           
"""

print(ascii_banner)

print_lock = threading.Lock()

open_ports = []



def scan_port(host, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        result = client.connect_ex((host, port))
        if result == 0:
            with print_lock:
                info = "[+] Port {} open".format(port)
                print(info)
                open_ports.append(port)
        client.close()
    except:
        pass


def threader(host, q):
    while True:
        port = q.get()
        scan_port(host, port)
        q.task_done()


def parse_port_range(port_input):
    ports = set()
    for part in port_input.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-")
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))
    return sorted(ports)


def parse_args():
    parser = argparse.ArgumentParser(description="Multithreaded Port Scanner")
    parser.add_argument("host", help="Target host (e.g., google.com)")
    parser.add_argument(
        "-p", "--ports",
        help="Ports to scan, comma-separated or with range (e.g., 22,80,1000-1010)",
        default="21,22,23,25,80,443,445,8080,8443,3306,139,135"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file to save results",
        default=None
    )
    return parser.parse_args()


def main():
    args = parse_args()
    host = args.host
    ports = parse_port_range(args.ports)

    q = Queue()

    for _ in range(200):  # Pode ajustar o número de threads
        t = threading.Thread(target=threader, args=(host, q), daemon=True)
        t.start()

    for port in ports:
        q.put(port)

    q.join()

    if args.output:
        with open(args.output, "w") as f:
            f.write(f"Scan result for {host} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            for port in open_ports:
                f.write("Port {} open\n".format(port))
        print("\n[+] Results saved to {}".format(args.output))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrompido pelo usuário. Encerrando...\n")
        sys.exit(0)
