import time
import requests

BACKEND_ADDRESS = 'backend-app-name'
BACKEND_PORT = '8800'
BACKEND_API = f'http://{BACKEND_ADDRESS}:{BACKEND_PORT}'

print(BACKEND_API)

def main():
    while True:
        global_cnt = requests.get(f'{BACKEND_API}/get_global_cnt').text
        print(f'Current global_cnt is {global_cnt}')
        time.sleep(1)

if __name__ == '__main__':
    time.sleep(5)
    main()
