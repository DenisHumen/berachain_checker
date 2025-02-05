import requests
import csv
from tqdm import tqdm

def read_lines_from_file(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

def send_request(wallet, proxy):
    url = 'https://bera-checker-staging.vercel.app/api/balance'
    headers = {
        'accept': '*/*',
        'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://bera-checker-staging.vercel.app',
        'priority': 'u=1, i',
        'referer': 'https://bera-checker-staging.vercel.app/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    data = {
        'addresses': [wallet]
    }
    try:
        response = requests.post(url, headers=headers, proxies=proxies, json=data)
        response_data = response.json()
        
        # Debugging information
        #print(f"Request data: {data}")
        #print(f"Response status code: {response.status_code}")
        #print(f"Response data: {response_data}")
        
        if response_data and 'results' in response_data and response_data['results']:
            return response_data['results'][0].get('balance', 'N/A')
    except requests.RequestException as e:
        print(f"Request failed with proxy {proxy}: {e}")
    return None

def main():
    print(r"""
______           _       _   _                            
|  _  \         (_)     | | | |                           
| | | |___ _ __  _ ___  | |_| |_   _ _ __ ___   ___ _ __  
| | | / _ \ '_ \| / __| |  _  | | | | '_ ` _ \ / _ \ '_ \ 
| |/ /  __/ | | | \__ \ | | | | |_| | | | | | |  __/ | | |
|___/ \___|_| |_|_|___/ \_| |_/\__,_|_| |_| |_|\___|_| |_|
                                                          
            
    """)
    print('\033[94mDONATION TRC-20 -- TRWzXZE16bgJg3eHa9n8q4ioZjMgKHwF9a\033[0m')
    print('\033[94mDenis Humen\033[0m')
    print('\033[94mhttps://github.com/DenisHumen\033[0m', '\n')

    wallets = read_lines_from_file('walletss.txt')
    proxies = read_lines_from_file('proxy.txt')
    proxy_index = 0
    
    with open('result.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['address', 'value'])
        
        for wallet in tqdm(wallets, desc="Processing wallets", colour='green'):
            value = None
            while value is None:
                proxy = proxies[proxy_index]
                value = send_request(wallet, proxy)
                proxy_index = (proxy_index + 1) % len(proxies)
            csvwriter.writerow([wallet, value])

if __name__ == "__main__":
    main()
