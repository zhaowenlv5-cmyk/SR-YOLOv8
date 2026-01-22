# 🚀 SR-YOLOv8
![Framework](https://img.shields.io/badge/Framework-YOLOv8-blue)
![Task](https://img.shields.io/badge/Task-Small%20Traffic%20Sign%20Detection-red)
![Learning](https://img.shields.io/badge/Learning-Multi--Task-purple)
![SR](https://img.shields.io/badge/Module-Super--Resolution-orange)

---

## 🎯 Overview
An end-to-end small traffic sign detection framework that incorporates **Super-Resolution (SR)** reconstruction and **small object detection** under a unified **multi-task learning** paradigm.

---

## 🧠 Pipeline
<img width="1200" height="649" alt="pipeline1" src="https://github.com/user-attachments/assets/fdcee413-4cfb-4a1a-b573-b8b16943248d" />

---
## 🏃 Keep updating 🏃:
- Trained model of SR-YOLOv8 on the CCTSDB2021 has been released.
- Training and testing code of SR-YOLOv8 has been released.
- Configuration file for SR-YOLOv8 has been released ([SRYOLOv8](SRyolov8.yaml)).
- Evaluation results of SR-YOLOv8 have been released.

---
## Requirements
-To install requirements:
```bash
pip install -r requirements.txt
```
---

## Usage
-Training: Please download the traffic sign training and testing sets: [CCTSDB2021 ](https://github.com/csust7zhangjm/CCTSDB2021), [TT100k]((https://cg.cs.tsinghua.edu.cn/traffic-sign), [GTSDB](https://benchmark.ini.rub.de/gtsdb_dataset.html).
-Fast Training: Download the [pre-trained model]() of SR-YOLOv8. Put it into <pretrained_models>.
-Run <train.py> to train SR-YOLOv8.




---
COMPARISON RESULTS ON CCTSDB2021 (%)
| Dataset | Algorithm | Venue | AP | AP50 | AP75 | APS | APM | APL |
|---------|-----------|-------|----|------|------|-----|-----|-----|
| CCTSDB | Faster R-CNN | TPAMI 2016 | 19.50 | 32.80 | 21.00 | 10.20 | 47.30 | 59.30 |
|  | Cascade R-CNN | TPAMI 2019 | 25.30 | 42.10 | 26.90 | 15.50 | 52.00 | 72.70 |
|  | Sparse R-CNN | CVPR 2021 | 31.20 | 60.50 | 29.80 | 25.80 | 50.20 | 63.40 |
|  | Deformable DETR | ICLR 2021 | 32.10 | 63.70 | 29.00 | 25.50 | 53.60 | 46.10 |
|  | YOLOv5s | 2020 | 39.98 | 70.52 | 41.27 | 34.85 | 57.08 | 38.54 |
|  | TPH-YOLOv5s | ICCV 2021 | 39.32 | 68.07 | 41.05 | 34.90 | 54.85 | 38.56 |
|  | YOLOv6s | arXiv 2022 | 41.30 | 67.20 | 44.90 | 36.10 | 58.90 | 43.50 |
|  | YOLOv7l | CVPR 2023 | 28.16 | 52.07 | 27.38 | 22.49 | 46.68 | 60.33 |
|  | DiffusionDet | ICCV 2023 | 43.30 | 72.50 | 46.80 | 39.70 | 58.60 |  **52.50** |
|  | SuperYOLO | TGRS 2024 | 49.47 | 81.69 | 55.37 | 45.91 | 61.96 | 43.54 |
|  | YOLO-MS | TPAMI 2025 | 41.40 | 69.20 | 44.60 | 36.10 | 59.40 | <ins>48.30 <ins>|
|  | YOLO-TS | TITS 2025 | <ins>55.34<ins> |<ins> 82.77 <ins>| <ins>65.87 <ins>| <ins>53.98 <ins>|<ins> 63.54 <ins>| 43.54 |
|  | YOLO-LLTS | TIM 2025 | 54.45 | 82.63 | 64.27 | 53.23 | 62.63 | 43.47 |
|  | YOLOv8 (baseline) | 2023 | 44.55 | 70.40 | 50.07 | 40.55 | 59.43 | 38.32 |
|  | **SR-YOLOv8s (ours)** | - | **56.12** | **84.04** | **67.34** | **54.72** | **63.66** | 38.56 |

COMPARISON RESULTS ON TT100k (%)
| Dataset | Algorithm | Venue | AP | AP50 | AP75 | APS | APM | APL |
|---------|-----------|-------|----|------|------|-----|-----|-----|
| TT100K | Faster R-CNN | TPAMI 2016 | 30.80 | 39.00 | 36.80 | 17.10 | 40.10 | 62.40 |
|  | Cascade R-CNN | TPAMI 2019 | 38.30 | 47.40 | 45.10 | 23.10 | 48.10 | 75.00 |
|  | Sparse R-CNN | CVPR 2021 | 36.30 | 46.60 | 43.10 | 32.60 | 44.20 | 68.50 |
|  | Deformable DETR | ICLR 2021 | 18.90 | 33.10 | 19.80 | 19.80 | 24.30 | 32.70 |
|  | YOLOv5s | 2020 | 40.19 | 50.66 | 47.56 | 41.41 | 47.14 | 68.47 |
|  | TPH-YOLOv5s | ICCV 2021 | 43.18 | 54.36 | 51.19 | 46.47 | 50.26 | 70.61 |
|  | YOLOv6s | arXiv 2022 | 35.70 | 45.20 | 41.80 | 30.10 | 44.00 | 63.00 |
|  | YOLOv7l | CVPR 2023 | 34.03 | 42.23 | 40.08 | 38.30 | 39.80 | 65.62 |
|  | DiffusionDet | ICCV 2023 | 56.40 | **71.90** | 67.40 | 54.00 | 62.10 | **82.10** |
|  | SuperYOLO | TGRS 2024 | 49.50 | 60.71 | 58.22 | 53.93 | 57.20 | 77.27 |
|  | YOLO-MS | TPAMI 2025 | 49.00 | 60.30 | 57.00 | 39.80 | 58.10 | 77.30 |
|  | YOLO-TS | TITS 2025 |  **58.72** | <ins>71.53<ins>| **68.34** | **57.52**| **65.09** | 75.42 |
|  | YOLO-LLTS | TIM 2025 | 45.55 | 57.31 | 54.34 | 47.93 | 52.87 | 64.19 |
|  | YOLOv8s (baseline) | 2023 | 44.28 | 55.10 | 52.43 | 39.64 | 53.45 | 70.74 |
|  | **SR-YOLOv8s (ours)** | - | <ins>57.46<ins> | 70.59 | <ins>67.85<ins> | <ins>54.86<ins> | <ins>64.66<ins> | <ins>78.43<ins> |

COMPARISON RESULTS ON GTSDB (%)
| Dataset | Algorithm | Venue | AP | AP50 | AP75 | APS | APM | APL |
|---------|-----------|-------|----|------|------|-----|-----|-----|
| GTSDB | Faster R-CNN | TPAMI 2016 | 61.60 | 84.50 | 73.80 | 32.50 | 74.10 | 93.10 |
|  | Cascade R-CNN | TPAMI 2019 | 66.80 | 87.40 | 78.40 | 38.70 | 78.70 | 91.30 |
|  | Sparse R-CNN | CVPR 2021 | 67.60 | 91.20 | 79.80 | 44.60 | 78.00 | 91.40 |
|  | Deformable DETR | ICLR 2021 | 64.70 | 92.20 | 74.90 | 40.40 | 75.40 | 84.30 |
|  | YOLOv5s | 2020 | 74.04 | 95.53 | 89.40 | 55.23 | 81.24 | 93.61 |
|  | TPH-YOLOv5s | ICCV 2021 | 76.74 | 95.80 | 91.68 | 69.01 | 82.14 | 80.54 |
|  | YOLOv6s | arXiv 2022 | 73.80 | 91.30 | 86.40 | 53.10 | 83.10 | 88.30 |
|  | YOLOv7l | CVPR 2023 | 53.28 | 72.86 | 64.52 | 26.51 | 64.60 | 78.73 |
|  | DiffusionDet | ICCV 2023 | 76.00 | 92.40 | 87.90 | 57.20 | 84.60 | 97.50 |
|  | SuperYOLO | TGRS 2024 | 78.02 | 96.34 | 92.87 | 62.52 | 85.21 | 89.58 |
|  | YOLO-MS | TPAMI 2025 | 74.90 | 93.80 | 87.20 | 52.00 | 84.10 | 97.90 |
|  | YOLO-TS | TITS 2025 | 77.44 | 97.57 | 94.18 | 63.07 | 84.10 | 82.00 |
|  | YOLO-LLTS | TIM 2025 | 74.00 | 96.53 | 92.03 | 63.79 | 79.53 | 69.94 |
|  | YOLOv8 (baseline) | 2023 | 79.07 | 97.95 | 94.35 | 66.82 | 84.98 | 91.29 |
|  | **SR-YOLOv8s (ours)** | - | **84.35** | **98.76** | **97.74** | **74.94** | **88.10** | **96.28** |




