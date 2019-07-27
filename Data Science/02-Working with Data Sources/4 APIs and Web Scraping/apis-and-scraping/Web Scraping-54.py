## 2. Web Page Structure ##

# Write your code here.

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

content = response.content






## 3. Retrieving Elements from a Page ##

from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With BeautifulSoup, we can access branches by using tag types as attributes.
head = parser.head

# Get the p tag from the body.
title = head.title

# Print the text inside the p tag.
# Text is a property that gets the inside text of a tag.
title_text = title.text

## 4. Using Find All ##

parser = BeautifulSoup(content, 'html.parser')

# Get a list of all occurrences of the body tag in the element.
head = parser.find_all("head")

# Get the paragraph tag.
title = head[0].find_all("title")

# Get the text.
title_text = title[0].text

## 5. Element IDs ##

# Get the page content and set up a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the ID attribute to only get the element with that specific ID.
second_paragraph = parser.find_all("p", id="second")[0]
second_paragraph_text = second_paragraph.text

## 6. Element Classes ##

# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then, take the first element in that list.
second_inner_paragraph = parser.find_all("p", class_="inner-text")
second_inner_paragraph_text = second_inner_paragraph[1].text

first_outer_paragraph = parser.find_all("p", class_="outer-text")
first_outer_paragraph_text = first_outer_paragraph[0].text

## 8. Using CSS Selectors ##

# Get the website that contains classes and IDs.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all of the elements that have the first-item class.
first_outer = parser.select(".outer-text")

first_outer_text = first_outer[0].text
# Print the text of the first paragraph (the first element with the first-item class).
second = parser.select("#second")

second_text = second[0].text

## 10. Using Nested CSS Selectors ##

# Get the Superbowl box score data.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

total_plays = parser.select("#total-plays")
patriots_total_plays = total_plays[0].select("td")[2]
patriots_total_plays_count = patriots_total_plays.text

total_yards = parser.select("#total-yards")
seahawks_total_yards = total_yards[0].select("td")[1]
seahawks_total_yards_count = seahawks_total_yards.text


