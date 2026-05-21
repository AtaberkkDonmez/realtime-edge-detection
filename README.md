# Real-Time Computer Vision Pipeline

## English

A real-time computer vision project developed using Python and OpenCV.  
The project started with edge detection and evolved into a motion tracking system with state-based logic.

---

## Features

### Version 1
- Real-time webcam capture
- Grayscale conversion
- Gaussian blur preprocessing
- Canny edge detection
- FPS counter
- Screenshot capture

### Version 2 (Updated)
- Frame differencing based motion detection
- Contour-based object detection
- Bounding box visualization
- Centroid (object center) tracking
- Motion trail visualization
- State-based motion handling (prevents artifact accumulation)

---

## Technologies

- Python
- OpenCV
- NumPy

---

## How to Run

```bash
pip install -r requirements.txt
python3 main.py
```

---

## Controls

- Press `s` → save screenshot
- Press `q` → quit program

---

## Project Purpose

This project was developed to explore real-time computer vision concepts and build an understanding of vision pipelines used in embedded and defense-related systems.

### Covered Concepts:
- Frame processing pipelines
- Edge detection techniques
- Motion detection using frame differencing
- Object localization and tracking
- Temporal state management in vision systems
- Real-time performance monitoring (FPS)

---

# Gerçek Zamanlı Bilgisayarlı Görü

## Türkçe

Python ve OpenCV kullanılarak geliştirilmiş gerçek zamanlı bilgisayarlı görü projesidir.  
Proje ilk olarak kenar tespiti ile başlamış, daha sonra hareket takibi içeren bir sisteme dönüştürülmüştür.

---

## Özellikler

### Sürüm 1
- Gerçek zamanlı kamera görüntüsü
- Grayscale dönüşümü
- Gaussian blur ön işleme
- Canny edge detection
- FPS sayacı
- Ekran görüntüsü alma

### Sürüm 2 (Güncellenmiş)
- Frame differencing ile hareket algılama
- Kontur tabanlı nesne tespiti
- Bounding box çizimi
- Merkez (centroid) takibi
- Hareket izi görselleştirme
- State-based (durum bazlı) iz yönetimi

---

## Kullanılan Teknolojiler

- Python
- OpenCV
- NumPy

---

## Çalıştırma

```bash
pip install -r requirements.txt
python3 main.py
```

---

## Kontroller

- `s` tuşu → ekran görüntüsü kaydet
- `q` tuşu → programdan çık

---

## Projenin Amacı

Bu proje gerçek zamanlı bilgisayarlı görü sistemlerini anlamak ve özellikle savunma sanayi ve gömülü sistemlerde kullanılan görüntü işleme pipeline mantığını öğrenmek amacıyla geliştirilmiştir.

### Öğrenilen Konular:
- Frame processing pipeline
- Kenar tespiti algoritmaları
- Hareket algılama
- Nesne konumlandırma ve takip
- Görüntü sistemlerinde state management
- Gerçek zamanlı performans analizi (FPS)