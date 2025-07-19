#  Camera Pose Estimation

This repository contains a simple and effective pipeline for **estimating camera pose** from a 2D image using known 3D-2D point correspondences. The solution is implemented in Python with OpenCV and NumPy, and is ideal for educational, robotics, and computer vision applications.

---

##  Repository Structure

```

CameraPoseEstimation/
├── Data.zip                   # Contains image and calibration files
├── FinalCode.py              # Main script for pose estimation
├── Image.jpg                 # Input image used for pose estimation
├── intrinsics.npy            # Camera intrinsics matrix
├── world\_coordinates.npy     # 3D world coordinates of feature points
├── Task January 2024          # Project Report

````

---

## What It Does

Given:
- A **2D image** of a scene (`Image.jpg`)
- Known **3D world coordinates** (`world_coordinates.npy`)
- Known **camera intrinsics** (`intrinsics.npy`)

The script:
1. Detects or selects corresponding 2D image points.
2. Uses OpenCV's `solvePnP` function to estimate the camera's pose (rotation and translation).
3. Projects the 3D points back onto the image to visualize accuracy.

---

##  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/shreehank22/CameraPoseEstimation.git
cd CameraPoseEstimation
````

### 2. Install Dependencies

Make sure you have Python 3.7+ and install the required packages:

```bash
pip install numpy opencv-python
```

### 3. Run the Code

```bash
python FinalCode.py
```

This will:

* Load `Image.jpg`, camera intrinsics, and world coordinates.
* Estimate camera pose.
* Project 3D points back onto the image and display the result.

---

## 🧾 Files Explained

| File                    | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| `FinalCode.py`          | Main script that runs the pose estimation            |
| `Image.jpg`             | Image containing the object or scene                 |
| `intrinsics.npy`        | Precomputed 3×3 camera intrinsics matrix             |
| `world_coordinates.npy` | Nx3 array of 3D points in world coordinates          |
| `Data.zip`              | Archive containing the above files (optional backup) |

---

##  Output Example

The script will display the image with projected 3D points (after pose estimation), allowing visual verification of pose accuracy.

---

##  Pose Estimation Details

Uses:

* OpenCV's `cv2.solvePnP()` for pose estimation.
* `cv2.projectPoints()` to visualize the re-projected 3D points.

This approach assumes a pinhole camera model and relies on accurate 2D–3D correspondences.

---

##  Author

**Shreehan Kate**

## 💬 Feedback / Contributions

Contributions and suggestions are welcome!
Feel free to open an issue or submit a pull request.

```

