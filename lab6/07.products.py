def main():
    products = {
        'Channel Bag': 852.00,
        'Earrings': 852.00,
        'Bracelet': 852.00,
        'iPhone': 599.00,
        'Galaxy': 599.00,
    }

    print("Length :", len(products));
    print("Prices :", list(products.values()));
    products.clear()
    print("Al cleared :", products);

if __name__ == '__main__':
    main()
