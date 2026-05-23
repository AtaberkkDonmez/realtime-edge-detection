# Real-Time AI Security Tracking System

## English

A real-time AI-assisted computer vision and security tracking system developed using Python, OpenCV, and YOLOv8.

The project initially started as a basic edge detection experiment and gradually evolved into a real-time human detection and persistent tracking pipeline using deep learning-based object detection techniques.

The system performs real-time person detection, multi-object tracking, intrusion monitoring, and trajectory visualization.

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

### Version 3
- Background subtraction based motion segmentation
- Persistent multi-object tracking
- Object ID assignment
- Noise filtering
- False positive reduction
- Camera motion rejection attempts

---

### Version 4 (Current)
- YOLOv8 real-time object detection
- Person-only tracking pipeline
- Persistent multi-object tracking using BoT-SORT
- Stable object ID assignment
- Trajectory visualization
- Restricted area monitoring
- Intrusion detection system
- Real-time confidence visualization
- Dynamic tracking buffer configuration
- Real-time FPS monitoring
- Unique ID session tracking
- Color-based ID visualization

---

## Technologies

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy
- BoT-SORT Tracker
- PyYAML

---

## How to Run

```bash
pip install -r requirements.txt
python3 yolo_tracking.py
```

---

## Controls

- `q` → quit application

---

## System Capabilities

The system can:

- Detect humans in real-time
- Track multiple people simultaneously
- Assign persistent IDs to detected people
- Visualize movement trajectories
- Monitor restricted areas
- Trigger intrusion warnings
- Maintain tracking consistency using BoT-SORT
- Display real-time FPS and tracking statistics

---

## Project Purpose

This project was developed to explore real-time AI-assisted computer vision pipelines and understand the core concepts behind object detection, tracking systems, and surveillance applications used in embedded, robotics, and defense-related systems.

---

## Covered Concepts

- Real-time frame processing
- Edge detection
- Motion segmentation
- Object detection
- Deep learning inference
- Persistent object tracking
- Trajectory analysis
- Multi-object tracking
- Background subtraction
- False positive reduction
- Intrusion detection systems
- Real-time performance analysis
- Tracking buffer management
- Region-of-interest (ROI) monitoring

---

# Gerçek Zamanlı Yapay Zeka Destekli Güvenlik Takip Sistemi

## Türkçe

Python, OpenCV ve YOLOv8 kullanılarak geliştirilmiş gerçek zamanlı yapay zeka destekli bilgisayarlı görü ve güvenlik takip sistemidir.

Proje başlangıçta basit bir kenar tespiti denemesi olarak geliştirilmiş, daha sonra derin öğrenme tabanlı insan tespiti ve persistent tracking sistemi haline dönüştürülmüştür.

Sistem gerçek zamanlı insan tespiti, çoklu nesne takibi, intrusion monitoring ve trajectory visualization işlemleri gerçekleştirmektedir.

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

### Sürüm 3
- Background subtraction tabanlı hareket segmentasyonu
- Persistent multi-object tracking
- Nesne ID sistemi
- Gürültü filtreleme
- False positive azaltma
- Kamera hareketi filtreleme denemeleri

---

### Sürüm 4 (Güncel)
- YOLOv8 gerçek zamanlı nesne tespiti
- Sadece insan takibi yapan pipeline
- BoT-SORT tabanlı persistent tracking
- Stabil object ID sistemi
- Trajectory visualization
- Restricted area monitoring
- Intrusion detection sistemi
- Gerçek zamanlı confidence gösterimi
- Dinamik tracking buffer yönetimi
- FPS takibi
- Unique ID session tracking
- ID bazlı renk sistemi

---

## Kullanılan Teknolojiler

- Python
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy
- BoT-SORT Tracker
- PyYAML

---

## Çalıştırma

```bash
pip install -r requirements.txt
python3 yolo_tracking.py
```

---

## Kontroller

- `q` tuşu → uygulamadan çık

---

## Sistem Yetenekleri

Sistem:

- Gerçek zamanlı insan tespiti yapabilir
- Aynı anda birden fazla insanı takip edebilir
- Her insan için persistent ID oluşturabilir
- Hareket geçmişini görselleştirebilir
- Restricted area kontrolü yapabilir
- Intrusion warning üretebilir
- BoT-SORT ile tracking stabilitesini artırabilir
- FPS ve tracking istatistiklerini gösterebilir

---

## Projenin Amacı

Bu proje gerçek zamanlı yapay zeka destekli bilgisayarlı görü pipeline sistemlerini öğrenmek ve özellikle gömülü sistemler, robotik ve savunma sanayi uygulamalarında kullanılan object detection ve tracking sistemlerinin temel mantığını anlamak amacıyla geliştirilmiştir.

---

## Öğrenilen Konular

- Gerçek zamanlı frame işleme
- Kenar tespiti
- Motion segmentation
- Object detection
- Deep learning inference
- Persistent object tracking
- Trajectory analysis
- Multi-object tracking
- Background subtraction
- False positive azaltma
- Intrusion detection sistemleri
- Gerçek zamanlı performans analizi
- Tracking buffer yönetimi
- ROI (Region of Interest) monitoring