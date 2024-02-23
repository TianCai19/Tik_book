import gradio as gr
from ebooklib import epub
from bs4 import BeautifulSoup
import random
import ebooklib

def load_epub(file_path):
    book = epub.read_epub(file_path)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
    return items

def extract_random_paragraph(epub_content):
    item = random.choice(epub_content)
    soup = BeautifulSoup(item.get_body_content(), 'html.parser')
    paragraphs = soup.find_all('p')
    if paragraphs:
        return random.choice(paragraphs).text
    else:
        return 'No text found.'

def process_epub(epub_path):
    # epub_path is now a string, which is the path to the uploaded file
    epub_items = load_epub(epub_path)
    return extract_random_paragraph(epub_items)

# Modify your Gradio Interface instantiation accordingly
gr.Interface(
    fn=process_epub,
    inputs=gr.components.File(label="Upload EPUB"),
    outputs="text",
    title="Random EPUB Paragraph Reader",
    description="Upload an EPUB file to extract and display a random paragraph."
).launch(share=True)  # If you want to create a public link, as suggested by the tip.

