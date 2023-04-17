"""
Name: aliy_signin.py
Description: Automatically sign in aliyundrive.
Author: hdaojin
Date: 2023.03.27
Update: 2023.03.27
Version: 0.0.1
"""

from aligo import Aligo

class CAligo(Aligo):
    def sign_in_list(self):
        return self._post('/v1/activity/sign_in_list', host='https://member.aliyundrive.com', body={})
    
if __name__=='__main__':
    ali = CAligo()
    r = ali.sign_in_list()
    result = r.json()['result']
    signInCount = result['signInCount']
    signInLog = next(filter(lambda i: i['day'] == signInCount, result['signInLogs']), None)
    if signInLog:
        if signInLog['reward'] is None:
            print("本月签到次数:" + str(signInCount) + ",今日签到无奖励")
        else:
            print("本月签到次数:" + str(signInCount) + ",今日签到奖励:" + signInLog['reward']['name'] +
                  signInLog['reward']['description'])
    else:
        print("签到失败")