## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers, params = params)
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers, params = params)
python_top = response.json()
python_top_articles = python_top["data"]["children"]

most_upvotes = 0
for i in python_top_articles:
    if i['data']['ups'] >= ups:
        most_upvotes = i['data']['ups']
        most_upvoted = i['data']['id']

    

## 4. Getting Post Comments ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
query = "https://oauth.reddit.com/r/python/comments/{}".format(most_upvoted) 
response = requests.get(query, headers = headers)
comments = response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]

comment = comments_list['data']['children']
most_upvotes_comment = 0
for i in comment:
    if  i["data"]["ups"] >= most_upvotes_comment:
        most_upvotes_comment = i["data"]['ups']
        most_upvoted_comment = i["data"]['id']

## 6. Upvoting a Comment ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
query = "https://oauth.reddit.com/api/vote"
payload = {"dir": 1, "id": "d16y4ry"}
response = requests.post(query, json = payload, headers =headers)
status = response.status_code