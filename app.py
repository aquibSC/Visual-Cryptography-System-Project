import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os

from encryption.generate_shares import generate_shares
from decryption.reconstruct_image import reconstruct_image


class VisualCryptographyApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Visual Cryptography System")
        self.root.state("zoomed")

        # =========================
        # THEME
        # =========================

        self.dark_mode = True

        self.themes = {
            "dark": {
                "bg": "#111827",
                "card": "#1f2937",
                "header": "#1e293b",
                "text": "#ffffff",
                "secondary": "#9ca3af",
                "blue": "#2563eb",
                "blue_hover": "#1d4ed8",
                "green": "#059669",
                "green_hover": "#047857",
                "purple": "#7c3aed",
                "purple_hover": "#6d28d9",
                "red": "#dc2626",
                "red_hover": "#b91c1c",
                "preview": "#0f172a"
            },

            "light": {
                "bg": "#f3f4f6",
                "card": "#ffffff",
                "header": "#e5e7eb",
                "text": "#111827",
                "secondary": "#6b7280",
                "blue": "#2563eb",
                "blue_hover": "#1d4ed8",
                "green": "#059669",
                "green_hover": "#047857",
                "purple": "#7c3aed",
                "purple_hover": "#6d28d9",
                "red": "#dc2626",
                "red_hover": "#b91c1c",
                "preview": "#e5e7eb"
            }
        }

        self.colors = self.themes["dark"]

        # =========================
        # VARIABLES
        # =========================

        self.selected_image = None
        self.save_location = None

        self.selected_share1 = None
        self.selected_share2 = None

        self.decryption_save_location = None

        self.original_photo = None
        self.share1_photo = None
        self.share2_photo = None
        self.reconstructed_photo = None

        # =========================
        # START HOME
        # =========================

        self.show_home_page()

    # =========================================================
    # GENERAL FUNCTIONS
    # =========================================================

    def clear_page(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    def toggle_theme(self):

        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.colors = self.themes["dark"]
        else:
            self.colors = self.themes["light"]

        self.show_home_page()

    def create_button(
        self,
        parent,
        text,
        command,
        bg,
        hover,
        width=20,
        height=1,
        font_size=10
    ):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", font_size, "bold"),
            bg=bg,
            fg="white",
            activebackground=hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            width=width,
            height=height
        )

        return button

    # =========================================================
    # HOME PAGE
    # =========================================================

    def show_home_page(self):

        self.clear_page()

        c = self.colors

        # Header
        header = tk.Frame(
            self.root,
            bg=c["header"],
            height=130
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="🔐  VISUAL CRYPTOGRAPHY",
            font=("Segoe UI", 26, "bold"),
            bg=c["header"],
            fg=c["text"]
        ).pack(pady=(25, 4))

        tk.Label(
            header,
            text="Secure Image Sharing System",
            font=("Segoe UI", 11),
            bg=c["header"],
            fg=c["secondary"]
        ).pack()

        # Theme button
        theme_text = "☀ Light Mode" if self.dark_mode else "🌙 Dark Mode"

        theme_button = tk.Button(
            header,
            text=theme_text,
            command=self.toggle_theme,
            font=("Segoe UI", 9, "bold"),
            bg=c["card"],
            fg=c["text"],
            relief="flat",
            cursor="hand2"
        )

        theme_button.place(
            x=790,
            y=25
        )

        # Main
        main = tk.Frame(
            self.root,
            bg=c["bg"]
        )

        main.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            main,
            text="What do you want to do?",
            font=("Segoe UI", 20, "bold"),
            bg=c["bg"],
            fg=c["text"]
        ).pack(pady=(65, 30))

        # Encryption Card
        encryption_card = tk.Frame(
            main,
            bg=c["card"],
            width=500,
            height=120
        )

        encryption_card.pack(pady=10)
        encryption_card.pack_propagate(False)

        tk.Label(
            encryption_card,
            text="🔐  ENCRYPTION",
            font=("Segoe UI", 15, "bold"),
            bg=c["card"],
            fg=c["text"]
        ).pack(pady=(18, 3))

        tk.Label(
            encryption_card,
            text="Convert an image into two secure shares",
            font=("Segoe UI", 9),
            bg=c["card"],
            fg=c["secondary"]
        ).pack()

        self.create_button(
            encryption_card,
            "Start Encryption",
            self.show_encryption_page,
            c["blue"],
            c["blue_hover"],
            width=22,
            font_size=9
        ).pack(pady=8)

        # Decryption Card
        decryption_card = tk.Frame(
            main,
            bg=c["card"],
            width=500,
            height=120
        )

        decryption_card.pack(pady=10)
        decryption_card.pack_propagate(False)

        tk.Label(
            decryption_card,
            text="🔓  DECRYPTION",
            font=("Segoe UI", 15, "bold"),
            bg=c["card"],
            fg=c["text"]
        ).pack(pady=(18, 3))

        tk.Label(
            decryption_card,
            text="Use two shares to reconstruct the image",
            font=("Segoe UI", 9),
            bg=c["card"],
            fg=c["secondary"]
        ).pack()

        self.create_button(
            decryption_card,
            "Start Decryption",
            self.show_decryption_page,
            c["purple"],
            c["purple_hover"],
            width=22,
            font_size=9
        ).pack(pady=8)

        # Footer
        tk.Label(
            self.root,
            text="Visual Cryptography • Secure Image Sharing",
            font=("Segoe UI", 9),
            bg=c["header"],
            fg=c["secondary"],
            pady=8
        ).pack(
            fill="x",
            side="bottom"
        )

    # =========================================================
    # ENCRYPTION PAGE
    # =========================================================

    def show_encryption_page(self):

        self.clear_page()

        c = self.colors

        # Header
        header = tk.Frame(
            self.root,
            bg=c["header"],
            height=85
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Button(
            header,
            text="← Back",
            command=self.show_home_page,
            font=("Segoe UI", 9, "bold"),
            bg=c["card"],
            fg=c["text"],
            relief="flat",
            cursor="hand2"
        ).place(
            x=20,
            y=28
        )

        tk.Label(
            header,
            text="🔐  ENCRYPTION",
            font=("Segoe UI", 21, "bold"),
            bg=c["header"],
            fg=c["text"]
        ).pack(pady=(16, 0))

        tk.Label(
            header,
            text="Create two secure image shares",
            font=("Segoe UI", 9),
            bg=c["header"],
            fg=c["secondary"]
        ).pack()

        # Main
        main = tk.Frame(
            self.root,
            bg=c["bg"]
        )

        main.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        # ================= ORIGINAL =================

        original_card = tk.Frame(
            main,
            bg=c["card"],
            height=205
        )

        original_card.pack(
            fill="x",
            pady=(0, 10)
        )

        original_card.pack_propagate(False)

        tk.Label(
            original_card,
            text="ORIGINAL IMAGE",
            font=("Segoe UI", 11, "bold"),
            bg=c["card"],
            fg=c["text"]
        ).pack(pady=(8, 2))

        self.encryption_image_label = tk.Label(
            original_card,
            text="No image selected",
            font=("Segoe UI", 8),
            bg=c["card"],
            fg=c["secondary"]
        )

        self.encryption_image_label.pack()

        self.encryption_preview = tk.Label(
            original_card,
            text="No Preview",
            bg=c["preview"],
            fg=c["secondary"],
            width=22,
            height=5
        )

        self.encryption_preview.pack(pady=5)

        self.create_button(
            original_card,
            "Select Original Image",
            self.select_encryption_image,
            c["blue"],
            c["blue_hover"],
            width=22,
            font_size=8
        ).pack(pady=4)

        # ================= SAVE LOCATION =================

        location_frame = tk.Frame(
            main,
            bg=c["card"],
            height=48
        )

        location_frame.pack(
            fill="x",
            pady=5
        )

        location_frame.pack_propagate(False)

        tk.Label(
            location_frame,
            text="Save Location:",
            font=("Segoe UI", 9, "bold"),
            bg=c["card"],
            fg=c["text"]
        ).pack(
            side="left",
            padx=12
        )

        self.encryption_location_label = tk.Label(
            location_frame,
            text="Not selected",
            font=("Segoe UI", 8),
            bg=c["card"],
            fg=c["secondary"]
        )

        self.encryption_location_label.pack(
            side="left"
        )

        self.create_button(
            location_frame,
            "Choose Folder",
            self.choose_save_location,
            c["purple"],
            c["purple_hover"],
            width=14,
            font_size=8
        ).pack(
            side="right",
            padx=10
        )

        # ================= GENERATE =================

        self.create_button(
            main,
            "🔐  GENERATE ENCRYPTED SHARES",
            self.encrypt_image,
            c["green"],
            c["green_hover"],
            width=32,
            font_size=10
        ).pack(pady=7)

        # ================= PROGRESS =================

        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor=c["preview"],
            background=c["green"],
            thickness=12
        )

        self.encryption_progress = ttk.Progressbar(
            main,
            style="Custom.Horizontal.TProgressbar",
            orient="horizontal",
            length=650,
            mode="determinate"
        )

        self.encryption_progress.pack(pady=3)

        self.encryption_status = tk.Label(
            main,
            text="Ready",
            font=("Segoe UI", 8),
            bg=c["bg"],
            fg=c["secondary"]
        )

        self.encryption_status.pack()

        # ================= SHARE PREVIEWS =================

        shares_frame = tk.Frame(
            main,
            bg=c["bg"]
        )

        shares_frame.pack(
            fill="x",
            pady=7
        )

        # Share 1
        self.share1_result = tk.Label(
            shares_frame,
            text="SHARE 1\n\nNo Preview",
            font=("Segoe UI", 9, "bold"),
            bg=c["card"],
            fg=c["secondary"],
            width=40,
            height=7
        )

        self.share1_result.pack(
            side="left",
            expand=True,
            fill="both",
            padx=(0, 5)
        )

        # Share 2
        self.share2_result = tk.Label(
            shares_frame,
            text="SHARE 2\n\nNo Preview",
            font=("Segoe UI", 9, "bold"),
            bg=c["card"],
            fg=c["secondary"],
            width=40,
            height=7
        )

        self.share2_result.pack(
            side="right",
            expand=True,
            fill="both",
            padx=(5, 0)
        )

    # =========================================================
    # SELECT ENCRYPTION IMAGE
    # =========================================================

    def select_encryption_image(self):

        file_path = filedialog.askopenfilename(
            title="Select Original Image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:
            return

        self.selected_image = file_path

        self.encryption_image_label.config(
            text=os.path.basename(file_path),
            fg=self.colors["green"]
        )

        self.show_image_preview(
            file_path,
            self.encryption_preview,
            180,
            105
        )

        self.encryption_status.config(
            text="Original image selected"
        )

    # =========================================================
    # SAVE LOCATION
    # =========================================================

    def choose_save_location(self):

        folder = filedialog.askdirectory(
            title="Choose Save Location"
        )

        if not folder:
            return

        self.save_location = folder

        self.encryption_location_label.config(
            text=folder,
            fg=self.colors["green"]
        )

    # =========================================================
    # ENCRYPT IMAGE
    # =========================================================

    def encrypt_image(self):

        if not self.selected_image:

            messagebox.showwarning(
                "No Image",
                "Please select an original image first."
            )

            return

        if not self.save_location:

            messagebox.showwarning(
                "No Save Location",
                "Please choose a save location first."
            )

            return

        try:

            self.encryption_progress["value"] = 10

            self.encryption_status.config(
                text="Preparing encryption..."
            )

            self.root.update_idletasks()

            share1_path = os.path.join(
                self.save_location,
                "Share1.png"
            )

            share2_path = os.path.join(
                self.save_location,
                "Share2.png"
            )

            self.encryption_progress["value"] = 40

            self.encryption_status.config(
                text="Generating encrypted shares..."
            )

            self.root.update_idletasks()

            generate_shares(
                self.selected_image,
                share1_path,
                share2_path
            )

            self.encryption_progress["value"] = 75

            self.encryption_status.config(
                text="Loading share previews..."
            )

            self.root.update_idletasks()

            # Share 1 preview
            self.show_image_preview(
                share1_path,
                self.share1_result,
                180,
                100
            )

            # Share 2 preview
            self.show_image_preview(
                share2_path,
                self.share2_result,
                180,
                100
            )

            self.encryption_progress["value"] = 100

            self.encryption_status.config(
                text="Encryption completed successfully!"
            )

            messagebox.showinfo(
                "Encryption Complete",
                "Encrypted shares generated successfully!\n\n"
                f"Share 1:\n{share1_path}\n\n"
                f"Share 2:\n{share2_path}"
            )

        except Exception as e:

            self.encryption_progress["value"] = 0

            self.encryption_status.config(
                text="Encryption failed"
            )

            messagebox.showerror(
                "Encryption Error",
                str(e)
            )

    # =========================================================
    # DECRYPTION PAGE
    # =========================================================

    def show_decryption_page(self):

        self.clear_page()

        c = self.colors

        # Header
        header = tk.Frame(
            self.root,
            bg=c["header"],
            height=85
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Button(
            header,
            text="← Back",
            command=self.show_home_page,
            font=("Segoe UI", 9, "bold"),
            bg=c["card"],
            fg=c["text"],
            relief="flat",
            cursor="hand2"
        ).place(
            x=20,
            y=28
        )

        tk.Label(
            header,
            text="🔓  DECRYPTION",
            font=("Segoe UI", 21, "bold"),
            bg=c["header"],
            fg=c["text"]
        ).pack(pady=(16, 0))

        tk.Label(
            header,
            text="Use Share 1 and Share 2 to reconstruct the image",
            font=("Segoe UI", 9),
            bg=c["header"],
            fg=c["secondary"]
        ).pack()

        # Main
        main = tk.Frame(
            self.root,
            bg=c["bg"]
        )

        main.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        # ================= SHARES =================

        shares_frame = tk.Frame(
            main,
            bg=c["bg"]
        )

        shares_frame.pack(
            fill="x"
        )

        # Share 1
        share1_card = tk.Frame(
            shares_frame,
            bg=c["card"],
            height=210
        )

        share1_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 6)
        )

        share1_card.pack_propagate(False)

        tk.Label(
            share1_card,
            text="SHARE 1",
            font=("Segoe UI", 11, "bold"),
            bg=c["card"],
            fg=c["text"]
        ).pack(pady=(10, 3))

        self.decryption_share1_label = tk.Label(
            share1_card,
            text="Not selected",
            font=("Segoe UI", 8),
            bg=c["card"],
            fg=c["secondary"]
        )

        self.decryption_share1_label.pack()

        self.decryption_share1_preview = tk.Label(
            share1_card,
            text="No Preview",
            bg=c["preview"],
            fg=c["secondary"],
            width=25,
            height=6
        )

        self.decryption_share1_preview.pack(pady=8)

        self.create_button(
            share1_card,
            "Select Share 1",
            self.select_decryption_share1,
            c["purple"],
            c["purple_hover"],
            width=18,
            font_size=8
        ).pack()

        # Share 2
        share2_card = tk.Frame(
            shares_frame,
            bg=c["card"],
            height=210
        )

        share2_card.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(6, 0)
        )

        share2_card.pack_propagate(False)

        tk.Label(
            share2_card,
            text="SHARE 2",
            font=("Segoe UI", 11, "bold"),
            bg=c["card"],
            fg=c["text"]
        ).pack(pady=(10, 3))

        self.decryption_share2_label = tk.Label(
            share2_card,
            text="Not selected",
            font=("Segoe UI", 8),
            bg=c["card"],
            fg=c["secondary"]
        )

        self.decryption_share2_label.pack()

        self.decryption_share2_preview = tk.Label(
            share2_card,
            text="No Preview",
            bg=c["preview"],
            fg=c["secondary"],
            width=25,
            height=6
        )

        self.decryption_share2_preview.pack(pady=8)

        self.create_button(
            share2_card,
            "Select Share 2",
            self.select_decryption_share2,
            c["purple"],
            c["purple_hover"],
            width=18,
            font_size=8
        ).pack()

        # ================= SAVE LOCATION =================

        location_frame = tk.Frame(
            main,
            bg=c["card"],
            height=48
        )

        location_frame.pack(
            fill="x",
            pady=10
        )

        location_frame.pack_propagate(False)

        tk.Label(
            location_frame,
            text="Save Reconstructed Image:",
            font=("Segoe UI", 9, "bold"),
            bg=c["card"],
            fg=c["text"]
        ).pack(
            side="left",
            padx=12
        )

        self.decryption_location_label = tk.Label(
            location_frame,
            text="Not selected",
            font=("Segoe UI", 8),
            bg=c["card"],
            fg=c["secondary"]
        )

        self.decryption_location_label.pack(
            side="left"
        )

        self.create_button(
            location_frame,
            "Choose Folder",
            self.choose_decryption_location,
            c["blue"],
            c["blue_hover"],
            width=14,
            font_size=8
        ).pack(
            side="right",
            padx=10
        )

        # ================= RECONSTRUCT =================

        self.create_button(
            main,
            "🔓  RECONSTRUCT ORIGINAL IMAGE",
            self.reconstruct,
            c["red"],
            c["red_hover"],
            width=32,
            font_size=10
        ).pack(pady=7)

        # Progress
        style = ttk.Style()

        style.configure(
            "Decrypt.Horizontal.TProgressbar",
            troughcolor=c["preview"],
            background=c["red"],
            thickness=12
        )

        self.decryption_progress = ttk.Progressbar(
            main,
            style="Decrypt.Horizontal.TProgressbar",
            orient="horizontal",
            length=650,
            mode="determinate"
        )

        self.decryption_progress.pack(pady=3)

        self.decryption_status = tk.Label(
            main,
            text="Select Share 1 and Share 2",
            font=("Segoe UI", 8),
            bg=c["bg"],
            fg=c["secondary"]
        )

        self.decryption_status.pack()

        # ================= RESULT =================

        result_card = tk.Frame(
            main,
            bg=c["card"],
            height=160
        )

        result_card.pack(
            fill="x",
            pady=8
        )

        result_card.pack_propagate(False)

        tk.Label(
            result_card,
            text="RECONSTRUCTED IMAGE",
            font=("Segoe UI", 10, "bold"),
            bg=c["card"],
            fg=c["text"]
        ).pack(pady=(7, 2))

        self.reconstructed_preview = tk.Label(
            result_card,
            text="No reconstructed image yet",
            bg=c["preview"],
            fg=c["secondary"],
            width=30,
            height=5
        )

        self.reconstructed_preview.pack(pady=4)

    # =========================================================
    # SELECT SHARE 1
    # =========================================================

    def select_decryption_share1(self):

        downloads = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        file_path = filedialog.askopenfilename(
            title="Select Share 1",
            initialdir=downloads,
            filetypes=[
                ("PNG Images", "*.png"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:
            return

        self.selected_share1 = file_path

        self.decryption_share1_label.config(
            text=os.path.basename(file_path),
            fg=self.colors["green"]
        )

        self.show_image_preview(
            file_path,
            self.decryption_share1_preview,
            180,
            105
        )

        self.decryption_status.config(
            text="Share 1 selected"
        )

    # =========================================================
    # SELECT SHARE 2
    # =========================================================

    def select_decryption_share2(self):

        downloads = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        file_path = filedialog.askopenfilename(
            title="Select Share 2",
            initialdir=downloads,
            filetypes=[
                ("PNG Images", "*.png"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:
            return

        self.selected_share2 = file_path

        self.decryption_share2_label.config(
            text=os.path.basename(file_path),
            fg=self.colors["green"]
        )

        self.show_image_preview(
            file_path,
            self.decryption_share2_preview,
            180,
            105
        )

        self.decryption_status.config(
            text="Share 2 selected"
        )

    # =========================================================
    # DECRYPTION SAVE LOCATION
    # =========================================================

    def choose_decryption_location(self):

        folder = filedialog.askdirectory(
            title="Choose Reconstruction Save Location"
        )

        if not folder:
            return

        self.decryption_save_location = folder

        self.decryption_location_label.config(
            text=folder,
            fg=self.colors["green"]
        )

    # =========================================================
    # RECONSTRUCT
    # =========================================================

    def reconstruct(self):

        if not self.selected_share1:

            messagebox.showwarning(
                "Share 1 Missing",
                "Please select Share 1 first."
            )

            return

        if not self.selected_share2:

            messagebox.showwarning(
                "Share 2 Missing",
                "Please select Share 2 first."
            )

            return

        if not self.decryption_save_location:

            messagebox.showwarning(
                "Save Location Missing",
                "Please choose where to save the reconstructed image."
            )

            return

        try:

            self.decryption_progress["value"] = 20

            self.decryption_status.config(
                text="Preparing reconstruction..."
            )

            self.root.update_idletasks()

            output_path = os.path.join(
                self.decryption_save_location,
                "Reconstructed.png"
            )

            self.decryption_progress["value"] = 50

            self.decryption_status.config(
                text="Combining Share 1 and Share 2..."
            )

            self.root.update_idletasks()

            reconstruct_image(
                self.selected_share1,
                self.selected_share2,
                output_path
            )

            self.decryption_progress["value"] = 80

            self.decryption_status.config(
                text="Loading reconstructed image..."
            )

            self.root.update_idletasks()

            self.show_image_preview(
                output_path,
                self.reconstructed_preview,
                220,
                120
            )

            self.decryption_progress["value"] = 100

            self.decryption_status.config(
                text="Reconstruction completed successfully!"
            )

            messagebox.showinfo(
                "Reconstruction Complete",
                "Image reconstructed successfully!\n\n"
                f"Saved at:\n{output_path}"
            )

        except Exception as e:

            self.decryption_progress["value"] = 0

            self.decryption_status.config(
                text="Reconstruction failed"
            )

            messagebox.showerror(
                "Reconstruction Error",
                str(e)
            )

    # =========================================================
    # IMAGE PREVIEW
    # =========================================================

    def show_image_preview(
        self,
        file_path,
        label,
        width,
        height
    ):

        try:

            image = Image.open(file_path)

            image.thumbnail(
                (width, height)
            )

            photo = ImageTk.PhotoImage(image)

            label.config(
                image=photo,
                text=""
            )

            label.image = photo

        except Exception:

            label.config(
                text="Preview unavailable",
                image=""
            )


# =============================================================
# START APPLICATION
# =============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = VisualCryptographyApp(root)

    root.mainloop()