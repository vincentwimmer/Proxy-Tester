# This is a rough script for checking proxies and taking it a step forward to ensure your proxy hasn't been detected.

# On line 40 you can change your Proxy Type from 'socks5://' to whatever works for you.

# Lastly, be sure to create 2 text files:
# 'testproxies.txt' > Here you store your list of proxies in an IP:Port format seperated by new lines.
# 'goodproxies.txt' > This is where the script will be storing good proxies.

import requests

# Insert your URL here.
URL = 'https://www.websiteurl.com/'

# Here we will look for a specific line of HTML that ONLY appears on a SUCCESSFUL page load.
searchHTML = '<a class="" href="/link/to/page">some link</a>'

# You may need to periodically update the User Agent. You can simply google "What's my useragent".
headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.5",
	"Connection": "keep-alive",
	"TE" : "Trailers",
	"Upgrade-Insecure-Requests": "1", 
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
	}

proxy = []
proxList = []
proxy_txt = open('testproxies.txt', 'r')

for proxies in proxy_txt:
	proxies = proxies.strip('\n')
	proxy.append(proxies)
proxy_txt.close()

for x in range(len(proxy)):
	print("Testing", x, "of", len(proxy))
	prox = proxy[x]
	proxy_dict = {'https': ('socks5://{}'.format(prox))}

	try:
		getPage = requests.get(URL, headers=headers, proxies=proxy_dict, timeout=(10))
		if getPage.text.find(searchHTML) != -1:
			proxList.append(prox)
			print("Number", x, "succeeded, adding", prox, "to list.")
	except:
		pass

with open('goodproxies.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(proxList))
