# SauceDemo Automation Framework

## Project Overview
Automation testing framework for the SauceDemo web application using **Python**, **Playwright**, **Pytest**, and **Page Object Model (POM)**.

**Application:** https://www.saucedemo.com/

## Features
- Login Validation
- Logout Functionality
- Add Products to Cart
- Cart Validation
- Checkout Process
- Product Sorting
- Random Product Selection
- Reset App State
- HTML Reports
- Screenshot Support

## Tech Stack
- Python
- Playwright
- Pytest
- Pytest-HTML

## Run All Tests

```bash
pytest
```

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

## Project Structure

```
pages/
tests/
utils/
reports/
screenshots/
conftest.py
pytest.ini
requirements.txt
```
