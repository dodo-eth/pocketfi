import time
import csv
import requests   

def claim_request(url, token, proxy):
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.9,ru-RU;q=0.8,ru;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Origin': 'https://pocketfi.app',
        'Referer': 'https://pocketfi.app/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'telegramRawData': token
    }
    
    proxies = {
        'http': proxy,
        'https': proxy
    }
    
    response = requests.post(url, headers=headers, proxies=proxies)
    return response
    
def read_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) == 3:  # Проверяем, что строка содержит 3 поля
                entry = {
                    'discription': row[0],
                    'proxy': row[1],
                    'token': row[2]
                }
                data.append(entry)
    return data
 

def claim_function(file_path):
    while True:
        data = read_csv(file_path)
        for entry in data:
            claim_request("https://bot.pocketfi.org/mining/claimMining", entry['token'], entry['proxy'])
            print(entry['discription'] + " claim function отработал")
        time.sleep(2 * 60 * 60)  # Спим 2 часа (2 * 60 минут * 60 секунд)
 
 
if __name__ == '__main__':
    file_path = 'file.csv'
    
    # Запуск функции синхронизации в отдельном потоке
    
    claim_function(file_path) 


 