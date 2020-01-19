import pymongo

client = pymongo.MongoClient()

db_name = "wardrobe"
col1 = "shirts"
col2 = "pants"

db = client[db_name]

shirts = db[col1]
pants  = db[col2]

with open("random_wardrobe.txt", "r") as f:
    for line in f:
        info = line.split(',')
        if info[0] == 'shirt':
            shirt_element = {'brand': info[1],
                            'color': info[2],
                            'formality': info[3],
                            'price': int(info[4][:-1])}
            shirts.insert(shirt_element)
        elif info[0] == 'pants':
            pants_element = {'style': info[1],
                            'brand': info[2],
                            'color': info[3],
                            'formality': info[4],
                            'price': int(info[5][:-1])}
            pants.insert(pants_element)
