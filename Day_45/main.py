from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")


# # print(soup.title)
article_titles = []
article_links = []
article_upvotes = []
tags = soup.find_all(name="span", class_="titleline")
for tag in tags:
    article_tag = tag.find(name="a")
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

upvote_tags = soup.find_all(name="span", class_="score")
for upvotes in upvote_tags:
    upvote_string = upvotes.get_text()
    article_upvotes.append(int(upvote_string.split(" ")[0]))


sorted_list = sorted(article_upvotes)
index = article_upvotes.index(sorted_list[-1])
print(article_upvotes.index(sorted_list[-1]))
print(article_titles[index])
print(article_links[index])
print(article_upvotes[index])

# all_achor_tags = soup.find_all(name="a", class_="titleline")

# for title in all_achor_tags:
#     print(title.getText())

























# with open("/Users/jamessingzon/Desktop/100DaysPython/Day_45/website.html") as file:
#     contents = file.read()

# # print(contents)

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup)
# print(soup.prettify())

# #Instead of returning first matching tag
# all_achor_tags = soup.find_all(name="a")
# print(all_achor_tags)
# print(type(all_achor_tags))

# for tag in all_achor_tags:
#     print(tag.getText())
#     #get value of attributes
#     print(tag.get("href"))

#     #get hold of items by the attribute name
# heading = soup.find(name="h1", id="name")
# print(heading)

#classes require a following underscore as to not clash with the python keyword for Classes
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.name)
# print(section_heading.get("class"))


# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector = "#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)
