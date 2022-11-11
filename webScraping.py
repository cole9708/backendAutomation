import requests
from bs4 import BeautifulSoup


url ='http://www.imdb.com'
resp = requests.get('https://www.imdb.com/find?s=ep&q=triller&ref_=nv_sr_sm')
soapresp = BeautifulSoup(resp.content, 'html.parser')
print(soapresp.prettify())





