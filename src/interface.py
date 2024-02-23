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
