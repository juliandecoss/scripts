from user_agents import parse
user_agent_string = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
user_agent_string = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
user_agent_string = "PostmanRuntime/7.29.0"
#user_agent_string = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
user_agent = parse(user_agent_string)
print(user_agent.os.family)  # This will get you what you need
print(user_agent.is_mobile)
print(user_agent.is_pc) 
print(user_agent.browser)
#user_agent.is_tablet # returns False
#user_agent.is_touch_capable # returns False
#user_agent.is_bot # returns False