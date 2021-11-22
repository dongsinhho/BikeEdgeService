import websocket
import json, sys

global mode
mode = False
id = sys.argv[2]
URL_socket = "ws://{}/ws/edge/".format(sys.argv[1])

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
