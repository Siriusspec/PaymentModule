Payment Module
A FastAPI-based payment processing module using Stripe and PostgreSQL. Part of a food delivery system — handles all payment operations and integrates with the Order Module and other services.

Live URL
https://paymentmodule-6ttf.onrender.com
Swagger UI (API Docs): https://paymentmodule-6ttf.onrender.com/docs
ReDoc: https://paymentmodule-6ttf.onrender.com/redoc

Project Structure
payment-module/
├── database/
│   ├── __init__.py
│   ├── db.py           # PostgreSQL connection & setup
│   └── models.py       # SQLAlchemy models
├── routes/
│   ├── __init__.py
│   └── payments.py     # Payment endpoints
├── security/           # Security utilities
├── tests/
│   └── tests.txt       # Test cases & examples
├── main.py             # App entry point
├── requirements.txt    # Dependencies
└── .gitignore

Tech Stack
FastAPIWeb frameworkStripePayment processingSQLAlchemyORMPostgreSQLDatabaseUvicornASGI serverRenderDeployment

Local Setup
1. Clone the repo
bashgit clone https://github.com/Siriusspec/PaymentModule.git

cd payment-module
2. Create virtual environment
bashpython -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
3. Install dependencies
bashpip install -r requirements.txt
4. Set up environment variables
Create a .env file in the root directory:
envDATABASE_URL=postgresql://your_db_url
STRIPE_SECRET_KEY=sk_test_your_key
SECRET_KEY=your_secret_key
5. Run the app
bashuvicorn main:app --reload
App runs at http://localhost:8000

Environment Variables
VariableDescriptionDATABASE_URLPostgreSQL connection URLSTRIPE_SECRET_KEYStripe restricted secret keySECRET_KEYApp secret key

Never commit .env to GitHub — it's already in .gitignore


Connecting Other Services
This module is part of a food delivery system. Other modules (Order, Confirmation, Rider etc.) can connect to this service via HTTP.
Base URL:
https://paymentmodule-6ttf.onrender.com
All payment routes are prefixed with /payments:
https://paymentmodule-6ttf.onrender.com/payments
CORS is enabled — any service can call this API out of the box. No extra configuration needed.

In production, replace allow_origins=["*"] in main.py with your specific service URLs for better security.


System Architecture
Order Module          -->
                            Payment Module  -->  Confirmation Module
Rider Module          -->

Deployment (Render)

Push code to GitHub
Create a PostgreSQL database on Render
Create a Web Service on Render, connect the GitHub repo
Add environment variables in Render dashboard
Set build & start commands:

Build:  pip install -r requirements.txt
Start:  uvicorn main:app --host 0.0.0.0 --port 10000

Notes

DB tables are auto-created on startup — no manual migration needed
Free tier on Render sleeps after 15 mins of inactivity — first request may be slow
Free PostgreSQL on Render expires after 90 days
