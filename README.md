# Churn Prediction Web Application

This repository contains a simple web application for churn prediction based on customer data. The application is built using Flask and a Decision Tree Classifier model trained on customer data. Users can input customer details, and the application predicts whether the customer is likely to leave or stay with the bank.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/churn-prediction-app.git
   cd churn-prediction-app
   ```

```bash 
pip install flask scikit-learn pandas

python app.py

Open your web browser and go to http://127.0.0.1:5000/ to use the churn prediction application.
```

## How to Use:

- Enter customer details in the provided input boxes.
- Click the "Predict Churn" button.
- The predicted churn status will be displayed.

## Code Structure
- app.py: Flask application file containing the code for initializing the Flask app, loading the churn prediction model, and defining the route for churn prediction.

- templates/home.html: HTML template for the home page of the web application.

- churn.model: Pickle file containing the trained Decision Tree Classifier churn prediction model.

## Acknowledgments
This application uses the Flask framework for web development. Learn more about Flask here.

The churn prediction model is based on a Decision Tree Classifier algorithm trained on customer data.

Feel free to explore, modify, and adapt the code for your specific use case. If you have any questions or suggestions, please open an issue or reach out to kvedant451@gmail.com.
