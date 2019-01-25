# coding: utf-8
from wxpy import *
from dao import insert_msg
import sys

bot = Bot()

print(sys.version)

'''
TODO:
1. 对文本类型消息进行处理（回复）
2. 消息记录存储
'''

# 发送的消息文本

my_msg = '我来啦，哈哈哈'

# 获取某个好友
friend_rouding = bot.friends().search('肉丁')[0]

# 从所有消息中检索某个人发送的内容
# msgFromFriendTom = bot.messages.search(sender=bot.friends().search('Tom')[0])[0]
# msgFromGroup = bot.messages.search(sender=bot.groups().search('C0deM0nkeys')[0])[0]

# 查询某个好友并发送文本消息
# bot.friends().search('肉丁')[0].send('哈哈哈')

# 检索历史信息
# bot.messages.search(sender=group_pika)

# 定位某个群
group_cm = ensure_one(bot.groups().search('C0deM0nkeys'))
# group_cm.send('什么是领域模型@Tom')

def msgRefMe(msg):
    if (msg.find('鑫锅') > 0 or msg.find('王鑫') > 0 or msg.find('鑫哥') > 0):
        return True
    return False

# 注册监听所有消息
@bot.register(except_self=False)
def just_print(msg):
    print(msg)
    if msg.member == None:
        # 非群聊
        insert_msg(msg.text, msg.type, msg.sender.name, msg.sender.name)
        # print(msg)
    else:
        # 群聊
        insert_msg(msg.text, msg.type, msg.member.name, msg.sender.name)
        # print(msg)
        if msgRefMe(msg):
            return '嗯？怎么了'
        group_cm = ensure_one(bot.groups().search('C0deM0nkeys'))
        yanghua = ensure_one(group_cm.search('杨华'))
        liaoze = ensure_one(group_cm.search('廖泽'))
        if msg.member == yanghua:
            return '华仔说活了[奸笑]'
            # return '华仔来啦'
        elif msg.member == liaoze:
            return '泽神说话了[奸笑]'

# try:
#     # 尝试向某个群员发送消息
#     # group.members[3].send('Hello')
#     bot.groups().search('C0deM0nkeys')[0].send(my_msg)
# except ResponseError as e:
#     # 若群员还不是好友，将抛出 ResponseError 错误
#     print(e.err_code, e.err_msg) # 查看错误号和错误消息

# 可在堵塞线程的同时，进入 Python 命令行，方便调试，一举两得
embed()