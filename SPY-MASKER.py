import pyshorteners
import requests
import pyfiglet


result = pyfiglet.figlet_format("SPY-MASKER")
print(result)
banner = pyfiglet.figlet_format("Developed by SPIDY", font="slant", justify="left")
print(banner)




shortener = pyshorteners.Shortener()

########################################################################
#WEBSITE LINK TO BE MASKED

web_url = input("GIVE ORIGINAL LINK (EG : https://www.facebook.com/) -: ")

custom_domain = input("\nEnter your custom domain (EG : youtube.com) -: ")

phish = input("\nENTER PHISH LINES (EG : free-money , pubg-tricks) -: ")


########################################################################
cookies = {
    'DaGdSession_0': '3d1d3d7b77b445458341586c6541a936.qHRf%2FFKpzpCNDDj%2F5cKV2W%2B1ljk90mjBRX%2B4%2BFoIu%2F4%3D',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'DaGdSession_0=3d1d3d7b77b445458341586c6541a936.qHRf%2FFKpzpCNDDj%2F5cKV2W%2B1ljk90mjBRX%2B4%2BFoIu%2F4%3D',
    'Origin': 'https://da.gd',
    'Referer': 'https://da.gd/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'url': web_url,
    'shorturl': '',
}

response = requests.post('https://da.gd/', cookies=cookies, headers=headers, data=data)

response_text = response.text
#print(response_text)

# Find a specific piece of text within the response
start_text = 'monospace;">'
end_text = '</a></h1></div></div>'
start_index = response_text.find(start_text)
end_index = response_text.find(end_text)
specific_text = response_text[start_index+len(start_text):end_index]




# Shorten the URL with TinyURL
short_url = shortener.tinyurl.short(web_url)

# Mask the URL with custom domain and keyword
masked_url = "https://" + custom_domain + f"-{phish}@" + short_url.split('//')[1]

masked_url2 = "https://" + custom_domain + f"-{phish}@" + specific_text.split('//')[1]

print("\nOriginal URL:", web_url,"\n")
print("Masked URL 1:", masked_url,"\n")
print("Masked URL 2:", masked_url2,"\n")


input("Press ENTER to close program")
print("Thanks For using this program")




