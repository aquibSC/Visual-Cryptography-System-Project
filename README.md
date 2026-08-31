# Visual-Cryptography-System
Python-based Visual Cryptography System for secure image authentication, secret image sharing, and digital watermarking using Pillow (PIL) and pixel-level image encryption.

<h1 align="center">Visual Cryptography System for Secure Image Authentication</h1>

<p align="center"><b>Python • Pillow (PIL) • Cryptography • Information Security • Image Processing</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" />
  <img src="https://img.shields.io/badge/Cryptography-Visual%20Cryptography-green" />
  <img src="https://img.shields.io/badge/Image%20Processing-Pillow-orange" />
  <img src="https://img.shields.io/badge/Status-Security%20Project-purple" />
</p>

---

## Overview

This project implements a **Visual Cryptography System** that securely encrypts an image into multiple independent shares. The original image becomes visible only when the required shares are combined (superimposed). Individual shares appear as random noise and reveal no meaningful information, making the technique suitable for secure image authentication, confidential image sharing, and digital watermarking applications.

## Problem Statement

Traditional image encryption methods require computational decryption algorithms and secret keys. Visual cryptography enables secure image sharing by dividing a secret image into multiple shares that can be visually reconstructed without exposing the original image through any single share.

## Objectives

* Encrypt images into multiple independent shares.
* Prevent information leakage from individual shares.
* Reconstruct the original image through share superimposition.
* Explore cryptographic techniques for secure image authentication.
* Demonstrate applications in digital watermarking and confidential image sharing.

## Key Features

* Visual cryptography-based image encryption
* Pixel-level image processing using Python
* Multi-share secret image generation
* Secure image reconstruction
* Randomized share generation
* Digital watermarking and authentication concepts

## Technologies Used

* Python
* Pillow (PIL)
* NumPy
* Image Processing
* Cryptography Concepts
* Information Security

## Repository Structure

Visual-Cryptography-System/
├── README.md
├── architecture/
├── algorithms/
├── encryption/
├── decryption/
├── sample-images/
├── reports/
└── requirements.txt

## Security Advantages

* Individual shares reveal no useful information.
* No secret key is required for visual reconstruction.
* Resistant to single-share compromise.
* Suitable for secure authentication systems.

## Applications

* Secure image authentication
* Confidential document sharing
* Digital watermarking
* Identity verification systems
* Medical image protection
* Multi-share secret image distribution

## Future Enhancements

* Support for color images
* Multi-level visual cryptography
* QR-code based secret sharing
* Threshold cryptography (k-out-of-n)
* Mobile and web deployment

## Author

Nitish Kumar

gmail: nitishcse4@gmail.com 

https://www.github.com/whoisni30

https://www.linkedin.com/in/nitish-kumar-69b32b232/
