import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import random
import tkinter as tk
from tkinter import scrolledtext
import os

def load_epub(epub_path):
    book = epub.read_epub(epub_path)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
    # Get all the document items from the EPUB book
    return items

def extract_random_paragraph(items):
    """
    Extracts a random paragraph from a list of items.

    Args:
        items (list): A list of items.

    Returns:
        str: A random paragraph text if found, otherwise 'No text found.'
    """
    item = random.choice(items)
    soup = BeautifulSoup(item.get_body_content(), 'html.parser')
    paragraphs = soup.find_all('p')
    if paragraphs:
        return random.choice(paragraphs).text
    else:
        return 'No text found.'

def on_next_button_click():
    text_area.config(state=tk.NORMAL)
    text_area.delete('1.0', tk.END)
    random_text = extract_random_paragraph(epub_items)
    text_area.insert(tk.INSERT, random_text)
    text_area.config(state=tk.DISABLED)

# Load EPUB
# Get the path of the first EPUB file in the 'books' folder
books_folder = '../books'
epub_files = [file for file in os.listdir(books_folder) if file.endswith('.epub')]
if epub_files:
    epub_path = os.path.join(books_folder, epub_files[0])
else:
    epub_path = ''

epub_items = load_epub(epub_path)

# Set up the GUI
root = tk.Tk()
root.title("Random EPUB Fragment Viewer")

text_area = scrolledtext.ScrolledText(root, width=60, height=20, state=tk.DISABLED)
text_area.pack()

next_button = tk.Button(root, text="Show Next Fragment", command=on_next_button_click)
next_button.pack()

root.mainloop()
