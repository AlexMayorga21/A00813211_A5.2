"""
Module for computing prices associated on catalog from files.

This module provides functionality to calculate total amount of sales read from a json file, the catalog of
product prices is also read from a json file.
"""
import sys
import time
import json

def main():
    """
    Main function to calculate total amount of sales from a file.

    Reads price catalog from a file specified as command line argument,
    calculates the total amount of sales and writes results to file and console.
    """
    start_time = time.time()


    # price catalog on argument 1
    price_catalog_file_name = sys.argv[1]
    # sales summary on argument 2
    sales_summary_file_name = sys.argv[2]


    # Open the file for reading
    try:
        with open(price_catalog_file_name, 'r', encoding='utf-8') as file:
            price_catalog = json.load(file)
    except FileNotFoundError:
        print("Error price catalog file not found process cannot continue without it")
        elapsed_time = time.time() - start_time
        print(f"elapsed_time: {elapsed_time}")
        return

    try:
        with open(sales_summary_file_name, 'r', encoding='utf-8') as file:
            sales_summary = json.load(file)
    except FileNotFoundError:
        print("Sales summary file not found process cannot continue without it")
        elapsed_time = time.time() - start_time
        print(f"elapsed_time: {elapsed_time}")
        return

    product_prices = {product['title']: product['price'] for product in price_catalog}

    # Calculate total
    total = 0
    output = f"{'Product':<30} {'Quantity':>10} {'Price':>10} {'Total':>12}\n"
    output += "-" * 62 + "\n"
    for sale in sales_summary:
        try:
            product_name = sale['Product']
            quantity = int(sale['Quantity'])
            price = product_prices[product_name]
            item_total = price * quantity
            output += f"{product_name:<30} {quantity:>10} ${price:>9.2f} ${item_total:>11.2f}\n"
            total += item_total
        except KeyError:
            output += f"ERROR: Product '{sale.get('Product', 'unknown')}' not found\n"
        except ValueError:
            output += f"ERROR: Invalid quantity for '{sale.get('Product', 'unknown')}'\n"


    # Format total to two digits decimal
    total = round(total, 2)

    elapsed_time = time.time() - start_time
    # Print and write results
    with open('SalesResults.txt', 'w', encoding='utf-8') as file:
        file.write(output)
        file.write(f"total: {total}\n")
        file.write(f"elapsed time: {elapsed_time}\n")
    print(output)
    print(f"total: {total}")
    print(f"elapsed time: {elapsed_time}")



if __name__ == '__main__':
    main()
