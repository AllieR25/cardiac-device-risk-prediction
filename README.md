# ML-Based Risk Prediction for Implanted Cardiac Devices

This project uses machine learning to classify the severity of adverse events associated with implanted cardiac devices such as pacemakers, based on public reports from the FDA MAUDE database.

## 🎯 Objective

Develop a supervised learning model that can predict whether an adverse event report will be classified as *serious* or *non-serious*, using event description text and related metadata.

## 📂 Project Structure

- `data/`: Contains raw and processed MAUDE data
- `notebooks/`: EDA, modeling, and evaluation notebooks
- `src/`: Python scripts for data processing and ML pipeline
- `outputs/`: Charts, metrics, and saved models

## 📊 Data Source

All data used in this project is publicly available via the [FDA MAUDE database](https://www.fda.gov/medical-devices/maude-adverse-event-reporting-system).

## ⚠️ Disclaimer

This project is for educational purposes only and is not affiliated with or endorsed by any medical device manufacturer. No proprietary or patient-identifiable data is used.

---

## 🛠️ Tech Stack

- Python, Pandas, scikit-learn
- NLP: NLTK, spaCy or scikit-learn’s TfidfVectorizer
- Visualization: Matplotlib, Seaborn

## 📌 Future Features

- Streamlit interface for real-time risk predictions
- Model interpretability (SHAP or LIME)
- Expansion to other device classes
