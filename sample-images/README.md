# Sample Images

# Sample Images

This folder contains demonstration images used for validating the Visual Cryptography workflow.

## Image Files

| File              | Description                                          |
| ----------------- | ---------------------------------------------------- |
| original.png      | Original secret image                                |
| share1.png        | First encrypted share                                |
| share2.png        | Second encrypted share                               |
| reconstructed.png | Image reconstructed by combining Share 1 and Share 2 |

## Workflow

Original Image
|
v
Visual Cryptography Encryption
|
+------> Share 1
|
+------> Share 2
|
v
Share Superimposition
|
v
Reconstructed Secret Image

## Observation

* Share 1 alone reveals no meaningful information.
* Share 2 alone reveals no meaningful information.
* The original image becomes visible only after combining both shares.

This demonstrates the security property of the (2,2) Visual Cryptography Scheme used in this project.


