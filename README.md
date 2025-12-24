# 🍎🍊🍌 Klasifikasi Kesegaran Buah Apel, Jeruk, dan Pisang

## 📌 Deskripsi Proyek
Proyek ini merupakan implementasi sistem **klasifikasi citra kesegaran buah** menggunakan pendekatan **Deep Learning** berbasis **Convolutional Neural Network (CNN)** dan **Transfer Learning**. Sistem ini mengklasifikasikan citra buah ke dalam dua kondisi utama, yaitu **Segar (Fresh)** dan **Busuk (Rotten)** pada tiga jenis buah: **Apel, Jeruk, dan Pisang**.

Proyek ini dikembangkan sebagai bagian dari **Ujian Akhir Praktikum (UAP) Mata Kuliah Pembelajaran Mesin** dan diimplementasikan dalam aplikasi web interaktif menggunakan **Streamlit**.

---
## 📝 Latar Belakang

Buah merupakan komoditas pangan yang banyak dikonsumsi masyarakat karena kandungan gizi dan manfaat kesehatannya. Namun, kualitas buah sangat dipengaruhi oleh tingkat kesegarannya. Buah yang telah mengalami pembusukan tidak hanya menurunkan nilai jual, tetapi juga dapat membahayakan kesehatan konsumen apabila dikonsumsi.

Penilaian kesegaran buah secara manual umumnya masih mengandalkan pengamatan visual oleh manusia, yang bersifat subjektif dan rentan terhadap kesalahan, terutama ketika jumlah buah yang harus diperiksa cukup banyak. Oleh karena itu, diperlukan suatu sistem otomatis yang mampu melakukan klasifikasi kesegaran buah secara cepat, konsisten, dan akurat.

Perkembangan teknologi **Deep Learning**, khususnya **Convolutional Neural Network (CNN)**, memungkinkan komputer untuk mengenali pola visual pada citra digital dengan tingkat akurasi yang tinggi. Dengan memanfaatkan teknik **Transfer Learning** menggunakan model pretrained seperti **MobileNetV2** dan **VGG16**, proses klasifikasi citra dapat dilakukan secara lebih efisien meskipun dengan jumlah data yang terbatas.

Berdasarkan permasalahan tersebut, proyek ini dikembangkan untuk membangun sistem klasifikasi citra kesegaran buah **apel, jeruk, dan pisang** ke dalam kategori **segar** dan **busuk** menggunakan pendekatan deep learning. Sistem ini diharapkan dapat menjadi solusi pendukung dalam proses sortasi buah serta sebagai media pembelajaran penerapan pembelajaran mesin dalam bidang pengolahan citra.

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

## 📊 Hasil Evaluasi dan Analisis Perbandingan Model

Berikut adalah tabel perbandingan performa ketiga arsitektur model berdasarkan pengujian pada dataset klasifikasi kesegaran buah:

| Nama Model | Akurasi | Macro Avg F1-Score | Weighted Avg F1-Score | Hasil Analisis |
| :--- | :---: | :---: | :---: | :--- |
| **CNN Base** | **0.16** | **0.11** | **0.10** | Performa sangat rendah. Model gagal mempelajari pola fitur dengan baik (terindikasi *underfitting*) dan memiliki presisi 0 pada beberapa kelas. |
| **MobileNetV2** | **1.00** | **1.00** | **1.00** | **Model Terbaik.** Mencapai skor sempurna di semua metrik. Sangat efisien dan akurat untuk klasifikasi 6 jenis kondisi buah. |
| **VGG16** | **1.00** | **1.00** | **1.00** | Performa sangat tinggi dan stabil. Menunjukkan kemampuan ekstraksi fitur yang sangat kuat meskipun arsitekturnya lebih berat dibanding MobileNetV2. |

> [!TIP]
> **Kesimpulan Pengujian:**
> Berdasarkan hasil di atas, **MobileNetV2** adalah pilihan paling ideal untuk deployment karena memberikan akurasi maksimum (100%) namun dengan struktur model yang lebih ringan dibandingkan VGG16.
---
# 🖼️ Visualisasi Performa

Berikut adalah bukti visualisasi hasil pelatihan (**Confusion Matrix** & **Grafik Loss**).

Berikut adalah bukti visualisasi hasil pelatihan (**Confusion Matrix** & **Grafik Loss**).

### 1. Analisis Custom CNN

| Confusion Matrix | Grafik Training |
| :---: | :---: |
| <img width="500" src="https://github.com/user-attachments/assets/5fe3d4c2-396c-42ff-bb32-7ef74be289f3" /> | <img width="500" src="https://github.com/user-attachments/assets/5101de2c-7c65-4d98-a925-043096ddfe34" /> |

### 2. Analisis Pre-trained Model (MobileNetV2)

| Confusion Matrix | Grafik Training |
| :---: | :---: |
| <img width="450" src="https://github.com/user-attachments/assets/410a2fa5-44a0-42fd-accf-5b67e009c4d3" /> | <img width="550" src="https://github.com/user-attachments/assets/9ce3d836-9835-4b01-8e61-2e83d860e835" /> |

### 3. Analisis Model Perbandingan (VGG16)

| Confusion Matrix | Grafik Training |
| :---: | :---: |
| <img width="450" src="https://github.com/user-attachments/assets/5a2b131c-a15a-4465-9930-5a0baa73d366" /> | <img width="550" src="https://github.com/user-attachments/assets/feaa971c-20b1-4e75-9cc6-5c33388f8164" /> |

---

## 💾 Unduh Model (Wajib)

Dikarenakan ukuran file yang besar, model **TIDAK** disertakan dalam repository ini. Anda wajib mengunduhnya dari Google Drive agar aplikasi dapat berjalan.

👉 **[Klik Disini untuk Mengunduh Model (Google Drive)](https://drive.google.com/drive/folders/1ZTu9TzxS3_9CYWaEV2rxdM4IkW72SvEY?usp=sharing)**

### 📂 Panduan Penempatan File:

1. Unduh file model: `model_base.h5`, `model_mobilenet.h5`, dan `model_vgg16.h5`.
2. Letakkan file tersebut di dalam folder `model/` di direktori utama proyek.

**Struktur akhir folder Anda harus terlihat seperti ini:**

```text
STREAMLITE ML/
│
├── model/
│   ├── model_base.h5
│   ├── model_mobilenet.h5
│   └── model_vgg16.h5
│
├── streamliteml.py
├── requirements.txt

```
---
##### 👤 Biodata Penulis

- **Nama** : Muhammad Roofiif Aflah Robbaanii  
- **NIM** : 202210370311152
- **Program Studi** : Informatika  
- **Fakultas** : Teknik  
- **Universitas** : Universitas Muhammadiyah Malang  






