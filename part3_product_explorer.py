# ---------------- TASK 1A: WRITE ----------------

with open("python_notes.txt", "w", encoding="utf-8") as file:
    file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    file.write("Topic 2: Lists are ordered and mutable.\n")
    file.write("Topic 3: Dictionaries store key-value pairs.\n")
    file.write("Topic 4: Loops automate repetitive tasks.\n")
    file.write("Topic 5: Exception handling prevents crashes.\n")

print("File written successfully.")

with open("python_notes.txt", "a", encoding="utf-8") as file:
    file.write("Topic 6: Functions help reuse code.\n")
    file.write("Topic 7: Python supports object-oriented programming.\n")

print("Lines appended.")

# ---------------- TASK 1B: READ ----------------

with open("python_notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("\nFile Content:")

for i in range(len(lines)):
    print(f"{i+1}. {lines[i].strip()}")

print("\nTotal number of lines:", len(lines))

keyword = input("\nEnter keyword to search: ").lower()

found = False

for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found.")

import requests

print("\n--- TASK 2: API INTEGRATION ---")

url = "https://dummyjson.com/products?limit=20"

response = requests.get(url)
data = response.json()

products = data["products"]

print("\nID  | Title                          | Category      | Price    | Rating")
print("----|--------------------------------|---------------|----------|-------")

for p in products:
    print(f"{p['id']:<4}| {p['title']:<30} | {p['category']:<13} | ${p['price']:<8} | {p['rating']}")

    print("\nFiltered (Rating ≥ 4.5):")

filtered = []

for p in products:
    if p["rating"] >= 4.5:
        filtered.append(p)

# Sort by price descending
filtered.sort(key=lambda x: x["price"], reverse=True)

for p in filtered:
    print(f"{p['title']} - ${p['price']} - Rating: {p['rating']}")
    print("\nLaptops Category:")

url2 = "https://dummyjson.com/products/category/laptops"

response2 = requests.get(url2)
data2 = response2.json()

laptops = data2["products"]

for p in laptops:
    print(f"{p['title']} - ${p['price']}")

print("\nPOST Request Response:")

new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

response3 = requests.post("https://dummyjson.com/products/add", json=new_product)

print(response3.json())

# ---------------- TASK 3A ----------------

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


# Test cases
print("\n--- Task 3A Output ---")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))

# ---------------- TASK 3B ----------------

def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")


print("\n--- Task 3B Output ---")
print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))

# ---------------- TASK 3C ----------------

import requests

print("\n--- Task 3C Output ---")

try:
    url = "https://dummyjson.com/products?limit=20"
    response = requests.get(url, timeout=5)

    response.raise_for_status()  # checks HTTP errors

    data = response.json()
    print("API fetch successful.")

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")

except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")

except Exception as e:
    print("Error:", e)

# ---------------- TASK 3D ----------------

print("\n--- Task 3D Output ---")

while True:
    user_input = input("Enter a product ID (1–100) or 'quit': ")

    if user_input.lower() == "quit":
        break

    # Validate integer
    if not user_input.isdigit():
        print("Invalid input! Enter a number.")
        continue

    product_id = int(user_input)

    if product_id < 1 or product_id > 100:
        print("Please enter ID between 1 and 100.")
        continue

    # API call
    try:
        url = f"https://dummyjson.com/products/{product_id}"
        response = requests.get(url, timeout=5)

        if response.status_code == 404:
            print("Product not found.")
        elif response.status_code == 200:
            product = response.json()
            print(f"{product['title']} - ${product['price']}")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")

    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")

    except Exception as e:
        print("Error:", e)

from datetime import datetime

# ---------------- TASK 4 ----------------

def log_error(function_name, error_type, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("error_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n")
    
    import requests

print("\n--- Task 4 Output ---")

try:
    bad_url = "https://this-host-does-not-exist-xyz.com/api"
    response = requests.get(bad_url, timeout=5)

except requests.exceptions.ConnectionError as e:
    print("Connection error triggered.")
    log_error("fetch_products", "ConnectionError", str(e))

try:
    url = "https://dummyjson.com/products/999"
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        print("HTTP error triggered (product not found).")
        log_error("lookup_product", "HTTPError", f"{response.status_code} Not Found for product ID 999")

except Exception as e:
    log_error("lookup_product", "UnexpectedError", str(e))

    print("\nError Log Contents:\n")

try:
    with open("error_log.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("No log file found.")
    