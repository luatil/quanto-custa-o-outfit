import numpy as np 

shirt_colortype = ['red', 'blue', 'black', 'white', 'grey']
formality = ['formal', 'casual']
pants_styletype = ['jeans', 'caqui']
pants_colortype = ['blue', 'black']
brands = ['renner', 'riachuelo', 'cea']

def random_element(l):
    return l[np.random.randint(low = 0, high = len(l))]


with open('random_wardrobe.txt', 'w') as f:
    for i in range(50):
        shirt_brand = random_element(brands)
        pants_brand = random_element(brands)
        shirt_color = random_element(shirt_colortype)
        pants_color = random_element(pants_colortype)
        shirt_formality = random_element(formality)
        pants_formality = random_element(formality)
        shirt_price = np.random.randint(low = 10, high = 60)
        pants_price = np.random.randint(low = 40, high = 120)
        pants_type = random_element(pants_styletype)
        shirt_str = f'shirt,{shirt_brand},{shirt_color},{shirt_formality},{shirt_price}\n'
        pants_str = f'pants,{pants_type},{pants_brand},{pants_color},{pants_formality},{pants_price}\n'
        f.write(shirt_str)
        f.write(pants_str)

