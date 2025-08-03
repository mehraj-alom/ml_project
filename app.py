import streamlit as st
import os
import shutil
import time
from PIL import Image
from src.Classifier.pipeline.predict import PredictionPipeline
from src.Classifier.pipeline.stage_03_training import ModelTrainingPipeline


ARTIFACT_DIR = "artifacts/training"
TEMP_DIR = "temp"
os.makedirs(ARTIFACT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

# ---------- Training Button ----------
if st.sidebar.button("Train Model"):
    st.sidebar.write("Training started...")
    try:
        trainer = ModelTrainingPipeline()
        trainer.main()
        st.sidebar.success("✅ Training complete!")
    except Exception as e:
        st.sidebar.error(f"❌ Training failed: {str(e)}")


# ---------- Model Selector ----------
def get_model_list():
    return [f for f in os.listdir(ARTIFACT_DIR) if f.endswith(".keras")]

model_list = get_model_list()
selected_model = st.sidebar.selectbox("Select Model for Prediction", model_list)

# ---------- Upload Image ----------
st.title("🐔 Chicken Disease Classifier")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    temp_image_path = os.path.join(TEMP_DIR, uploaded_file.name)
    with open(temp_image_path, "wb") as f:
        f.write(uploaded_file.read())

    image = Image.open(temp_image_path)  # ✅ Correctly open image
    st.image(image, caption="Uploaded Image", use_container_width=True) 

    if st.button("Predict"):
        try:
            model_path = os.path.join(ARTIFACT_DIR, selected_model)
            predictor = PredictionPipeline(filename=temp_image_path, model_path=model_path)
            result = predictor.predict()
            st.success(f"✅ Prediction: {result[0]['image']}")
        except Exception as e:
            st.error(f"❌ Error during prediction: {str(e)}")

        os.remove(temp_image_path)
