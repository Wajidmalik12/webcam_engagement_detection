# Webcam Engagement Detection

A real-time computer vision project that uses a trained **CNN model with TensorFlow/Keras** and a webcam to detect a person's engagement level.

The system continuously captures frames from the webcam, preprocesses them, runs the trained model, and displays the predicted engagement level with its confidence score directly on the camera feed.

## Features

* Real-time webcam detection
* CNN-based image classification
* Three engagement classes:

  * Disengaged
  * Highly Engaged
  * Moderately Engaged
* Real-time confidence score
* OpenCV-based camera interface
* TensorFlow/Keras model inference

## Tech Stack

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* CNN (Convolutional Neural Network)

## How It Works

```text
Webcam
   ↓
Capture Frame
   ↓
Resize to 224 × 224
   ↓
Convert BGR → RGB
   ↓
CNN Model
   ↓
Prediction
   ↓
Engagement Status + Confidence
   ↓
Display on Webcam
```

## Classes

The model predicts one of three classes:

| Class              | Description       |
| ------------------ | ----------------- |
| Disengaged         | Low engagement    |
| Highly Engaged     | High engagement   |
| Moderately Engaged | Medium engagement |

## Model

The trained CNN model expects images with the following input shape:

```text
224 × 224 × 3
```

The model produces three output classes corresponding to the engagement categories.

## Example Output

The webcam displays information similar to:

```text
Status: Highly Engaged
Confidence: 0.94
```

## Purpose

This project was built as a practical computer vision application to demonstrate how a trained CNN can be integrated with **OpenCV for real-time inference**.

It combines:

* Deep learning
* Image classification
* Computer vision
* Real-time webcam processing
* Model deployment/inference

## Future Improvements

* Face detection before classification
* Prediction smoothing across multiple frames
* FPS display
* Better confidence visualization
* Real-time engagement statistics
* Web-based interface
* Support for multiple people
* Improved model accuracy with a larger dataset

## Author

**Abdul Wajid Malik**

GitHub: [Wajidmalik12](https://github.com/Wajidmalik12)
