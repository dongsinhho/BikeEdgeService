import websocket
import json

global mode
mode = False
id = 16
URL_socket = "ws://172.17.0.1:8000/ws/edge/"

def on_message(ws, message):   #nhận dữ liệu từ websocket báo là khoá xe đã đóng thì thay đổi chế độ
    messages = json.loads(message)
    for item in messages:
        if int(item['id']) == id:
            if item['mode'] != mode:
                mode != mode
                print('Mo khoa/dong khoa')


def on_open(ws):
    print("### opened ###")


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(URL_socket,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                on_open=on_open)
    ws.run_forever()