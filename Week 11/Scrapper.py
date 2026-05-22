import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import messagebox, ttk

def get_car_data(car):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://google.com"
    }
    url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'
    response = requests.get(url, headers=headers)
    cars = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)
                    cars.append({'name': name, 'price': price})
    else:
        print("Page not available!")
    return cars

def save_to_csv(data, filename):
    if not data:
        print("No data to save!")
        return
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'price'])
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")

def search():
    car = entry.get().strip().lower().replace(" ", "-")
    if not car:
        messagebox.showwarning("Input Error", "Please enter a car manufacturer name!")
        return
    status_label.config(text="Fetching data...")
    root.update()
    data = get_car_data(car)
    if not data:
        status_label.config(text="No data found!")
        messagebox.showerror("Error", "No data found! Check manufacturer name.")
        return
    for row in tree.get_children():
        tree.delete(row)
    for item in data:
        tree.insert('', tk.END, values=(item['name'], item['price']))
    filename = f"{car}_prices.csv"
    save_to_csv(data, filename)
    status_label.config(text=f"Done! Data saved to {filename}")

root = tk.Tk()
root.title("PakWheels Car Price Finder")
root.geometry("600x450")

tk.Label(root, text="Car Manufacturer:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Search", command=search).pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tree = ttk.Treeview(frame, columns=('Name', 'Price'), show='headings')
tree.heading('Name', text='Car Model')
tree.heading('Price', text='Price (PKR)')
tree.column('Name', width=350)
tree.column('Price', width=200)
tree.pack(fill=tk.BOTH, expand=True)

root.mainloop()