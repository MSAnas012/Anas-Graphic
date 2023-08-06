# Import the necessary libraries.
import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# Create the main window.
root = tk.Tk()
root.title("Graphic Designer Portfolio")
# Create the canvas.
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
# Create the header.
header = tk.Label(canvas, text="My Graphic Designer Portfolio", font=("Helvetica", 24))
header.place(x=100, y=10)
# Create the navigation bar.
nav_bar = tk.Frame(canvas)
nav_bar.place(x=10, y=50)
# Create the links in the navigation bar.
link1 = tk.Button(nav_bar, text="About Me", command=lambda: open_about_page())
link1.pack(side="left")
link2 = tk.Button(nav_bar, text="Skills", command=lambda: open_skills_page())
link2.pack(side="left")
link3 = tk.Button(nav_bar, text="Projects", command=lambda: open_projects_page())
link3.pack(side="left")
link4 = tk.Button(nav_bar, text="Contact Me", command=lambda: open_contact_pag9())
link4.pack(side="left")
# Create the about page.
def open_about_page():
  # Create the about page frame.
  about_page = tk.Frame(canvas)
  about_page.place(x=10, y=100)
  # Create the about me label.
  about_me_label = tk.Label(about_page, text="About Me", font=("Helvetica", 18))
  about_me_label.pack(side="top")
  # Create the about me text.
  about_me_text = tk.Text(about_page, height=10, width=50)