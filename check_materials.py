import requests

WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=92f0e410-c0a6-4127-8f1b-b1d949e304c6"

def send_message():
    data = {
        "msgtype": "text",
        "text": {
            "content": "📦 物料检查进行时，盘点库存进行记录"
        }
    }
    response = requests.post(WEBHOOK_URL, json=data)
    print(response.text)

if __name__ == "__main__":
    send_message()
