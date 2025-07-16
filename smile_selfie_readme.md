# 📸 Smile Selfie Capture Project

This project captures selfies **automatically when you smile**, using OpenCV with real-time webcam detection. Selfies are saved to your **desired folder location** with a popup **"Clicked Selfie!"** shown on the video feed.

---

## ✅ Features

- Real-time **face and smile detection** using OpenCV Haar Cascades.
- **Selfie saved automatically** when you smile.
- Displays **“Clicked Selfie!”** on the live camera feed.
- Saves images to your **custom folder**.
- **One image per smile** (avoids duplicates).
- **Press **``** to quit** anytime.

---

## 📂 Project Structure

```
Smile Selfie Capture Project/
│
├── dataset/
│   ├── haarcascade_frontalface_default.xml
│   └── haarcascade_smile.xml
│
├── Selfies Clicked/
│   └── (Captured selfies will be saved here)
│
└── main.py
└── README.md
```

---

## ⚙️ Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- Haar Cascade XML files (included in `dataset/`)

---

## 💻 Installation

```bash
pip install opencv-python
```

---

## 🚀 How to Run

```bash
python main.py
```

- Smile at the camera 😊
- Selfie will be automatically captured with an on-screen message.
- Press `` to close the camera.

---

## 📁 Changing Save Location

In `main.py`, you can set your own folder to save selfies:

```python
save_directory = r"E:\Machine-Learning-Projects\Smile Selfie Capture Project\Selfies Clicked"
```

---

## 📢 Example Output

- ✅ Selfie saved at:\
  `E:\Machine-Learning-Projects\Smile Selfie Capture Project\Selfies Clicked\selfie_1.jpg`
- ✅ Live pop-up on camera screen: “Clicked Selfie!”
- ✅ Terminal message: “Clicked Selfie! Saved at: [path]”

---

## 👏 Credits

Built using **OpenCV** Haar Cascades.

