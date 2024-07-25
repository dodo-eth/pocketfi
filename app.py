import time
import csv
import requests   
import logging
import os
from fake_useragent import UserAgent

# Настройка логирования
log_file_path = 'poketfi_service.log'
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()

logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s %(message)s')


def claim_request(url, token, proxy):
    fake_useragent = UserAgent()
    user_agent = fake_useragent.random
    
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
        'User-Agent': user_agent,
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
            try:
                url = "https://api.onetime.dog/rewards"
                response = claim_request("https://bot.pocketfi.org/mining/claimMining", entry['token'], entry['proxy'])                
                logging.info(f"{entry['discription']} claimMining function : {response.status_code}")
                response = claim_request("https://bot.pocketfi.org/boost/activateDailyBoost", entry['token'], entry['proxy'])
                logging.info(f"{entry['discription']} activateDailyBoost function : {response.status_code}")
            except Exception as e:
                logging.error(f"Error during claim request: {e}") 
        time.sleep(2 * 60 * 60)  # Спим 2 часа (2 * 60 минут * 60 секунд)
 
 
if __name__ == '__main__':
    file_path = 'file.csv'
    logging.info("Starting claim function")
    # Запуск функции синхронизации в отдельном потоке
    
    claim_function(file_path) 


 