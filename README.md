# 🩸 CycleSync: In-Memory Period Tracking and Prediction System

## 🌟 Overview

**CycleSync** is a modular, command-line application built in Python designed to track menstrual periods, log symptoms, and calculate the next predicted period and ovulation dates. It demonstrates a clear separation of concerns using distinct service modules for authentication, data logging, and prediction, utilizing Python lists for simple, in-memory data storage.

## ✨ Features

* **🔐 User Management:** Register and login user accounts.
* **🗓️ Cycle Logging:** Log the start and end dates of periods (`YYYY-MM-DD` format).
* **📋 Symptom Tracking:** Log custom symptoms with intensity ratings (1 to 5).
* **📊 Prediction Engine:** Uses the **Mean Cycle Length (MCL)** method to calculate future dates.
* **🎯 Ovulation Estimation:** Predicts ovulation 14 days prior to the predicted next period.

## 🛠️ Technologies / Tools Used

* **Language:** Python 3.x
* **Core Libraries:** Python Standard Library (`datetime`)
* **Architecture:** Service-Oriented (Auth, Cycle, Prediction)
* **Data Storage:** In-Memory Python Lists (simulated database)

## 🚀 Steps to Install & Run the Project

This project requires only a standard Python 3 installation.

### 1. Clone the Repository

```bash
git clone https://github.com/aanya25bai10190/Aanya-VITyarthi-Project
cd CycleSync
```
### 2. Run the Application

Execute the main runner file directly from your command line:
```bash
python app.py
```
The workflow will prompt for registration/login, automatically log sample data, and display the final prediction.

## 🧪 Instructions for Validation and Testing

The application's logic is validated using fixed input data in app.py to ensure predictable outcomes.

A. Prediction Logic Validation

The application uses cycles of 31 and 30 days.
* Expected MCL Calculation: (31 + 30) / 2 = 30.5. Rounded, the MCL is 31 days.
* Expected Next Period (Based on 2025-10-20 last start): 2025-10-20 + 31 days= 2025-11-20}.
* Expected Ovulation: 2025-11-20- 14 days = 2025-11-06.

B. Error Handling Validation (NFRs)

The code contains input validation checks (NFR1). You can manually test this by modifying the logging calls in app_runner.py:

* Date Format Error: Change a date string (e.g., "2025-10-20") to an invalid format (e.g., "10/20/2025"). The log_period call should return the error message: "Invalid date format. Use YYYY-MM-DD."
* Intensity Error: Change the intensity for a symptom from 3 to 6. The log_symptom call should return the error: "Intensity must be between 1 and 5."
