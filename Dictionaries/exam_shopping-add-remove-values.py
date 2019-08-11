product_dict = {}

while True:

    products = input().split(" ")

    if products[0] == "exam":
        break
    elif products[0] == "shopping":
        continue

    if products[0] == "stock":
        key = ' '.join(products[1:-1])
        value = int(products[-1])
        if key in product_dict.keys():
            product_dict[key] += value
        else:
            product_dict[key] = value
    elif products[0] == "buy":
        key = ' '.join(products[1:-1])
        value = int(products[-1])
        if key in product_dict.keys():
            if product_dict.get(key) == 0:
                print(f'{key} out of stock')
            elif product_dict.get(key) < value:
                product_dict[key] = 0
            else:
                product_dict[key] -= value
        else:
            print(f'{key} doesn\'t exist')


for key, value in product_dict.items():
    if value > 0:
        print(f'{key} -> {value}')