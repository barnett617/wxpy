# coding: utf-8
from wxpy import *
from dao import insert_msg, getDBConnection
from util import uploadPictureToOSS
from wxpy import get_wechat_logger
import local_enum
import sys

bot = Bot()

print(sys.version)

# 找到需要接收日志的群 -- `ensure_one()` 用于确保找到的结果是唯一的，避免发错地方
log_receiver = ensure_one(bot.friends().search('Tom'))

# 获得一个专用 Logger
# 当不设置 `receiver` 时，会将日志发送到随后扫码登陆的微信的"文件传输助手"
logger = get_wechat_logger(log_receiver)

# 发送警告
logger.warning('程序启动，这是一条 WARNING 等级的日志，你收到了吗？')

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
    ref_me = False
    for item in local_enum.keyword['about_me']:
        if (msg.find(item)):
            ref_me = True
    return ref_me

# 注册监听所有消息
@bot.register(except_self=False)
def just_print(msg):
    print(msg)
    send_text = ''
    text_msg = False
    try:
        # 过滤空消息或非文本消息
        if msg.text is not None:
            send_text = msg.text
            text_msg = True
        # 获取数据库连接
        getDBConnection()
        # 判断消息来源（个人消息 or 群聊消息）
        if msg.member == None:
            # 非群聊
            insert_msg(send_text, msg.type, msg.sender.name, msg.sender.name, msg.create_time, msg.receive_time)
        else:
            # 群聊

            if msg.type == 'Picture':
                picture_obj = msg.get_file(save_path=None)
                file_url = uploadPictureToOSS(picture_obj, msg.file_name)
                send_text = file_url

            insert_msg(send_text, msg.type, msg.member.name, msg.sender.name, msg.create_time, msg.receive_time)

            # 获取对象
            group_cm = ensure_one(bot.groups().search(local_enum.group['cm']))
            pika_cm = ensure_one(bot.groups().search(local_enum.group['pika']))
            yanghua = ensure_one(group_cm.search(local_enum.user['yanghua']))
            liaoze = ensure_one(group_cm.search(local_enum.user['liaoze']))

            # 开始对文本进行解析处理（建立在消息是文本类型的基础上）
            if text_msg:
                if msgRefMe(send_text):
                    # return local_enum.my_reply['whatsup']
                    pass

            # 对指定成员的消息进行处理
            if msg.member.name == yanghua:
                return local_enum.my_reply['yhcome']
            elif msg.member.name == liaoze:
                return local_enum.my_reply['lzcome']

    except ResponseError as res_error:
        logger.exception('现在你又收到了什么？')
        print(res_error.err_code, res_error.err_msg)  # 查看错误号和错误消息
    except Exception as e:
        logger.exception('现在你又收到了什么？')
        print('msg resolve error: ', e)

# 可在堵塞线程的同时，进入 Python 命令行，方便调试，一举两得
embed()