# 🎯 CycleSync: Project Statement

## 1. Problem Statement

Women often need a reliable, personal system to track irregular or regular menstrual cycles, log associated symptoms, and calculate predictive dates for their next period and ovulation. Existing commercial solutions can be overly complex or rely on external cloud infrastructure. The problem addressed by CycleSync is to build a **simple, self-contained, and easily verifiable application** that provides core cycle tracking and robust, data-driven predictions using foundational Python concepts and an in-memory storage model.

## 2. Scope of the Project

The scope of the CycleSync project is to implement a command-line utility with the following boundaries:

* **In-Memory Data:** Data storage will be managed using basic Python lists, simulating a simple database. Data will not persist after the application terminates.
* **Core Services Only:** Focus is strictly on Authentication, Cycle/Symptom Logging, and Predictive Analytics.
* **Prediction Method:** Prediction is limited to the **Mean Cycle Length (MCL)** method.

## 3. Target Users

* **Individuals:** Users who require a straightforward, private tool to track their menstrual health.
* **Students/Researchers:** Users who need a clear, understandable, and modular implementation of a common cycle prediction algorithm for study or reference.

## 4. High-Level Features

1.  **User Authentication:** Secure registration and login.
2.  **Period Management:** Logging of cycle start and end dates.
3.  **Symptom Tracking:** Detailed logging of symptoms with intensity scores (1-5).
4.  **Cycle Analytics:** Calculation of the Mean Cycle Length (MCL).
5.  **Future Prediction:** Predicting the next period start date and estimated ovulation date.
