# 네이버(구글) 웹페이지 긁어오기2

#pip --version
 #pip 22.0.4 from C:\DEV\Langs\Python\Python39\lib\site-packages\pip (python 3.9)
#pip install requests

import requests as req

res = req.get('https://www.goole.com')
#print(res.status_code)
print(res._content)