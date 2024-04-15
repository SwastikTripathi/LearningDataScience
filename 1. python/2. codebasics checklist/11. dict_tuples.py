import math
# Question 1
country_population = {'china':143, 'india':136, 'usa':32, 'pakistan':21}
def q1():
    while(True):
        inp = input('enter command: ')
        match inp:
            case 'print':
                print_countries()
            case 'add':
                add_countries()
            case 'remove':
                remove_countries()
            case 'query':
                query_countries()
            case 'exit':
                exit()

def print_countries():
    for key, value in country_population.items():
        print(key,'==>',value)

def add_countries():
    name = input('enter name: ')
    if name in country_population:
        print('already exists')
    else:
        population = input('enter population: ')
        country_population[name] = population
        print_countries()

def remove_countries():
    name = input('enter name: ')
    if name not in country_population:
        print('country doesn\'t exist')
    else:
        del country_population[name]
        print_countries()

def query_countries():
    name = input('enter name: ')
    if name not in country_population:
        print('country doesn\'t exist')
    else:
        print(name,'==>',country_population[name])

# q1() # uncomment to run quesiton 1


# Question 2
stocks = {'info':[600,630,620], 'ril':[1430,1490,1567], 'mtl':[234,180,160]}
def q2():
    while(True):
        inp = input('enter command: ')
        match inp:
            case 'print':
                print_stocks()
            case 'add':
                add_stocks()
            case 'exit':
                exit()

def print_stocks():
    for name, prices in stocks.items():
        print(name,' ==> ',prices,' ==> avg: ',avg(stocks[name]))

def avg(prices):
    sum = 0
    l = len(prices)
    for i in prices:
        sum = sum + i
    return round(sum/l, 2)

def add_stocks():
    name = input('enter ticker: ')
    price = int(input('enter price: '))
    if name in stocks:
        stocks[name].append(price)
    else:
        stocks[name] = [price]

# q2() # uncomment to run quesiton 2

# Question 3
def circle_calc(radius):
    area = 2*math.pi*(radius**2)
    circum = 2*math.pi*radius
    dia = 2*radius
    return (area, circum, dia)

def q3():
    radius = int(input())
    print(circle_calc(radius))

# q3() # uncomment to run quesiton 3