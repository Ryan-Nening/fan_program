# Fan Program

**An Object-Oriented Smart Dashboard using Encapsulation**

## Project Overview
This project simulates an IoT (Internet of Things) smart-home dashboard to monitor ceiling fans. It was strictly developed to demonstrate **Data Hiding** and **Encapsulation** in Object-Oriented Programming (OOP). 

Instead of printing static text to a terminal, this program utilizes a custom Tkinter UI to visually display the live properties of two encapsulated `Fan` objects.

## Core OOP Features
* **Strict Data Hiding:** All internal fan properties (`__speed`, `__radius`, `__color`, `__on`) are locked as private variables to prevent unauthorized external modification.
* **Secure Gateways:** Utilizes authorized `Getter` and `Setter` methods to safely read and modify the object's state.
* **Separation of Concerns:** The mathematical blueprint (`Fan`) is completely isolated from the graphical interface (`FanDashboard`), showcasing professional software architecture.

## How to Run the Program
1. Open the `fan_program` folder in your terminal or IDE.
2. Run the main execution driver:
   ```bash
   python main_fan_file.py
