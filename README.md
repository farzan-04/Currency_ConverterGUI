# Currency Converter Web App 🌍💰
✅ **Live Demo:** [Streamlit App](https://currencyconvertergui.streamlit.app)  
✅ **Backend API:** [Powered by Flask API (Deployed on Render)](https://flask-currency-api-2.onrender.com)  

## 🔧 How It Works
- The frontend is built using **Streamlit**.
- The backend runs on **Flask API**, which provides real-time exchange rates.
- The API fetches rates from ExchangeRate-API and returns converted amounts.
- **Source Code for API:** Available upon request.

🛠️ Tech Stack
- **Streamlit** (Frontend UI)
- **Flask API** (Backend Logic)
- **Requests** (Calls API for real-time exchange rates)
- **Streamlit Cloud** (Hosting)


**Example API Request from GUI to API**
https://your-api.onrender.com/convert?amount=100&from=USD&to=INR

📤 **Example API Response:**
```json
{
    "from": "USD",
    "to": "INR",
    "amount": 100,
    "converted_amount": 8300.00
}
