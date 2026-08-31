from PIL import Image
import numpy as np
import random


def generate_shares(input_image_path, share1_path, share2_path):
    # Open original image
    img = Image.open(input_image_path).convert("RGB")

    # Convert image to numpy array
    img_array = np.array(img, dtype=np.uint8)

    # Create two empty shares
    share1 = np.zeros_like(img_array)
    share2 = np.zeros_like(img_array)

    height, width, channels = img_array.shape

    # Encrypt every pixel
    for i in range(height):
        for j in range(width):

            pixel = img_array[i, j]

            # Generate random pixel values
            random_pixel = np.array([
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            ], dtype=np.uint8)

            # Share 1 gets random pixel
            share1[i, j] = random_pixel

            # Share 2 gets XOR encrypted pixel
            share2[i, j] = np.bitwise_xor(pixel, random_pixel)

    # Save encrypted shares
    Image.fromarray(share1).save(share1_path)
    Image.fromarray(share2).save(share2_path)

    print("Pixel encryption completed!")
    print("Share 1:", share1_path)
    print("Share 2:", share2_path)


if __name__ == "__main__":
    input_image = input("Enter image path: ")

    generate_shares(
        input_image,
        "sample-images/share1.png",
        "sample-images/share2.png"
    )