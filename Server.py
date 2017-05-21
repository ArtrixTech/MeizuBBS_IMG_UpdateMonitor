from flask import Flask
import os
import sys
import PIL.Image as Image
import Fuctions
import os.path
import threading

app = Flask(__name__)


@app.route('/')
def api_post():

    t = "<html> <body>"

    with open("new_img", mode="r")as file:
        for line in file.readlines():

            file = Image.open(Fuctions.get_file_name(line))
            width, height = file.size
            width = str(width * 0.2)
            height = str(height * 0.2)

            t += "<p><img src=\"" + line + "\"" + " width=\"" + \
                width + "\" height=\"" + height + "\"></p>"

    t += "</body></html>"
    return t


def no_use(rootdir):
    rootdir = os.path.split(os.path.realpath(sys.argv[0]))[0]
    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for parent, dirnames, filenames in os.walk(rootdir):

        for filename in filenames:  # 输出文件信息
            if ".jpg" in filename or ".png" in filename or ".bmp" in filename:
                pass


def start():
    app.run(port="5500", host="172.18.204.140")
    # app.run(port="5500", host="192.168.1.251")

t = threading.Thread(target=start)
t.start()
