"""
This script displays the blink login credentials
"""

from mitmproxy import http, ctx
import json

def response(flow: http.HTTPFlow) -> None:
    if "rest-prod.immedia-semi.com" in flow.request.pretty_host:
        if ('login' in flow.request.url):
            data = json.loads(flow.request.content)
            password=data['password']
            email=data['email']
            ctx.log.alert("[Blink] <login> account:%s, password:%s" %(email,password))
