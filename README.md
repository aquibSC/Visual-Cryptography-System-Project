# 🔐 Visual Cryptography System

A Python-based Visual Cryptography System that securely converts an image into two encrypted visual shares. The original image can be reconstructed only by combining both shares.

## 📌 About the Project

Visual Cryptography is a cryptographic technique that allows a secret image to be divided into multiple shares.

In this project, the original image is converted into two pixel-based encrypted shares. Individually, the shares do not reveal the original image. The original image is reconstructed by manually selecting and combining both shares.

The project includes a graphical user interface built with Python and Tkinter.

---

## ✨ Features

- 🔐 Image encryption using visual cryptography
- 🧩 Generation of two encrypted shares
- 🖼️ Pixel-based encrypted share representation
- 🔓 Manual reconstruction using Share 1 and Share 2
- 📂 Select images directly from the file system
- 💾 Custom save location for encrypted shares
- 💾 Custom save location for reconstructed images
- 🖼️ Image previews inside the GUI
- 📊 Encryption and reconstruction progress indicators
- 🌙 Dark mode / light mode interface
- 🖥️ Desktop GUI using Tkinter
- 📁 Organized project structure

---

## 🔐 Encryption Process

The encryption process follows these steps:

1. Select the original image.
2. Choose a folder where the encrypted shares should be saved.
3. Click **Generate Encrypted Shares**.
4. The system processes the image pixel-by-pixel.
5. Two encrypted shares are generated.
6. Share 1 and Share 2 can be stored separately.
7. Each share can be viewed as a pixel-based encrypted image.

### Encryption Workflow

```text
Original Image
      │
      ▼
Pixel Processing
      │
      ▼
┌───────────────┐
│ Visual        │
│ Cryptography  │
└───────────────┘
      │
      ├──────────────► Share 1
      │
      └──────────────► Share 2
### Encryption Workflow
Share 1 ──────┐
              │
              ▼
        Share Combination
              │
              ▼
     Reconstructed Image
              ▲
              │
Share 2 ──────┘
🖥️ Graphical User Interface

The application contains three main sections:

Home Page

The Home Page allows the user to choose between:

🔐 Encryption
🔓 Decryption
Encryption Page

The Encryption Page provides:

Original image selection
Image preview
Custom save location
Encrypted share generation
Progress indicator
Share 1 preview
Share 2 preview
Decryption Page

The Decryption Page provides:

Share 1 selection
Share 2 selection
Share previews
Custom output location
Manual reconstruction
Reconstruction progress
Reconstructed image preview
Visual-Cryptography-System
│
├── algorithms/
│
├── architecture/
│
├── decryption/
│   └── reconstruct_image.py
│
├── encryption/
│   └── generate_shares.py
│
├── reports/
│
├── sample-images/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── SECURITY.md
└── CONTRIBUTING.md
 Author

MD Aquib Hussain

GitHub:
https://github.com/aquibSC

📄 License

This project is licensed under the MIT License.
