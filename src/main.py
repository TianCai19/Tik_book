# Main execution script (could be named app.py, main.py, etc.)
from interface import create_interface

if __name__ == "__main__":
    interface = create_interface()
    interface.launch(share=False)