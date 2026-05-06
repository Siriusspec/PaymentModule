# Payment Module

A FastAPI-based payment processing module using Stripe and PostgreSQL. Part of a food delivery system that handles all payment operations and integrates with the Order Module and other services.

---

## Live URL

- API: https://paymentmodule-6ttf.onrender.com
- Swagger Docs: https://paymentmodule-6ttf.onrender.com/docs
- ReDoc: https://paymentmodule-6ttf.onrender.com/redoc

---

## Project Structure

```
payment-module/
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── models.py
├── routes/
│   ├── __init__.py
│   └── payments.py
├── security/
├── tests/
│   └── tests.txt
├── main.py
├── requirements.txt
└── .gitignore
```

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

**1. Clone the repo**

    git clone https://github.com/Siriusspec/PaymentModule.git
    cd payment-module

**2. Create virtual environment**

    python -m venv venv
    venv\Scripts\activate        # Windows
    source venv/bin/activate     # Mac/Linux

**3. Install dependencies**

    pip install -r requirements.txt

**4. Create a `.env` file in the root directory**

    DATABASE_URL=postgresql://your_db_url
    STRIPE_SECRET_KEY=sk_test_your_key
    SECRET_KEY=your_secret_key

**5. Run the app**

    uvicorn main:app --reload

App runs at http://localhost:8000

---

## Environment Variables

- `DATABASE_URL` — PostgreSQL connection URL
- `STRIPE_SECRET_KEY` — Stripe restricted secret key
- `SECRET_KEY` — App secret key

Never commit `.env` to GitHub — it is already in `.gitignore`

---

## Connecting Other Services

This module is part of a food delivery system. Other modules (Order, Confirmation, Rider etc.) can connect via HTTP.

- Base URL: https://paymentmodule-6ttf.onrender.com
- All payment routes: https://paymentmodule-6ttf.onrender.com/payments

CORS is enabled — any service can call this API out of the box. In production, replace `allow_origins=["*"]` in `main.py` with specific service URLs.

---

## Deployment on Render

1. Push code to GitHub
2. Create a PostgreSQL database on Render
3. Create a Web Service on Render and connect the GitHub repo
4. Add environment variables in Render dashboard
5. Build command: `pip install -r requirements.txt`
6. Start command: `uvicorn main:app --host 0.0.0.0 --port 10000`

---

## Notes

- DB tables are auto-created on startup, no manual migration needed
- Free tier on Render sleeps after 15 mins of inactivity, first request may be slow
- Free PostgreSQL on Render expires after 90 days
