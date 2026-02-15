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

    print(price_catalog)

    print(sales_summary)


if __name__ == '__main__':
    main()
