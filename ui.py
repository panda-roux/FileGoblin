import tkinter as tk
from PIL import Image, ImageTk
import configparser

class TkinterHandler:
    def __init__(self, window_title="GoblinFile Project", window_size=(300, 180)):
        self.config = configparser.ConfigParser()
        self.config.read('config.txt')
        self.root = tk.Tk()
        self.root.title(window_title)

        # Calculate the position to center the window
        position_top = int(self.root.winfo_screenheight() / 2 - window_size[1] / 2)
        position_right = int(self.root.winfo_screenwidth() / 2 - window_size[0] / 2)

        # Set the window size and position
        self.root.geometry(f"{window_size[0]}x{window_size[1]}+{position_right}+{position_top}")

        # Set the minimum and maximum window size
        self.root.minsize(500, 200)
        self.root.maxsize(500, 200)

        # Create a frame for the left side of the window
        left_frame = tk.Frame(self.root)
        left_frame.grid(row=0, column=0, sticky='ns')


        # Create a LabelFrame in the left frame
        label_frame = tk.LabelFrame(left_frame)
        label_frame.grid(row=0, column=0, padx=10, pady=10)

        # Add a title to the LabelFrame
        title = tk.Label(label_frame, text=window_title, font=("Arial", 24))
        title.grid(row=0, column=0, padx=0, pady=0, sticky='sn')

        # Add a "Goblin" button to the LabelFrame
        goblin_button = tk.Button(label_frame, text="Goblin", command=self.goblin)
        goblin_button.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        # Add an "Exit" button to the LabelFrame
        exit_button = tk.Button(label_frame, text="Exit", command=self.root.quit)
        exit_button.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

        # Load and display the image on the right side of the window
        img = Image.open("assets/FileGoblin.png")
        img = img.resize((300, 160), Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img)
        img_label = tk.Label(self.root, image=self.photoImg)
        img_label.grid(row=0, column=1, sticky='n')

    def goblin(self):
        print("Goblin button clicked!")

    def run(self):
        self.root.mainloop()
