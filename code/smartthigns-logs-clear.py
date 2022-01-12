"""
This script clears the logs of SmartThings devices
"""
from mitmproxy import http, ctx

def request(flow: http.HTTPFlow) -> None:
    if "api.smartthings.com" in flow.request.pretty_host:
         if "limit" in flow.request.query:
             flow.request.query['limit']='0'
             ctx.log.alert("[Smartthings] <cleared logs>")         

