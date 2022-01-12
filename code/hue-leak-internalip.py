from mitmproxy import http, ctx
import json

def response(flow: http.HTTPFlow) -> None:
    if "discovery.meethue.com" in flow.request.pretty_host:
        data = json.loads(flow.response.content)
        ipaddr=data[0]['internalipaddress']
        ctx.log.alert('[Hue] Leak Internal IP %s' %ipaddr)

