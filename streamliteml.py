import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

# ==============================
# KONFIGURASI HALAMAN
# ==============================
st.set_page_config(
    page_title="Fruit Quality Classifier",
    page_icon="🍎",
    layout="centered"
)

# ==============================
# JUDUL & DESKRIPSI
# ==============================
st.title("🍎 Klasifikasi Kesegaran Buah")
st.markdown("""
Aplikasi ini menggunakan **Deep Learning (CNN)** untuk mengklasifikasikan
buah **Apel, Pisang, dan Jeruk** ke dalam kondisi:

- ✅ **Segar**
- ❌ **Busuk**

Silakan pilih model dan unggah gambar buah.
""")

# ==============================
# SIDEBAR - PILIH MODEL
# ==============================
st.sidebar.header("⚙️ Pengaturan Model")

model_option = st.sidebar.selectbox(
    "Pilih Model:",
    (
        "CNN Base (Non-Pretrained)",
        "MobileNetV2 (Pretrained)",
        "VGG16 (Pretrained)"
    )
)

# ==============================
# PATH DASAR PROYEK
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==============================
# LOAD MODEL (CACHE)
# ==============================
@st.cache_resource
def load_prediction_model(option):
    model_files = {
        "CNN Base (Non-Pretrained)": "model_base.h5",
        "MobileNetV2 (Pretrained)": "model_mobilenet.h5",
        "VGG16 (Pretrained)": "model_vgg16.h5"
    }

    file_name = model_files[option]

    # 🔑 PATH MODEL YANG BENAR
    model_path = os.path.join(BASE_DIR, "model", file_name)

    if not os.path.exists(model_path):
        return None, model_path

    model = tf.keras.models.load_model(model_path)
    return model, model_path

# ==============================
# INISIALISASI MODEL
# ==============================
model, model_path = load_prediction_model(model_option)

if model is None:
    st.sidebar.error("❌ Model tidak ditemukan")
    st.sidebar.write("Path dicek:")
    st.sidebar.code(model_path)
    st.stop()
else:
    st.sidebar.success("✅ Model berhasil dimuat")
    st.sidebar.write("Model path:")
    st.sidebar.code(model_path)

# ==============================
# UPLOAD GAMBAR
# ==============================
uploaded_file = st.file_uploader(
    "📤 Unggah gambar buah",
    type=["jpg", "jpeg", "png"]
)

# ==============================
# NAMA KELAS (SESUSAI TRAINING)
# ==============================
class_names = [
    "Fresh Apple",
    "Fresh Banana",
    "Fresh Orange",
    "Rotten Apple",
    "Rotten Banana",
    "Rotten Orange"
]

# ==============================
# PROSES PREDIKSI
# ==============================
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Gambar yang diunggah",
        use_container_width=True
    )

    st.write("---")

    if st.button("🔍 Klasifikasikan Sekarang"):
        with st.spinner("Sedang memproses..."):
            # Preprocessing
            img = image.resize((150, 150))
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = img_array / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Prediksi
            predictions = model.predict(img_array)
            class_index = np.argmax(predictions)
            confidence = np.max(predictions) * 100
            label = class_names[class_index]

        st.subheader("📊 Hasil Prediksi")

        if "Fresh" in label:
            st.success(f"✅ **{label.upper()}**")
        else:
            st.error(f"❌ **{label.upper()}**")

        st.write(f"**Tingkat Kepercayaan:** {confidence:.2f}%")

        st.write("### Detail Probabilitas:")
        for i, class_name in enumerate(class_names):
            st.write(class_name)
            st.progress(float(predictions[0][i]))

# ==============================
# FOOTER
# ==============================
st.write("---")
st.caption("Ujian Akhir Praktikum - Pembelajaran Mesin | Informatika UMM 2025")
