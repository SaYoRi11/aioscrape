from aioscrape.utils import request

async def get_guest_token(session, authorization_token):
    authorize_url = 'https://api.twitter.com/1.1/guest/activate.json'

    headers = {
        'authorization': authorization_token,       
    }

    resp = await request(authorize_url, session, method="POST", headers=headers)
    data = await resp.json()
    return data['guest_token']