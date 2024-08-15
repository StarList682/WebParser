import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def parse_data():
    url = entry.get()
    response = requests.get(url)

    if response.status_code == 200:
        page_content = response.content
        soup = BeautifulSoup(page_content, 'html.parser')
        
        website_id = url.split("//")[-1].split("/")[0]
        
        text_content = soup.get_text()
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        with open('website_data.txt', 'w') as file:
            file.write(f'Website URL: {url}\n')
            file.write(f'Website ID: {website_id}\n\n')
            file.write('Text Content:\n')
            file.write(text_content)
            file.write('\n\nLinks:\n')
            for link in links:
                file.write(f'{link}\n')

        messagebox.showinfo("Success", "Data saved in website_data.txt")
    else:
        messagebox.showerror("Error", f"Failed to retrieve the page, status code: {response.status_code}")

root = tk.Tk()
root.title("Data Parser")

label = tk.Label(root, text="Enter URL:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Parse", command=parse_data)
button.pack(pady=20)

root.mainloop()
