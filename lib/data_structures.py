spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy= [item['name'] for item in spicy_foods]
    print(spicy)
get_names(spicy_foods)


def get_spiciest_foods(spicy_foods):
    very_spicy = [item for item in spicy_foods if item['heat_level'] > 5]
    print(very_spicy)
get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
   for item in spicy_foods:
       print( f"{item['name']} | Heat Level: { '🌶' * item['heat_level']}")  
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
   cuisine_spicy = [item for item in spicy_foods if item['cuisine'] == cuisine]
   print(cuisine_spicy)
get_spicy_food_by_cuisine(spicy_foods, 'Thai')


def print_spiciest_foods(spicy_foods):
    spiciest_foods= [f"{item['name']} | Heat Level: { '🌶' * item['heat_level']}" for item in spicy_foods if item['heat_level'] > 5]
    print(spiciest_foods)
print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    get_list = [ item['heat_level'] for item in spicy_foods]
    avg= sum(get_list)/len(spicy_foods)
    print(avg)
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
      
    spicy_foods.append(spicy_food)
    print(spicy_foods)
create_spicy_food(spicy_foods,  {
        "name": "chop suey",
        "cuisine": "japanese",
        "heat_level": 1,
    })
