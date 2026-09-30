# Project Statement

## Electricity Bill Calculator

### Student Details

| **Field** | **Details** |
|---|---|
| **Name** | Saba Naz |
| **Registration Number** | 26MIM10041 |
| **College Mail ID** | saba.26mim10041@vitbhopal.ac.in |
| **Course** | Python Essential |
| **Program** | B. Tech CSE (AIML) |
| **Institution** | VIT Bhopal University |
| **Academic Year** | 2026–27 |

---

## Project Statement

The **Electricity Bill Calculator** is a simple Python-based application developed to calculate an electricity bill based on the number of units consumed by a customer.

The project was created as a basic academic application to understand how Python classes and modules can be used together to solve a small real-world problem.

The user enters the following information:

- Customer Name
- Customer ID
- Units Consumed

The program then calculates the **energy charge** using predefined unit slabs, adds the applicable **fixed charge**, and displays the final electricity bill.

---

## Classes Used

The project uses five main classes:

1. `Customer`
2. `Units`
3. `EnergyCharge`
4. `FixedCharge`
5. `Bill`

The `main.py` file connects these classes and controls the overall flow of the program.

The project deliberately avoids unnecessary complexity such as databases, payment gateways, login systems, and graphical interfaces. The main focus is on **Python fundamentals, modular programming, classes, objects, and a clear calculation process**.

---

## Objectives

The main objectives of this project are:

1. To create a simple electricity bill calculation program using Python.
2. To practice the concepts of classes and objects.
3. To understand how separate Python modules can work together.
4. To apply conditional statements to slab-based electricity calculations.
5. To produce a clear and readable electricity bill as output.
6. To understand how a small real-world problem can be divided into independent modules.

---

## Scope

The current project is designed for **academic and demonstration purposes**.

It can calculate an electricity bill for one customer at a time using the predefined sample electricity rates.

The project can be expanded in the future by adding features such as:

- Input validation
- File-based data storage
- Multiple customer records
- Graphical user interface
- Configurable tariff rates
- Bill history
- Automated report generation

---

## Expected Outcome

After entering the customer information and units consumed, the program should correctly calculate and display the following details:

| **Output** | **Description** |
|---|---|
| Customer Name | Name entered by the user |
| Customer ID | Unique customer identification |
| Units Consumed | Number of electricity units used |
| Energy Charge | Charge calculated according to unit slabs |
| Fixed Charge | Fixed amount added to the bill |
| **Total Bill** | Final electricity bill amount |

---

## Technology Used

| **Technology / Component** | **Details** |
|---|---|
| **Programming Language** | Python |
| **Application Type** | Console-based application |
| **Programming Concepts** | Classes, Objects, Modules, Conditional Statements |
| **External Database** | Not used |
| **External Libraries** | Not required |

---

## Project Structure

```text
Electricity_Bill_Calculator/
│
├── main.py
├── bill.py
├── customer.py
├── energy_charge.py
├── fixed_charge.py
├── units.py
├── README.md
├── statement.md
├── successful_output.png
└── validation_test.png
