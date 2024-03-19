import cv2
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import ttk  # Add this line to import ttk module


def process_image():
  # Open file dialog to select image
  file_path = filedialog.askopenfilename()

  # Read the selected image
  image = cv2.imread(file_path)

  # Convert the image to grayscale
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Invert the grayscale image
  inverted_gray_image = 255 - gray_image

  # Apply Gaussian blur to the inverted image
  blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

  # Invert the blurred image
  inverted_blurred_image = 255 - blurred_image

  # Avoid division by zero by adding a small value
  inverted_blurred_image = cv2.add(inverted_blurred_image, 1)

  # Create the pencil sketch image by blending the inverted blurred image with the original grayscale image
  pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

  # Display the original image and the pencil sketch
  plt.figure(figsize=(10, 5))
  plt.subplot(1, 2, 1)
  plt.title('Original Image')
  plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  plt.axis('off')

  plt.subplot(1, 2, 2)
  plt.title('Pencil Sketch')
  plt.imshow(pencil_sketch, cmap='gray')
  plt.axis('off')

  plt.show()


def open_settings():
  # Create settings window
  settings_window = tk.Toplevel()
  settings_window.title("Settings")

  def apply_settings():
    settings_window.destroy()

  # Theme dropdown
  theme_label = tk.Label(settings_window, text="Theme:")
  theme_label.grid(row=0, column=0, padx=10, pady=5)
  theme_options = ["Light", "Dark"]
  theme_var = tk.StringVar(value=theme_options[0])
  theme_dropdown = ttk.Combobox(settings_window,
                                textvariable=theme_var,
                                values=theme_options,
                                state="readonly")
  theme_dropdown.grid(row=0, column=1, padx=10, pady=5)

  # Style dropdown
  style_label = tk.Label(settings_window, text="Style:")
  style_label.grid(row=1, column=0, padx=10, pady=5)
  style_options = ["Sketch", "Pencil Drawing", "Charcoal Drawing", "Coloring"]
  style_var = tk.StringVar(value=style_options[0])
  style_dropdown = ttk.Combobox(settings_window,
                                textvariable=style_var,
                                values=style_options,
                                state="readonly")
  style_dropdown.grid(row=1, column=1, padx=10, pady=5)

  # Apply button
  apply_button = tk.Button(settings_window,
                           text="Apply",
                           command=apply_settings)
  apply_button.grid(row=2, column=0, columnspan=2, pady=10)


# Create the main application window
root = tk.Tk()
root.title("Pencil Sketch Generator")

# Add a button to select and process image with green color
process_button = tk.Button(root,
                           text="Select Image",
                           command=process_image,
                           bg="green")
process_button.pack(pady=20)

# Add a button to open settings with red color
settings_button = tk.Button(root,
                            text="Settings",
                            command=open_settings,
                            bg="red")
settings_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
