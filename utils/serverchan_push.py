
import config
import requests


def push_to_wechat(title,desp,secretKey):
    """
    通过serverchan将消息推送到微信
    :param secretKey: severchan secretKey
    :param text: 标题
    :param desp: 内容
    :return resp: json
    """
    url = f'http://sctapi.ftqq.com/{secretKey}.send'
    session = requests.Session()
    data = {'title':title,'desp':desp}
    resp = session.post(url,data = data)
    return resp.json()


if __name__ == '__main__':
    resp = push_to_wechat(title = 'test', desp='hi', secretKey= config.SERVERCHAN_SECRETKEY)
    print(resp)
