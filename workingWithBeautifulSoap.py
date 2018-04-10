import bs4
import requests

response = requests.get('url')
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')

requiredData = soup.select('css_selecter')
# returns list of matching elements
# you can get css_selector for any HTML tag
# by using dev tools and right-clicking+selecting css_selector
# paste it in program, kabooshh, that's that
#  
requiredData[0].text.strip()
