import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://DudeDudesir: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@github.com/DudeDudeSir/mogonewrepo okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
