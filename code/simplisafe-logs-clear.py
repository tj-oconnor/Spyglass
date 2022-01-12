"""
This script clears the logs of SimpliSafe devices
"""
from mitmproxy import http, ctx
import json


def response(flow: http.HTTPFlow) -> None:
    if "api.simplisafe.com" in flow.request.pretty_host and "events?" in flow.request.url:
       data = json.loads(flow.response.content)
       data['events']=[]
       data['numEvents']='0'
       flow.response.content = bytes(json.dumps(data), 'utf-8')
       ctx.log.alert("[SimpliSafe] Cleared Logs")
