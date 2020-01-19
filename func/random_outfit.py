import pymongo

client = pymongo.MongoClient()
wardrobe = client['wardrobe']
shirts = wardrobe['shirts']
pants = wardrobe['pants']


def random_outfit_generator(num_shirts, num_pants, max_shirt_price, max_pants_price):
    shirt_query = {"price": {"$lt":max_shirt_price},"$sample": {"size": 1} 
    pants_query = {"price": {"$lt":max_pants_price}, "$sample": {"size":1}}
    shirt_result = shirts.find(shirt_query)
    pants_result = pants.find(pants_query)
    return shirt_result, pants_result