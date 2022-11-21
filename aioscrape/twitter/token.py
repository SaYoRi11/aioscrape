from aioscrape.utils import request
import os

async def get_guest_token(session, authorization_token, new = False):
    gt_path = 'aioscrape/twitter/gt'
    if new or not os.path.exists(gt_path):
        gt = await request_token(session, authorization_token)

        with open('aioscrape/twitter/gt', 'w+') as f:
            f.write(gt)
        return gt
    
    with open('aioscrape/twitter/gt') as f:
        gt = f.read()
    return gt


async def request_token(session, authorization_token):
    authorize_url = 'https://api.twitter.com/1.1/guest/activate.json'
    headers = {
        'authorization': authorization_token,       
    }

    resp = await request(authorize_url, session, method="POST", headers=headers)
    data = await resp.json()
    return data['guest_token']