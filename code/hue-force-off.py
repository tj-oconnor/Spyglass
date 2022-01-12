"""
This script forces the Hue lights to turn off regardless of user input
"""
from mitmproxy import http, ctx
import json

def request(flow: http.HTTPFlow) -> None:
    if "api2.amplitude.com" in flow.request.pretty_host:
        if b'state%22%3A%22on' in flow.request.content:
           flow.request.content.replace(b'state%22%3A%22on',b'state%22%3A%22off')        
           ctx.log.alert("[Hue] <forcing Lights off> ")
