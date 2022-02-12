import requests

page = 0
request = requests.get("https://api.hypixel.net/skyblock/auctions?page="+str(page)).json()

items = []
finished = False
while not finished:
    try:
        for item in range(len(request["auctions"])):
            if request["auctions"][item]["bin"]:
                items.append([request["auctions"][item]["item_name"],request["auctions"][item]["starting_bid"]])
        page += 1
        request = requests.get("https://api.hypixel.net/skyblock/auctions?page=" + str(page)).json()
    except KeyError:
        finished = True
        print("Total pages: "+str(page-1))

items.sort()
for item in range(len(items)):
    if item != 0 and item != len(items)-1:
        if items[item][0] != items[item-1][0] and items[item][0] == items[item+1][0] and items[item][1] < items[item+1][1]*0.5:
            print(items[item])