# Blur Face Project

A Python project that detects faces in an image and applies a blur effect to protect the privacy of individuals.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

## Overview

The Blur Face project is a simple Python script that utilizes the OpenCV library to detect faces in an image and applies a blur effect to those faces. This can be useful for privacy protection when sharing images with identifiable individuals. The script uses a pre-trained Haar Cascade Classifier for face detection and applies a median blur to the detected faces.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/umairrrkhan/blur-face.git
   cd blur-face
   ```

2. Make sure you have Python and OpenCV installed. You can install OpenCV using pip:

```bash
pip install opencv-python
```
Download the Haar Cascade Classifier for face detection from the OpenCV GitHub repository and save it as 
```bash
haarcascade_frontalface_default.xml in the project directory.
```

## Usage
Place the image you want to process in the project directory, e.g., input_image.jpg.

Run the blur_face.py script:
Replace input_image.jpg with the filename of your input image and output_image.jpg with the desired output filename.

The script will detect faces in the input image and apply a blur effect to them.

The resulting image with blurred faces will be saved as output_image.jpg in the project directory.

## Examples

### imnput iamge
1. ![MESSI IMAGE](messi.jpg)

### output
2. ![blurred image](blurred_image.jpg)
