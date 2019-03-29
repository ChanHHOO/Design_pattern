import telegram

import os
import sys
class Chat_Bot:
    def __init__(self, latest):

        self.bot = telegram.Bot(token='816156203:AAHkomYOGpusDAgOshG1oc_7guQXAI71wWY')
        self.chat_id = self.bot.getUpdates()[-1].message.chat.id
        self.latest = latest
    def New_content(self):
        self.bot.sendMessage(chat_id=self.chat_id, text="새 글이 왔다.")
        with open(os.path.join('/home/chanho/pysrc/myweb/home/', 'latest.txt'), 'w+') as f_write:
            f_write.write(self.latest)
            f_write.close()

    def No_new(self):
        self.bot.sendMessage(chat_id=self.chat_id, text="없다")

    # header = Req.headers
    # status = Req.status_code