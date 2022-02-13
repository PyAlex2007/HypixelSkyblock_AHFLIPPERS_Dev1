import requests

page = 0
request = requests.get("https://api.hypixel.net/skyblock/auctions?page="+str(page)).json()
reforges = ["Gentle","Odd","Fast","Fair","Epic","Sharp","Heroic","Spicy","Legendary","Deadly","Fine","Grand",
            "Hasty","Neat","Rapid","Unreal","Awkward","Rich","Clean","Fierce","Heavy","Light","Mythic","Pure",
            "Smart","Titanic","Wise","Bizarre","Itchy","Ominous","Pleasant","Pretty","Shiny","Simple","Strange",
            "Vivid","Godly","Demonic","Forceful","Hurtful","Keen","Strong","Superior","Unpleasant","Zealous","◆",
            "[Lvl","✪","Dirty","Fabled","Suspicious","Gilded","Warped","Withered","Bulky","Salty","Treacherous",
            "Stiff","Lucky","Precise","Spiritual","Headstrong","Perfect","Necrotic","Ancient","Spiked","Renowned",
            "Cubic","Warped","Reinforced","Loving","Ridiculous","Empowered","Giant","Submerged","Jaded","Silky",
            "Bloody","Shaded","Sweet","Moil","Toil","Blessed","Bountiful","Magnetic","Fruitful","Refined","Stellar",
            "Mithraic","Auspicious","Fleet","Heated","Ambered"]
limit = input("")

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
        print("Total pages: "+str(page))

def linear_scan(items):
    items.sort()
    for item in range(len(items)):
        if item != 0 and item != len(items)-1:
            if items[item][0] != items[item-1][0] and items[item][0] == items[item+1][0] and items[item][1] < items[item+1][1]*0.5 and items[item][1] < int(limit):
                inside = False
                for i in reforges:
                    if i in items[item][0]:
                        inside = True
                if not inside:
                    print(items[item])
linear_scan(items)