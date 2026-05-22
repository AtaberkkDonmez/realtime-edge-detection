# Real-Time Computer Vision Pipeline

## English

A real-time computer vision project developed using Python and OpenCV.

The project initially started as a basic edge detection application and gradually evolved into a persistent multi-object motion tracking system with real-time processing and background subtraction techniques.

---

## Features

### Version 1
- Real-time webcam capture
- Grayscale conversion
- Gaussian blur preprocessing
- Canny edge detection
- FPS counter
- Screenshot capture

---

### Version 2
- Frame differencing based motion detection
- Contour-based object detection
- Bounding box visualization
- Centroid tracking
- Motion trail visualization
- State-based motion handling

---

### Version 3 (Current)
- Background subtraction based motion segmentation
- Persistent multi-object tracking
- Object ID assignment
- Centroid distance matching
- Noise filtering
- False positive reduction
- Camera motion rejection attempts
- Real-time FPS monitoring
- Real-time object localization

---

## Technologies

- Python
- OpenCV
- NumPy

---

## How to Run

```bash
pip install -r requirements.txt
python3 motion_detection.py
```

---

## Controls

- Press `q` → quit application

---

## Project Purpose

This project was developed to explore real-time computer vision pipelines and understand the fundamentals of motion analysis, object tracking, and image processing systems used in embedded and defense-related applications.

---

## Covered Concepts

- Real-time frame processing
- Edge detection
- Image preprocessing
- Motion segmentation
- Background subtraction
- Contour extraction
- Object localization
- Persistent object tracking
- Centroid-based tracking logic
- False positive reduction
- Real-time FPS analysis

---

# Gerçek Zamanlı Bilgisayarlı Görü Pipeline Sistemi

## Türkçe

Python ve OpenCV kullanılarak geliştirilmiş gerçek zamanlı bilgisayarlı görü projesidir.

Proje başlangıçta basit bir kenar tespiti uygulaması olarak geliştirilmiş, daha sonra gerçek zamanlı persistent multi-object tracking sistemine dönüştürülmüştür.

---

## Özellikler

### Sürüm 1
- Gerçek zamanlı kamera görüntüsü
- Grayscale dönüşümü
- Gaussian blur ön işleme
- Canny edge detection
- FPS sayacı
- Ekran görüntüsü alma

---

### Sürüm 2
- Frame differencing ile hareket algılama
- Kontur tabanlı nesne tespiti
- Bounding box çizimi
- Centroid takibi
- Hareket izi görselleştirme
- State-based hareket yönetimi

---

### Sürüm 3 (Güncel)
- Background subtraction tabanlı hareket segmentasyonu
- Persistent multi-object tracking
- Nesne ID atama sistemi
- Centroid distance matching
- Gürültü filtreleme
- False positive azaltma
- Kamera hareketi filtreleme denemeleri
- Gerçek zamanlı FPS takibi
- Gerçek zamanlı nesne konumlandırma

---

## Kullanılan Teknolojiler

- Python
- OpenCV
- NumPy

---

## Çalıştırma

```bash
pip install -r requirements.txt
python3 motion_detection.py
```

---

## Kontroller

- `q` tuşu → uygulamadan çık

---

## Projenin Amacı

Bu proje gerçek zamanlı bilgisayarlı görü pipeline sistemlerini anlamak ve özellikle gömülü sistemler ile savunma sanayi uygulamalarında kullanılan motion analysis ve object tracking mantığını öğrenmek amacıyla geliştirilmiştir.

---

## Öğrenilen Konular

- Gerçek zamanlı frame işleme
- Kenar tespiti
- Görüntü ön işleme
- Motion segmentation
- Background subtraction
- Contour extraction
- Nesne konumlandırma
- Persistent object tracking
- Centroid tabanlı tracking mantığı
- False positive azaltma
- Gerçek zamanlı FPS analizi