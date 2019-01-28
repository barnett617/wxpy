# -*- coding: utf-8 -*-
import oss2
import os
from conf import oss_appid, oss_appkey, oss_endpoint, oss_bucket, oss_addr

def uploadPictureToOSS(obj, file_name):
    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth(oss_appid, oss_appkey)
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, oss_endpoint, oss_bucket)

    bucket.put_object(file_name, obj)

    file_url = str(oss_addr) + str(file_name)

    return file_url

