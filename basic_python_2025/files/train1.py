import csv

def process_products(input_file, output_file):
    """
    Reads a CSV file containing product names, prices, and quantities,
    calculates the total price for each product, and saves the result to a new CSV file.
    
    Args:
        input_file (str): Path to the input CSV file
        output_file (str): Path to the output CSV file
    """
    try:
        processed_data = []

        # Reading data from the CSV file
        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Calculating the total price and storing in a new list
            for row in reader:
                try:
                    price = float(row['Price'])
                    quantity = int(row['Quantity'])
                    total_price = price * quantity
                    row['Total Price'] = round(total_price, 2)
                    processed_data.append(row)
                except ValueError:
                    print(f"Error in data conversion: {row}")

        # Writing the processed data to a new CSV file
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            fieldnames = ['Product Name', 'Price', 'Quantity', 'Total Price']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Writing the header
            writer.writeheader()

            # Writing the processed rows
            for data in processed_data:
                writer.writerow(data)

        print(f"Processing completed successfully. Output file: {output_file}")

    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Running the function
input_csv = 'products.csv'
output_csv = 'processed_products.csv'
process_products(input_csv, output_csv)
