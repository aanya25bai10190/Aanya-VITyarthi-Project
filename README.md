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
