# Payment Module

A FastAPI-based payment processing module using Stripe and PostgreSQL. Part of a food delivery system that handles all payment operations and integrates with the Order Module and other services.

---

## Live URL

- API: https://paymentmodule-6ttf.onrender.com
- Swagger Docs: https://paymentmodule-6ttf.onrender.com/docs
- ReDoc: https://paymentmodule-6ttf.onrender.com/redoc

---

## Project Structure
payment-module/
├── database/
│   ├── init.py
│   ├── db.py
│   └── models.py
├── routes/
│   ├── init.py
│   └── payments.py
├── security/
├── tests/
│   └── tests.txt
├── main.py
├── requirements.txt
└── .gitignore

---

## Tech Stack

- FastAPI
- Stripe
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Render

---

## Local Setup

1. Clone the repo git clone https://github.com/Siriusspec/PaymentModule.git
cd payment-module
2. Create virtual environment python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
