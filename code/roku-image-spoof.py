"""
This script rewrites the image from Roku menu
"""
from mitmproxy import http, ctx
import os

def response(flow: http.HTTPFlow) -> None:
    if "images.sr.roku.com" in flow.request.pretty_host:
        data=str(flow.response.content)
        spoof =  open('images/roku-spoof.jpg','rb').read()
        flow.response.content=spoof
        ctx.log.alert("[Roku] <Spoofed TV-Show Image>")
