from ebooklib import epub
from bs4 import BeautifulSoup
import ebooklib
import random

def process_epub(file_path, min_length=1000):
    """
    Processes an EPUB file to randomly select a starting point and then extract continuous paragraphs
    that together meet a specified minimum length.
    """
    # Load the EPUB content
    book = epub.read_epub(file_path)
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
    
    all_paragraphs = []  # A list to hold all paragraphs in the EPUB
    
    # Iterate through each document item to collect all paragraphs
    for item in items:
        soup = BeautifulSoup(item.get_body_content(), 'html.parser')
        paragraphs = soup.find_all('p')  # Find all paragraph elements
        for paragraph in paragraphs:
            all_paragraphs.append(paragraph.text)  # Add paragraph text to the list

    # Randomly select a starting index from all paragraphs
    if all_paragraphs:
        start_index = random.randint(0, len(all_paragraphs) - 1)
    else:
        return "No paragraphs found in the EPUB."

    collected_text = ""  # Initialize an empty string to collect text
    
    # Iterate through paragraphs starting from the random index, concatenating them
    for i in range(start_index, len(all_paragraphs)):
        if len(collected_text) >= min_length:
            break  # Stop if we have enough text
        collected_text += all_paragraphs[i] + "\n\n"  # Add paragraph text to the collected text

    # Check if we've collected enough text; if not, return a message indicating so
    if len(collected_text) < min_length:
        return 'The text collected does not meet the minimum length requirement.'
    else:
        return collected_text

# Example usage:
# file_path = "path_to_your_epub_file.epub"
# print(process_epub(file_path, min_length=1000))
