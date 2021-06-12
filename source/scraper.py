import requests
from bs4 import BeautifulSoup as BST

# Getting username to make url.
githubUsername = input('Input GitHub Username: ')

url = 'https://github.com/' + githubUsername

request = requests.get(url)

htmlContent = BST(request.content, 'html.parser')

profileImage = htmlContent.find('img', {'alt' : 'Avatar'})['src']

numberOfRepo = htmlContent.find('span', {'class' : 'Counter'})['title']


print('')
print('----------------------------------------------------')
print('Profile picture link: ' + profileImage)
print('Number of Repositories: ' + numberOfRepo)
print('----------------------------------------------------')
print('')
