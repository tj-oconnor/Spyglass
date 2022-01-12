"""
This script spies on the responses from Amazon Alexa questions
"""
from mitmproxy import http, ctx
import os

def response(flow: http.HTTPFlow) -> None:
    if "avs-alexa-12-na.amazon.com" in flow.request.pretty_host:
        data=str(flow.response.content)
        for element in data.split("{"):
          if "caption" in element:
              caption = str(element).replace('"caption":','')
              answer = caption.split('"')[1]
              ctx.log.alert("[Alexa] <speaking> = %s" % answer)

