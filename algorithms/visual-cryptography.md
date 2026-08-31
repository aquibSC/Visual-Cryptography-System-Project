# Visual Cryptography Algorithm

## Objective

Visual cryptography divides a secret image into multiple shares such that the original image becomes visible only when the required shares are combined.

## (2,2) Visual Cryptography Scheme

This project implements a **2-out-of-2 visual cryptography scheme**, where:

* Share 1 alone reveals nothing.
* Share 2 alone reveals nothing.
* Share 1 + Share 2 reconstruct the secret image.

## Basic Principle

For each pixel of the original image:

### White Pixel

Randomly choose one of the following patterns:

Pattern A

Share 1: █░
Share 2: █░

Pattern B

Share 1: ░█
Share 2: ░█

Result after superimposition: Gray appearance

### Black Pixel

Randomly choose one of the following patterns:

Pattern A

Share 1: █░
Share 2: ░█

Pattern B

Share 1: ░█
Share 2: █░

Result after superimposition: Black appearance

## Algorithm Steps

1. Load the input image.
2. Convert the image to binary form.
3. For each pixel:

   * Generate a random pattern.
   * Create corresponding patterns in Share 1 and Share 2.
4. Save both encrypted shares.
5. Reconstruct the image by superimposing the shares.

## Security Analysis

The probability of correctly guessing a secret pixel from a single share is 50%, making individual shares computationally useless for recovering the original image.

## Advantages

* No decryption key required
* Human visual system performs reconstruction
* Strong information hiding
* Simple implementation
* Suitable for authentication systems

## Applications

* Secure image authentication
* Digital watermarking
* Secret document sharing
* Identity verification
* Medical image protection
