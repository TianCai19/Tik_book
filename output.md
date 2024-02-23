## epub_processing.py

```python
from ebooklib import epub
from bs4 import BeautifulSoup
import ebooklib
import random
from diskcache import Cache

# 初始化diskcache缓存，设置大小限制为100MB
cache = Cache('./epub_cache', size_limit=100 * 1024 * 1024)

def load_and_cache_epub_paragraphs(file_path):
    """
    加载EPUB文件的所有段落，并将其缓存。如果缓存中已存在，则直接从缓存加载。
    """
    cache_key = f"paragraphs_{file_path}"

    if cache_key in cache:
        print("Loading paragraphs from cache")
        all_paragraphs = cache[cache_key]
    else:
        print("Processing and caching paragraphs")
        book = epub.read_epub(file_path)
        items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
        # print the length of the items
        print("Number of items: ", len(items))


        all_paragraphs = []

        for item in items:
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            paragraphs = [p.text for p in soup.find_all('p')]
            print("Number of paragraphs: ", len(paragraphs))
            all_paragraphs.extend(paragraphs)
        print("Total number of paragraphs: ", len(all_paragraphs))       
        cache[cache_key] = all_paragraphs

    return all_paragraphs

def process_epub(file_path, min_length=1000):
    """
    从缓存中加载EPUB的所有段落，然后随机选择一个起始位置，从该位置开始提取连续段落直到达到指定的最小长度。
    """
    all_paragraphs = load_and_cache_epub_paragraphs(file_path)

    # 如果没有段落，返回提示信息
    if not all_paragraphs:
        return "No paragraphs found in the EPUB."

    # 随机选择一个起始位置
    start_index = random.randint(0, len(all_paragraphs) - 1)
    collected_text = ""

    # 从随机起始位置开始，拼接段落直到满足最小长度要求
    for i in range(start_index, len(all_paragraphs)):
        collected_text += all_paragraphs[i] + "\n\n"
        if len(collected_text) >= min_length:
            break

    return collected_text

# 使用示例
# file_path = "path/to/your/epub/file.epub"
# print(process_epub(file_path, min_length=1000))

```

## interface.py

```python
# src/interface.py
import gradio as gr  # Import the gradio library to create web UIs for Python functions

# Import the necessary functions from the epub_processing module. These functions handle the loading of the EPUB file
# and the extraction of random paragraphs from it.
from epub_processing import process_epub

# Define a function that creates a Gradio interface
def create_interface():


    # Create and return a Gradio interface object.
    # - `fn`: The function to call when the user submits a file, which is process_epub in this case.
    # - `inputs`: The input components for the interface, here a File input for users to upload an EPUB file and a Number input for users to specify the length.
    # - `outputs`: The output type, which is text, indicating that the output will be displayed as text.
    # - `title`: The title of the web interface, which is displayed at the top.
    # - `description`: A brief description of what the interface does, providing users with instructions on how to use it.
    return gr.Interface(
        fn=process_epub,  # The function the interface will use to process the input
        inputs = [gr.File(label="Upload EPUB"), gr.Number(label="Length")],
          # Define the input components as a File upload field and a Number input field with a default value of 100
        outputs="text",  # Define the output component as a text field
        title="EPUB Content Reader",  # Title for the web interface
        description="Upload an EPUB file and specify the length to extract content."  # Description for what the interface will do
    )

# Note: This file doesn't execute the interface; it merely defines it.
# The execution should happen in a separate script where this module's `create_interface` function is called.

```

## main.py

```python
# Main execution script (could be named app.py, main.py, etc.)
from interface import create_interface

if __name__ == "__main__":
    interface = create_interface()
    interface.launch(share=False)
```

