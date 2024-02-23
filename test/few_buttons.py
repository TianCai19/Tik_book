import gradio as gr

def greet(name):
    return "Hello, " + name + "!"

def calculate(number1, number2):
    return number1 * number2

def clear_output(output_text):
    return ""

interface = gr.Interface(
    [greet, calculate, clear_output],  # List of functions
    [
        gr.Textbox(label="Your Name"),
        gr.Number(label="Number 1"),
        gr.Number(label="Number 2"),
        gr.Textbox(lines=2, label="Output")
    ],
    outputs="textbox",
    title="Multiple Functions with Buttons",
)

# Create the buttons directly
gr.Button("Greet").click(fn=greet, inputs=[0], outputs=[3])
gr.Button("Calculate").click(fn=calculate, inputs=[1, 2], outputs=[3])
gr.Button("Clear").click(fn=clear_output, inputs=[3], outputs=[3]) 

interface.launch()
