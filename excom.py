import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_and_save_resources(html_content, output_dir):
    # Extract CSS
    css_pattern = re.compile(r'<style[^>]*>(.*?)</style>', re.DOTALL)
    css_matches = css_pattern.findall(html_content)
    css_content = '\n'.join(css_matches)
    
    # Extract JavaScript
    js_pattern = re.compile(r'<script[^>]*>(.*?)</script>', re.DOTALL)
    js_matches = js_pattern.findall(html_content)
    js_content = '\n'.join(js_matches)
    
    # Remove CSS and JS from HTML
    html_content = css_pattern.sub('', html_content)
    html_content = js_pattern.sub('', html_content)
    
    # Save HTML with correct links to CSS and JS
    html_content = html_content.replace('</head>', f'<link rel="stylesheet" href="styles.css">\n</head>')
    html_content = html_content.replace('</body>', f'<script src="scripts.js"></script>\n</body>')
    
    with open(os.path.join(output_dir, 'output.html'), 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
    
    # Save CSS
    with open(os.path.join(output_dir, 'styles.css'), 'w', encoding='utf-8') as css_file:
        css_file.write(css_content)
    
    # Save JS
    with open(os.path.join(output_dir, 'scripts.js'), 'w', encoding='utf-8') as js_file:
        js_file.write(js_content)

def combine_resources(html_file, css_file, js_file, output_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    with open(css_file, 'r', encoding='utf-8') as file:
        css_content = file.read()
    
    with open(js_file, 'r', encoding='utf-8') as file:
        js_content = file.read()
    
    # Insert CSS and JS into HTML
    html_content = html_content.replace('</head>', f'<style>{css_content}</style></head>')
    html_content = html_content.replace('</body>', f'<script>{js_content}</script></body>')
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

def verify_resources(output_dir):
    html_path = os.path.join(output_dir, 'output.html')
    css_path = os.path.join(output_dir, 'styles.css')
    js_path = os.path.join(output_dir, 'scripts.js')
    
    if not os.path.exists(html_path) or not os.path.exists(css_path) or not os.path.exists(js_path):
        return False, "Some files are missing in the output directory."
    
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    if '<link rel="stylesheet" href="styles.css">' not in html_content:
        return False, "CSS link is missing in the HTML file."
    
    if '<script src="scripts.js"></script>' not in html_content:
        return False, "JS script link is missing in the HTML file."
    
    return True, "All files are correctly linked."

def select_html_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
    html_file.set(file_path)

def select_css_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSS Files", "*.css")])
    css_file.set(file_path)

def select_js_file():
    file_path = filedialog.askopenfilename(filetypes=[("JavaScript Files", "*.js")])
    js_file.set(file_path)

def select_output_directory():
    directory = filedialog.askdirectory()
    output_dir.set(directory)

def process_files():
    output_directory = output_dir.get()
    
    if not output_directory:
        messagebox.showerror("Error", "Please select an output directory.")
        return
    
    if mode.get() == "extract":
        html_path = html_file.get()
        if not html_path:
            messagebox.showerror("Error", "Please select an HTML file.")
            return
        
        with open(html_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        extract_and_save_resources(html_content, output_directory)
        
        # Verify resources
        success, message = verify_resources(output_directory)
        if success:
            messagebox.showinfo("Success", f"Processed HTML file and saved resources to {output_directory}\nVerification: {message}")
        else:
            messagebox.showerror("Verification Failed", message)
    
    elif mode.get() == "combine":
        html_path = html_file.get()
        css_path = css_file.get()
        js_path = js_file.get()
        
        if not html_path or not css_path or not js_path:
            messagebox.showerror("Error", "Please select HTML, CSS, and JS files.")
            return
        
        output_file_path = os.path.join(output_directory, 'combined.html')
        combine_resources(html_path, css_path, js_path, output_file_path)
        messagebox.showinfo("Success", f"Combined files saved to {output_file_path}")

# Create the main window
root = tk.Tk()
root.title("HTML/CSS/JS Separator and Combiner")

# Variables
html_file = tk.StringVar()
css_file = tk.StringVar()
js_file = tk.StringVar()
output_dir = tk.StringVar()
mode = tk.StringVar(value="extract")

# HTML File
tk.Label(root, text="HTML File:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=html_file, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_html_file).grid(row=0, column=2, padx=10, pady=10)

# CSS File (only for combine mode)
tk.Label(root, text="CSS File:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=css_file, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_css_file).grid(row=1, column=2, padx=10, pady=10)

# JS File (only for combine mode)
tk.Label(root, text="JS File:").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=js_file, width=50).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_js_file).grid(row=2, column=2, padx=10, pady=10)

# Output Directory
tk.Label(root, text="Output Directory:").grid(row=3, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_dir, width=50).grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_directory).grid(row=3, column=2, padx=10, pady=10)

# Mode Selection
tk.Label(root, text="Select Mode:").grid(row=4, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Extract HTML/CSS/JS", variable=mode, value="extract").grid(row=4, column=1, padx=10, pady=10, sticky="w")
tk.Radiobutton(root, text="Combine HTML/CSS/JS", variable=mode, value="combine").grid(row=5, column=1, padx=10, pady=10, sticky="w")

# Process Button
tk.Button(root, text="Process", command=process_files).grid(row=6, column=1, padx=10, pady=20)

# Run the application
root.mainloop()