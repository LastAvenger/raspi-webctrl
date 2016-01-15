#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

from os import system
from flask import Flask, request, render_template

app = Flask(__name__)

cmd = {
  #     '关机': 'poweroff',
  #     '重启': 'reboot',
        '重启 MentoHUST': 'systemctl restart mentohust',
        }

@app.route('/', methods=['GET'])
def index():
    action = request.args.get('action')
    if action:
        system(cmd[action])
        return render_template('index.html', message = '即将 ' + action)
    else:
        return render_template('index.html', message = 'Raspi WebCtrl')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
