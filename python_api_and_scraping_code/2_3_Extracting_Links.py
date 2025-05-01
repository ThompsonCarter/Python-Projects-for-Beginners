# Extracting All Links from a Web Page
url = "https://www.bbc.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the links
    links = soup.find_all('a')
    
    for link in links:
        print(link.get('href'))  # Print the URL from the href attribute
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
