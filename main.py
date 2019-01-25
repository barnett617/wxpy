# coding: utf-8
from wxpy import *
from dao import insert_msg, getDBConnection
import local_enum
import sys

bot = Bot()

print(sys.version)

'''
TODO:
1. 对文本类型消息进行处理（回复）
2. 消息记录存储
'''

# 发送的消息文本

my_msg = local_enum.my_reply['test']
print(my_msg)

# 好友操作

# 获取某个好友
# 可通过获取数组第一个或使用ensure_one方法取数组中的唯一对象
# friend_rouding = bot.friends().search(local_enum.user['rouding'])[0]
# 对找到的唯一好友发送消息
# friend_rouding.send('哈哈哈[坏笑]')

# 查找的同时发送
# bot.friends().search(local_enum.user['rouding'])[0].send('哈哈哈')

# 从所有消息中检索某个人发送的内容
# msgFromFriendTom = bot.messages.search(sender=bot.friends().search('Tom')[0])[0]
# msgFromGroup = bot.messages.search(sender=bot.groups().search('C0deM0nkeys')[0])[0]

# 群操作

# 定位某个群
# group_cm = ensure_one(bot.groups().search(local_enum.group['cm']))
# 对群发消息
# group_cm.send('嘿嘿嘿@Tom')

def msgRefMe(msg):
    for item in local_enum.keyword['about_me']:
        if (msg.find(item)):
            return True
        return False

# 注册监听所有消息
@bot.register(except_self=False)
def just_print(msg):
    print(msg)
    send_text = ''
    try:
        # 过滤空消息或非文本消息
        if msg.text is not None:
            send_text = msg.text
        # 获取数据库连接
        getDBConnection()
        # 判断消息来源（个人消息 or 群聊消息）
        if msg.member == None:
            # 非群聊
            insert_msg(send_text, msg.type, msg.sender.name, msg.sender.name)
        else:
            # 群聊
            insert_msg(send_text, msg.type, msg.member.name, msg.sender.name)
            if msgRefMe(msg):
                return local_enum.my_reply['whatsup']
            group_cm = ensure_one(bot.groups().search(local_enum.group['cm']))
            pika_cm = ensure_one(bot.groups().search(local_enum.group['pika']))
            yanghua = ensure_one(group_cm.search(local_enum.user['yanghua']))
            liaoze = ensure_one(group_cm.search(local_enum.user['liaoze']))
            if msg.member.name == yanghua:
                return local_enum.my_reply['yhcome']
            elif msg.member.name == liaoze:
                return local_enum.my_reply['lzcome']
    except ResponseError as e:
        print(e.err_code, e.err_msg)  # 查看错误号和错误消息
    except Exception as e:
        print('msg resolve error: ', e)

# 可在堵塞线程的同时，进入 Python 命令行，方便调试，一举两得
embed()