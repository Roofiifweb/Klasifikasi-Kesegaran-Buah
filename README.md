# 🍎🍊🍌 Klasifikasi Kesegaran Buah Apel, Jeruk, dan Pisang

## 📌 Deskripsi Proyek
Proyek ini merupakan implementasi sistem **klasifikasi citra kesegaran buah** menggunakan pendekatan **Deep Learning** berbasis **Convolutional Neural Network (CNN)** dan **Transfer Learning**. Sistem ini mengklasifikasikan citra buah ke dalam dua kondisi utama, yaitu **Segar (Fresh)** dan **Busuk (Rotten)** pada tiga jenis buah: **Apel, Jeruk, dan Pisang**.

Proyek ini dikembangkan sebagai bagian dari **Ujian Akhir Praktikum (UAP) Mata Kuliah Pembelajaran Mesin** dan diimplementasikan dalam aplikasi web interaktif menggunakan **Streamlit**.

---

## 🗂️ Dataset
- **Nama Dataset**: Fresh and Rotten Fruits Image Dataset  
- **Sumber**: https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification 
- **Jumlah Kelas**: 6  
  - Fresh Apple  
  - Fresh Banana  
  - Fresh Orange  
  - Rotten Apple  
  - Rotten Banana  
  - Rotten Orange  

### 📊 Distribusi Data Training
| Kelas | Jumlah Gambar |
|------|---------------|
| Fresh Apple | 1.693 |
| Rotten Apple | 2.342 |
| Fresh Banana | 1.581 |
| Rotten Banana | 2.224 |
| Fresh Orange | 1.466 |
| Rotten Orange | 1.595 |

**Total Data Training: 10.901 citra**

---

## ⚙️ Preprocessing & Augmentasi
- Resize citra menjadi **150 × 150 piksel**
- Normalisasi nilai piksel (`rescale = 1/255`)
- Augmentasi citra:
  - Rotasi
  - Zoom
  - Horizontal Flip
- Pembagian data training dan validation menggunakan `validation_split = 0.2`

---

## 🧠 Model yang Digunakan

### 1️⃣ CNN Base (Non-Pretrained)
Model CNN yang dilatih dari awal tanpa bobot pretrained. Digunakan sebagai **baseline** untuk membandingkan performa dengan model transfer learning.

### 2️⃣ MobileNetV2 (Pretrained)
Model pretrained **MobileNetV2** dengan bobot **ImageNet**. Model ini ringan, efisien, dan cocok untuk aplikasi berbasis web.

### 3️⃣ VGG16 (Pretrained)
Model pretrained **VGG16** dengan bobot **ImageNet** yang memiliki kemampuan ekstraksi fitur visual yang kuat, namun membutuhkan resource komputasi lebih besar.

---

## 📈 Evaluasi Model
Evaluasi dilakukan menggunakan data validation dengan metrik:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Grafik Loss dan Accuracy

---

## 📌 Catatan Penyimpanan Model
Model **CNN Base (Non-Pretrained)** tidak disertakan dalam repository GitHub karena ukuran file model yang cukup besar.

Namun:
- Model tetap dilatih dan dievaluasi secara penuh
- Digunakan sebagai baseline analisis
- Hasil evaluasi disertakan dalam laporan

Model **MobileNetV2** dan **VGG16** disertakan dan digunakan pada aplikasi Streamlit.

---

## 🌐 Implementasi Website (Streamlit)
Aplikasi web dikembangkan menggunakan **Streamlit** dengan fitur:
- Upload citra buah
- Pemilihan model (CNN Base, MobileNetV2, VGG16)
- Menampilkan hasil klasifikasi **Segar / Busuk**
- Menampilkan confidence score dan probabilitas tiap kelas

---

## 📁 Struktur Folder



---
