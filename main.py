# Author: WebUwU (github.com/WebUwU)
import random
import string
import time
import httpx
import ctypes
import os
from pystyle import Colors, Colorate, Center

try:
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Author: WebUwU (github.com/WebUwU)")
except ImportError:
    pass  


def generate_keys(filename, num_keys, key_length):
    chars = string.ascii_lowercase + string.digits
    start = time.time()
    
    with open(filename, 'w') as f:
        for _ in range(num_keys):
            key = ''.join(random.choice(chars) for _ in range(key_length))
            f.write(key + '\n')
    
    elapsed = time.time() - start
    print(Colorate.Color(Colors.purple, f"[*] Generated {num_keys} keys in {elapsed:.2f} seconds", True))

class CapMonsterChecker:
    def __init__(self):
        with open("keys.txt", 'r') as f:
            self.keys = [line.strip() for line in f.readlines()]

    def Check(self):
        print(Colorate.Color(Colors.purple, f"[*] Starting checker with {len(self.keys)} keys...", True))
        for key in self.keys:
            try:
                resp = httpx.post(
                    "https://api.capmonster.cloud/getBalance",
                    headers={"Content-Type": "application/json"},
                    json={"clientKey": key},
                    timeout=10.0
                )
                if resp.status_code == 200:
                    data = resp.json()
                    balance = data.get('balance')
                    if balance is not None:
                        print(Colorate.Color(Colors.green, f"[+] Valid Key: {key} | Balance: {balance}", True))
                elif "ERROR_KEY_DOES_NOT_EXIST" in resp.text:
                    print(Colorate.Color(Colors.red, f"[-] Invalid Key: {key}", True))
                else:
                    print(Colorate.Color(Colors.red, f"[!] Error checking key: {key} | {resp.status_code} | {resp.text}", True))
            except Exception as e:
                print(Colorate.Color(Colors.red, f"[ERROR] Exception during request -> {e}", True))

if __name__ == "__main__":
    while True:
        ascii_art = r"""
        _______ __             __                               __                ________                       
       / ____(_) /__  ____  / /_  ____  ____ _      ______  / /_  ___  _____ / ____/ /___ _____ ___  ___  _____
      / /   / / / _ \/ __ \/ __ \/ __ \/ __ \ | /| / / __ \/ __ \/ _ \/ ___/ / /   / / __ `/ __ `__ \/ _ \/ ___/
     / /___/ / /  __/ / / / /_/ / /_/ / / / / |/ |/ / / / / /_/ /  __/ /    / /___/ / /_/ / / / / / /  __/ /    
     \____/_/_/\___/_/ /_/_.___/\____/_/ /_/|__/|__/_/ /_/_.___/\___/_/     \____/_/\__,_/_/ /_/ /_/\___/_/     
                                                                                                               
        """
        print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(ascii_art), 1))
        options = "[1] Generate keys\n[2] Check keys"
        print(Colorate.Color(Colors.blue, Center.XCenter(options), True))
        choice = input(Colorate.Color(Colors.blue, "Enter your choice: ", True))

        if choice == '1':
            generate_keys("keys.txt", 100000, 32)
        elif choice == '2':
            try:
                checker = CapMonsterChecker()
                checker.Check()
            except KeyboardInterrupt:
                os._exit(0)
        else:
            print(Colorate.Color(Colors.red, "Invalid choice.", True))
