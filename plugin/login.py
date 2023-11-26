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
    # status=data.get('data',{}).get('code',{})
    # message=data.get('data',{}).get('message',{})
    # token=data.get('data',{}).get('token',{})
    return data,response
def save_cookie():
    value={}
    with open('cookie.txt', 'r') as cookie_file:
        data = cookie_file.read()
        pairs=data.split()
        for i in pairs:
            k ,v=i.split('=')
            value[k]=v
    return value
def mainloop():
    qrcode_url,qrcode_key=login()
    sqrcode(qrcode_url)
    print(qrcode_key)
    print('等待10s')
    time.sleep(10)
    data,resposen=check(qrcode_key)
    code=data.get('data',{}).get('code',{})
    message=data.get('data',{}).get('message',{})
    if code==0:
        print('登录成功')
        with open('cookie.txt', 'w') as cookie_file:
            cookie_file.write('\n'.join([f"{name}={value}" for name, value in resposen.cookies.items()]))
        print('cookie.txt文件已生成')
    else:
        print(message)
if '__name__'=='__main__':
    mainloop()
