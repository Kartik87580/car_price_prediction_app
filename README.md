

# 🚗 Car Price Prediction App

A Machine Learning web application that predicts the **selling price of a used car** based on various features such as car age, fuel type, transmission, etc. The app is built using **Streamlit** for the interface and **Random Forest Regressor** for the prediction model.

---

## 📂 Project Structure

```
car_price_prediction/
│
├── app.py               # Streamlit app code
├── car data.csv         # Dataset used for training
├── car_price_pred.ipynb # Jupyter notebook for exploration & model training
└── README.md            # Project documentation
```

---

## 🧠 Features Used

* **Present\_Price**: Current ex-showroom price (in lakhs)
* **Driven\_kms**: Total distance driven (in kilometers)
* **Fuel\_Type**: Petrol, Diesel, or CNG
* **Seller\_Type**: Dealer or Individual
* **Transmission**: Manual or Automatic
* **Owner**: Number of previous owners
* **Car\_Age**: Age of the car (calculated from Year)

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – for interactive UI
* **Pandas & NumPy** – for data manipulation
* **Scikit-learn** – for ML model and preprocessing
* **Random Forest Regressor** – for predicting car prices

---

## 🚀 How to Run the App

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/car_price_prediction.git
   cd car_price_prediction
   ```

2. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is missing, install manually:

   ```bash
   pip install streamlit pandas scikit-learn
   ```

3. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

---

## 📊 Model Overview

* **Model Used**: `RandomForestRegressor`
* **Target Variable**: `Selling_Price`
* **Encoding**: Categorical features like Fuel Type, Transmission, etc. were label encoded.
* **Performance**: Model gives reasonably accurate predictions for practical applications.


## 📁 Dataset Source

* The dataset is included in this repository: [`car data.csv`](./car%20data.csv)

---

## 🤝 Contributing

Contributions are welcome! If you find bugs or want to enhance the app, feel free to fork the repo and create a pull request.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

