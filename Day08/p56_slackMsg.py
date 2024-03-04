# file : p56_slackMsg.py
# desc : slcak으로 스마트폰 메시지 보내기

'''
순서
1. https://api.slack.com/ 에서 Your app > Create your first app
2. From Scratch 클릭 - 앱 이름은 영어로만
3. Workspace 선택
4. Incoming webhooks > on > Add new webhook to Workspace 클릭 > 채널 선택 > 허용
'''


# 'https://hooks.slack.com/yourSlackUrl'

import requests
import json

slack_url = 'https://hooks.slack.com/yourSlackUrl' # 깃헙 업로드 전 삭제 필요

headers = {'Content-type':'application/jason'}
data = {'text':'안녕하세요, Slack'}

res = requests.post(slack_url, headers= headers, data= json.dumps(data))
if res.status_code == 200:
    print('메시지 전송 성공')
else:
    print('메시지 전송 실패')