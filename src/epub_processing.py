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
        all_paragraphs = []

        for item in items:
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            paragraphs = [p.text for p in soup.find_all('p')]
            all_paragraphs.extend(paragraphs)
        
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
