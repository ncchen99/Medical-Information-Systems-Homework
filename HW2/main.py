import requests
import json
import yaml
from pprint import pprint

def request(sent, token):
    res = requests.post("http://140.116.245.157:2001", data={"data":sent, "token":token})
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        return None 

with open('entity.yaml', 'r') as file:
    ner_entity_map = yaml.safe_load(file)

# Go 'WMMKS API' website to get your token, and put it in secret.yaml
with open('secret.yaml', 'r') as file:
    token = yaml.safe_load(file)["token"]

if __name__ == "__main__":
    sent = """傅達仁今將執行安樂死，卻突然爆出自己20年前遭緯來體育台封殺，他不懂自己哪裡得罪到電視台。
美國參議院針對今天總統布什所提名的勞工部長趙小蘭展開認可聽證會，預料她將會很順利通過參議院支持，成為該國有史以來第一位的華裔女性內閣成員。"""
    r = request(sent, token)
    for item in r["ner"][0]:
        print(ner_entity_map[item[2]],":", item[3])
