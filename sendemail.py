import requests

import smtplib

url = 'https://www.amazon.in/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-F3-5-5-6/dp/B07B45D8WV/ref=sr_1_1?keywords=sony+a7&qid=1570217594&s=beauty&sr=8-1'

headers = {"User-Agent":
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('bangalorelocation@gmail.com', 'qqoytuorsqscbhwk')
subject = 'Python email'
body = 'testing'
msg = f"Subject:{subject}\n\n{body}"
server.sendmail(
    'bangalorelocation@gmail.com',
    'ravi.kc@dxc.com',
    msg

)

print('email sent')

server.quit()
