import requests
import time
import random


def scan(dom, speed):
    if speed == 's':
        speed = [10,9,8,7]
    elif speed == 'm':
        speed = [2,5,4,3]
    elif speed == 'f':
        speed = [.3,.5,.8]
    output_file = dom + '_subs.txt'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
            }
    with open('subs.txt', 'r', encoding="utf-8") as file:
        for item in file:
            frequency = random.choice(speed)
            time.sleep(frequency)
            item = item.strip()
            item = 'https://' + item + '.' + dom
            print(item)
            try:
                r = requests.get(item, headers=headers)
                response = str(r)
                response = response.strip('<Response []>')
                print(response)
                with open(output_file, 'a', encoding="utf-8") as output:
                    output.write(f'\n{response} | {item}')
                    output.close()
            except:
                print('error')


if __name__ == "__main__":
    dom = input('Domain: https://')
    speed = input('How fast? S_low/M_edium/F_ast: ').lower()
    scan(dom, speed)
