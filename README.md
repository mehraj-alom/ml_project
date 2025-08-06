# ml_project

## 🐔 Chicken Classification ML Project
**A complete end-to-end Machine Learning project for classifying Chicken disease , built with a modular pipeline, experiment tracking, and deployment ready with Docker & Streamlit.**

## 📂 Project Structure
├── artifacts/               # Saved artifacts from training
├── config/                  # Configuration files
├── logs/                    # Training and evaluation logs
├── research/                # Jupyter notebooks for initial exploration & prototyping
│   ├── 01_data_ingestion.ipynb
│   ├── 02_prepare_base_model.ipynb
│   ├── ...
├── src/                     # Source code
│   ├── Classifier/          # Main Classifier module
│   │   ├── components/      # Individual components of the pipeline
│   │   ├── config/          # Config management
│   │   ├── constants/       # Project-wide constants
│   │   ├── entity/          # Data classes / schema definitions
│   │   ├── pipeline/        # Pipeline orchestration
│   │   ├── utils/           # Utility functions
│   │   └── __init__.py
├── templates/               # HTML / Streamlit templates if any
├── temp/                    # Temporary files (ignored in VCS)
├── app.py                   # Streamlit app entry point
├── main.py                  # Script to run training pipeline
├── Dockerfile               # Docker configuration
├── dvc.yaml                 # DVC pipeline definition
├── dvc.lock                 # DVC lock file
├── params.yaml              # Hyperparameters & config
├── requirements.txt         # Python dependencies
├── setup.py                 # Packaging and installation config
├── scores.json              # Model evaluation scores
├── README.md                # Project documentation
└── .gitignore               # Git ignore file


## ⚙️ Tech Stack & Tools
- **Programming Language: Python 3.11**

- **Libraries: TensorFlow / PyTorch (depending on requirements.txt), scikit-learn, pandas, numpy, matplotlib, etc.**

- **Experiment Tracking: DVC**

- **Deployment: Docker, Streamlit**

- **Version Control: Git, GitHub**

- **CI/CD Ready**

## 🚀 How to Run
**1️⃣ Clone the Repository**
 - git clone https://github.com/mehraj-alom/ml_project.git
 -   cd ml_project
   
**2️⃣ Setup Virtual Environment**
- python3 -m venv venv
- source venv/bin/activate  # Linux / Mac
- venv\Scripts\activate     # Windows
  
**3️⃣ Install Dependencies**
- pip install -r requirements.txt
  
**4️⃣ Run Training Pipeline**
- python main.py
  
**5️⃣ Run the Streamlit App**
- streamlit run app.py

    **OR**

  **🐳 Run with Docker**
  -  Pull the image
      - docker pull mehrajalom/chicken:latest

  - Run the image
      - docker run -p 8501:8501 mehrajalom/chicken:latest
  - Open Browser and paste it 
      - http://localhost:8501



## 📝 Project Highlights

**✅ Modular Code Structure**
**✅ DVC-based Pipeline & Experiment Tracking**
**✅ Configurable via YAML**
**✅ Reproducible Experiments**
**✅ Containerized with Docker**
**✅ Simple Web App with Streamlit**
**✅ Industry-ready Practices**

## 💻 Contributing

Feel free to open issues or submit pull requests!
Contributions are welcome.


## ✨ Author
- Mehraj Alam

- GitHub: https://github.com/mehrajalom



  





ECR repo
677012401372.dkr.ecr.eu-north-1.amazonaws.com/chicken

