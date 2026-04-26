from bs4 import BeautifulSoup 
import httpx

url = 'https://blog.faradars.org/%D8%AA%D8%AD%D9%84%DB%8C%D9%84-%D8%AF%D8%A7%D8%AF%D9%87-%DA%86%DB%8C%D8%B3%D8%AA/'
response = httpx.get(url)

soup = BeautifulSoup(response.text, 'html.parser')