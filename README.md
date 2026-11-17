# Bullion & Stock Market Tracker

## 1. Project Overview

The **Bullion & Stock Market Tracker** is an Android application designed to provide users with a unified platform to monitor precious metal prices and Indian stock market movements.

The application aims to track gold and silver rates, monitor NSE and BSE stocks, manage investment portfolios, maintain watchlists, and receive price alerts.

The project combines real-time or provider-delayed financial market data with investment tracking and portfolio analytics.

## 2. Project Objectives

- Track live or delayed gold and silver market prices.
- Monitor Indian stock market data from NSE and BSE.
- Display NIFTY 50 and SENSEX indices.
- Calculate gold prices based on different purities.
- Track stock and precious metal investments.
- Calculate portfolio value, profit and loss.
- Create personalized watchlists.
- Set price alerts for selected assets.
- Provide a simple and user-friendly Android interface.

## 3. Key Features

### Gold and Silver Tracking
- Gold price tracking (24K, 22K and 18K).
- Silver price tracking.
- Price display per gram and kilogram.
- INR currency conversion.
- Historical price tracking.

### Indian Stock Market Tracking
- NSE and BSE stock monitoring.
- Individual stock price details.
- NIFTY 50 and SENSEX tracking.
- Opening and closing prices.
- Daily high and low.
- Price changes and percentage changes.

### Portfolio Management
- Add stock investments.
- Add gold and silver holdings.
- Calculate total invested amount.
- Calculate current portfolio value.
- Calculate unrealized profit and loss.
- Monitor individual investment performance.

### Watchlists and Price Alerts
- Add and remove favourite assets.
- Monitor selected stocks and metals.
- Set target prices.
- Generate alerts when price conditions are met.

## 4. Technology Stack

### Backend
- Python
- FastAPI
- Uvicorn
- PostgreSQL (planned)
- SQLite (initial development)
- REST APIs
- WebSockets

### Frontend
- Flutter
- Dart

### Development Tools
- Git
- GitHub
- Visual Studio Code
- Postman
- Pytest

## 5. Project Architecture

The application follows a client-server architecture.

```text
Bullion & Stock Market Tracker
             |
       Flutter App
             |
        REST APIs
             |
       FastAPI Backend
             |
     -------------------
     |        |        |
   Metals   Stocks   Portfolio
   Service  Service  Service
     |        |        |
     -------------------
             |
         Database
             |
       SQLite / PostgreSQL
             |
      External Market APIs
```

## 6. Team Responsibilities

### Member 1 – Backend Lead
**Primary responsibility:** Backend development and API integration.

Tasks:
- Develop the FastAPI backend.
- Integrate gold and silver market data.
- Integrate NSE and BSE stock market data.
- Design database models.
- Develop portfolio calculations.
- Implement watchlists and price alerts.
- Write backend tests.
- Participate in Flutter integration.

### Member 2 – Frontend Development
**Primary responsibility:** Flutter application development.

Tasks:
- Set up the Flutter project.
- Design the application interface.
- Develop dashboard screens.
- Build gold and silver tracking screens.
- Develop stock market screens.
- Create portfolio and watchlist interfaces.
- Integrate backend APIs.
- Implement notification interfaces.
- Test the Android application.

Both members will participate in learning and integrating frontend and backend technologies.

## 7. Repository Structure

```text
Market-tracker/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   └── database/
│   │
│   ├── tests/
│   ├── requirements.txt
│   └── .venv/
│
├── frontend/
│   └── Flutter application (planned)
│
├── README.md
└── .gitignore
```

## 8. Development Roadmap

| Week | Development Focus |
|---|---|
| Week 1 | Backend and Flutter foundation |
| Week 2 | Gold and silver price integration |
| Week 3 | NSE and BSE stock integration |
| Week 4 | Database and portfolio management |
| Week 5 | Watchlists, alerts and analytics |
| Week 6 | Testing, integration and deployment |

## 9. Current Development Status

**Project Phase:** Initial Development

## 10. Future Enhancements

- Advanced stock market analytics.
- Technical indicators.
- Interactive financial charts.
- Personalized investment dashboards.
- Push notifications.
- Historical market comparisons.
- Improved portfolio performance analysis.

## 11. Disclaimer

This application is developed for educational and informational purposes.

Market prices may be delayed depending on the selected data provider. Gold and silver calculations are indicative and may not include applicable taxes, GST, making charges or local dealer premiums.

This application does not provide financial or investment advice.

## 12. Contributors

- **Member 1:** Backend Lead
- **Member 2:** Frontend Developer

---

**Project Name:** Bullion & Stock Market Tracker

**Platform:** Android

**Backend:** Python + FastAPI

**Frontend:** Flutter + Dart

**Target Markets:** Indian Bullion Market, NSE and BSE

**Repository:** Market-tracker
