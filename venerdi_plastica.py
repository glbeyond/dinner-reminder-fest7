import requests

WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b2dee511-fc19-4056-91de-16188d61c59d"

def send_message():
    data = {
        "msgtype": "text",
        "text": {
            "content": "周五下午到了，同志们，是时候整理下塑料垃圾了"
        }
    }
    response = requests.post(WEBHOOK_URL, json=data)
    print(response.text)

if __name__ == "__main__":
    send_message()
