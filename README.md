# 🧠 Predict Tomorrow’s Pay Today — Employee Salary Prediction

This machine learning project was developed as part of the **AICTE–IBM SkillsBuild AI/ML Internship**. The goal is to predict whether an individual earns more than 50K annually using various demographic and employment-related features. The project utilizes supervised learning techniques with a focus on accuracy and interpretability.

---

## 📌 Objective

To build a predictive model that classifies individuals based on their income level (`<=50K` or `>50K`) using the UCI Adult dataset, enabling insights into key factors influencing employee salaries.

---

## 🔍 Dataset

- **Source:** [UCI Adult Income Dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- **Features Include:**
  - Age, Workclass, Education, Occupation
  - Marital Status, Race, Sex
  - Hours-per-week, Capital Gain/Loss, etc.

---

## 🛠️ Technologies Used

- **Languages:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost
- **Platform:** Jupyter Notebook / VS Code

---

## 📊 Workflow

1. **Data Preprocessing:**
   - Removed missing or inconsistent data
   - Label encoding and feature scaling

2. **Exploratory Data Analysis:**
   - Visualized relationships using bar plots, histograms, and heatmaps

3. **Model Building:**
   - Tested multiple classifiers: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting
   - **Gradient Boosting** gave the highest accuracy

4. **Model Evaluation:**
   - Used Accuracy, Precision, Recall, and F1 Score
   - Gradient Boosting performed best with balanced performance on both salary classes

---

## ✅ Key Findings

- Features like **education level**, **hours-per-week**, and **occupation** significantly impact salary.
- **Gradient Boosting** outperformed other models in accuracy and generalization.
- The model effectively classified salary brackets and revealed strong feature-salary relationships.

---

## 🌱 Future Scope

- **Model Deployment:** Create a web interface using Streamlit or Flask
- **Real-world Expansion:** Include features like experience, company size, and location
- **Tuning & Optimization:** Apply advanced hyperparameter tuning techniques
- **Automation:** Integrate into HR or finance tools for salary benchmarking

---

## 📚 References

- UCI Machine Learning Repository - Adult Dataset  
- Scikit-learn Documentation: https://scikit-learn.org/  
- IBM SkillsBuild AI/ML Internship Materials  
- Kaggle Discussions and Tutorials

---

## 🙌 Acknowledgements

This project was developed as part of the **AICTE–IBM SkillsBuild Internship**, where I gained practical experience in real-world machine learning workflows, model selection, and business-oriented problem solving.

---

> **Made with 💡 and 🔍 by Mamatha Sara**
