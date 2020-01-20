import pymongo

client = pymongo.MongoClient()
wardrobe = client['wardrobe']
shirts = wardrobe['shirts']
pants = wardrobe['pants']


def random_outfit_generator(num_outfits, max_shirt_price, max_pants_price):
    shirts_query = [{"$match": {"price": {"$lt": max_shirt_price}}}, {"$sample": {"size":num_outfits}}]
    pants_query = [{"$match": {"price": {"$lt": max_pants_price}}}, {"$sample": {"size":num_outfits}}]
    shirt_result = shirts.aggregate(shirts_query)
    pants_result = pants.aggregate(pants_query)
    outfit_list = []
    for doc in zip(shirt_result, pants_result):
        outfit_list.append(doc)
    return outfit_list
