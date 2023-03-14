from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.li.string)


all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for i in all_anchor_tags:
    # print(i.getText())
    print(i.get("href"))
heading = soup.find(name="h1", id="name")
print (heading)