laptops = [
    ['Apple', '1234$', '2567$', '2144$', '2567$'],
    ['Lg', '324$', '476$', '523$', '7657$'],
    ['Hp', '254$', '367$', '567$', '890$'],
    ['Honor', '299$', '345$', '587$', '6237$']
]


def show_price(laptops_price):
    print('Цена первую модель ноутбука -', laptops_price[0], laptops_price[1:2])


for price in laptops:
    show_price(price)


def keyword_function(a=1, b=2):
    return a + b


print(keyword_function(b=4, a=5))


age = 13


def get_older():
    global age
    age += 1


print(age)
get_older()
print(age)
