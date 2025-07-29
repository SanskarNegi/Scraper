import requests
from bs4 import BeautifulSoup

#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative

# URL of the Amazon product
url = 'https://www.amazon.in/GeForce-Graphics-Interface-Extended-Warranty/dp/B0CHJV11VC'  # Example product link (replace with your desired product)

# Headers to mimic a real browser request (Amazon might block requests that don't have this)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


# Send a request to the amazon page
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Parse the content of the page with Beautifulsoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the price element in the HTML
    # Amazon often uses a couple of different formats for price depending on the country, availability, etc.
    price = soup.select_one('#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole')
    
    # if not price:
    #     price = soup.find('span', {'id':'priceblock_dealprice'})
    
    # extract and print the price if found
    if price:
        print(f'Price of the product: {price.get_text().strip()}')
    else:
        print('Price not found!')

else:
    print(f'Failed to retrieve the page, status code: {response.status_code}')




