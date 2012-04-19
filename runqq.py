# coding: utf-8
from qqweibo import APIClient
qq = APIClient("app_key", "app_secret", redirect_uri="callback_uri")
qq.set_access_token("access_token", "openid", "expire")
#print qq.post.t__add(content="test", clientip="202.22.251.18")
print qq.post.t__add_pic_url(content="test", clientip="real ip", pic_url="pic url")
