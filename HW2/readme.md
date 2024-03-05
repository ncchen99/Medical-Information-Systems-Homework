# 作業二 

```python=
import requests
import json

def request(sent, token):
    res = requests.post("http://140.116.245.157:2001", data={"data":sent, "token":token})
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        return None 


if __name__ == "__main__":
    token = "XXX" # Go 'WMMKS API' website to get your token
    sent = "今天的天氣很不錯"
    r = request(sent, token)
    print(r)
```