
#  Profile Catalog 

A simple **Streamlit-based Profile Catalog Web Application** that collects user information and stores it in a CSV file.  
User authentication is handled through a JSON file that stores username–password pairs.

---

##  Features
-  User login system using JSON-based authentication  
-  Profile information form  
-  CSV storage for user data  
-  Lightweight, portable, and easy to run  

---

## 🛠️ Installation & Setup

### **1. Create and activate a virtual environment**
```bash
python -m venv venv
```

**Activate it:**

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

---

### **2. Install dependencies**
```bash
pip install streamlit pandas
```

---

### **3. Run the Streamlit application**
```bash
streamlit run streamlit1.py
```

---

##  Project Structure
```
project/
│── Correct_info_page.py      
│── streamlit1.py             
│── ID_PASS.json              
│── Login_info.csv            
│── __pycache__/              
```

---

## 🔧 How It Works

### **1. User Login**
Credentials are stored in `ID_PASS.json` like:
```json
{
  "user1": "password1"
}
```

### **2. User Profile Submission**
Details submitted via Streamlit UI are saved into `Login_info.csv`.

### **3. Info Display**
`Correct_info_page.py` displays or verifies stored data.

---

## Developer
Abhijeet
