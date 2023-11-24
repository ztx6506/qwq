import requests,time,qrcode
from PIL import Image
def login():
    sq='https://passport.bilibili.com/x/passport-login/web/qrcode/generate'
    r=requests.get(sq)
    data = r.json()
    qrcode_key = data.get('data', {}).get('qrcode_key', '')
    qrcode_url = data.get('data', {}).get('url', '')
    return qrcode_url,qrcode_key


def sqrcode(url):
    # 生成二维码
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')
    img.show()
def check(qrcode_key):
    check_url='https://passport.bilibili.com/x/passport-login/web/qrcode/poll'
    check_key={'qrcode_key':qrcode_key}
    response=requests.get(check_url,check_key)
    data=response.json()
    status=data.get('data',{}).get('code',{})
    message=data.get('data',{}).get('message',{})
    return status,message,response
def mainloop():
    qrcode_url,qrcode_key=login()
    sqrcode(qrcode_url)
    print(qrcode_key)
    print('等待10s')
    time.sleep(10)
    code,message,res=check(qrcode_key)
    if code==0:
        print('登录成功')
        with open('cookie.txt', 'w') as cookie_file:
            cookie_file.write('\n'.join([f"{name}={value}" for name, value in res.cookies.items()]))
    else:
        print(message)
mainloop()