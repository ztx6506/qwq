import sys,requests
number = int(sys.argv[1])
result = number *12
bark = requests.post(f'https://api.day.app/KR76KmKwtPtjnwy8rCqnd8/{result}?group=bilibili')
print(result)