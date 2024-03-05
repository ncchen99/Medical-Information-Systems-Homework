# 作業二 

將 token 填入範例城市

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

之後使用 `https://github.com/ckiplab/ckiptagger/wiki/Entity-Types` 提供之表格產生 `entity.yaml` 用來對應 NER 之條目！

小量修改程式後完成~