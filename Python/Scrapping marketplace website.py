from bs4 import BeautifulSoup
import requests

# Function to extract Product Title
def get_title(soup):
	
	try:
		# Outer Tag Object
		title = soup.find("span", attrs={"id":'productTitle'})

		# Inner NavigableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip()

		# # Printing types of values for efficient understanding
		# print(type(title))
		# print(type(title_value))
		# print(type(title_string))
		# print()

	except AttributeError:
		title_string = ""	

	return title_string

# Function to extract Product Price
def get_price(soup):

	try:
		price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()

	except AttributeError:
		price = ""	

	return price

# Function to extract Product Rating
def get_rating(soup):

	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""	

	return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
	try:
		review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
		
	except AttributeError:
		review_count = ""	

	return review_count

# Function to extract Availability Status
def get_availability(soup):
	try:
		available = soup.find("div", attrs={'id':'availability'})
		available = available.find("span").string.strip()

	except AttributeError:
		available = ""	

	return available	

if __name__ == '__main__':

	# Headers for request
	HEADERS = ({'User-Agent':
	            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	            'Accept-Language': 'en-US, en;q=0.5'})

	# The webpage URL
	URL =  "https://www.amazon.com/gp/bestsellers/videogames/16227130011?ref_=Oct_d_obs_S&pd_rd_w=XUNwm&content-id=amzn1.sym.05db1fab-3555-4da8-8d54-acac215f94a1&pf_rd_p=05db1fab-3555-4da8-8d54-acac215f94a1&pf_rd_r=126G1MYJ97DSEP1A9878&pd_rd_wg=sYDl2&pd_rd_r=23323070-a5ab-4a07-a32f-65b43e95f697"
	 # "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"

	# HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	# Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")

	# Function calls to display all necessary product information
	# print("Product Title =", get_title(soup))
	# print("Product Price =", get_price(soup))
	# print("Product Rating =", get_rating(soup))
	# print("Number of Product Reviews =", get_review_count(soup))
	# print("Availability =", get_availability(soup))
	


testx = soup.find("i", attrs={'class':'a-icon a-icon-star-small a-star-small-5 aok-align-top'}).string.strip()

test2 = soup.findAll(attrs={'class':'zg-grid-general-faceout'})

for item in test2:
	print(item.span)