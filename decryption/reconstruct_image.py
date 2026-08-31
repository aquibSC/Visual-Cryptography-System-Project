from PIL import Image
import numpy as np


def reconstruct_image(share1_path, share2_path, output_path):
    # Open encrypted shares
    share1 = Image.open(share1_path).convert("RGB")
    share2 = Image.open(share2_path).convert("RGB")

    # Convert to NumPy arrays
    s1 = np.array(share1, dtype=np.uint8)
    s2 = np.array(share2, dtype=np.uint8)

    # XOR the two shares to recover the original image
    reconstructed = np.bitwise_xor(s1, s2)

    # Save recovered color image
    Image.fromarray(reconstructed).save(output_path)

    print("Original color image reconstructed successfully!")


if __name__ == "__main__":
    share1 = input("Enter Share 1 path: ")
    share2 = input("Enter Share 2 path: ")

    reconstruct_image(
        share1,
        share2,
        "sample-images/reconstructed.png"
    )