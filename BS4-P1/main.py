import requests
import bs4

url =  input("Enter URL: ")
response = requests.get(url)
# print(type(response))
# print(response.text)

filename = "temp.html"

bs = bs4.BeautifulSoup(response.text,"html.parser")

formatted_text = bs.prettify()
#print(formatted_text)

with open(filename, "w+") as f:
    f.write(formatted_text)


list_of_imgs = bs.find_all("img")
#print(list_of_imgs)
num_of_imgs = len(list_of_imgs)
print("No. of img tags = ", num_of_imgs)


list_of_anchorTags = bs.find_all("a")
#print(list_of_anchorTags)
num_of_anchorTags = len(list_of_anchorTags)
print("No. of anchor tags = ",num_of_anchorTags)












# use URL: https://www.techsoftindia.co.in/ only for educational/testing purpose.
# All rights reserved with techsoftindia 