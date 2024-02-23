import os

def generate_directory_tree(path, prefix=''):
    output = ''
    if os.path.isfile(path):
        output += f'{prefix + os.path.basename(path)}\n'
    else:
        output += f'{prefix + os.path.basename(path)}/\n'
        for item in os.listdir(path):
            output += generate_directory_tree(os.path.join(path, item), prefix + '  ')
    return output

def py_to_md(path):
    with open(r'C:\Users\jack\Downloads\output.md', 'w', encoding='utf-8') as md_file:
        md_file.write('# Project Structure\n\n```\n')
        md_file.write(generate_directory_tree(path))
        md_file.write('```\n\n')
        for filename in os.listdir(path):
            if filename.endswith('.py'):
                md_file.write(f'## {filename}\n\n```python\n')
                with open(os.path.join(path, filename), 'r', encoding='utf-8') as py_file:
                    md_file.write(py_file.read())
                md_file.write('\n```\n\n')

py_to_md('src')