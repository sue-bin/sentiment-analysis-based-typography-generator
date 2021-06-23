#!/usr/bin/env python
# coding: utf-8

# In[39]:


import os
import sys
import urllib.request
import json
import pandas as pd
from pprint import pprint

### 한글 텍스트를 영어로 번역 ###
    
def ko_papago(text):
    
    client_id = "9UZOb1Zhe1izICETvRxm" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "D8ubKWBCHF" # 개발자센터에서 발급받은 Client Secret 값
    
    encText = urllib.parse.quote(text)
    data = "source=ko&target=en&text=" + encText
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        res = json.loads(response_body.decode('utf-8'))
        text = res['message']['result']['translatedText']
        
        return text         
              
    else:
        print("Error Code:" + rescode)

