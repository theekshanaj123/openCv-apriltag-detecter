# 📷 AprilTag Detection and Color Detection with Arduino Trigger

This project captures an image via webcam when triggered by an Arduino, detects **AprilTags** in the image, and is set up for future **color detection**.

---

## 🚀 Features

- Listens for a trigger signal from Arduino over **Serial Communication**.
- Captures an image from a **Webcam** when triggered.
- Detects **AprilTags** using the `pyapriltags` library.
- Picks the best tag based on the **decision margin** (confidence).
- Color detection placeholder is included for future expansion.

---

## 🛠️ Requirements

- Python 3.x
- Libraries:
  - `opencv-python`
  - `pyserial`
  - `pyapriltags`
  - `numpy`

Install dependencies with:

```bash
pip install opencv-python pyserial pyapriltags numpy
