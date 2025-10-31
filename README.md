# Mobile-App-Automation-Testing-Exercises-Python

## Project Overview
This repository contains a collection of **mobile automation testing exercises** developed using **Python**.  
The goal of this project is to **practice and master automation testing for Android and iOS mobile applications** using tools like **Appium** and **Selenium** (for hybrid apps).

The exercises focus on building the skills needed to design, script, and execute test automation for mobile applications efficiently.

---

## Tech Stack
| Component | Description |
|------------|--------------|
| **Language** | Python |
| **Automation Framework** | Appium |
| **Supported Platforms** | Android & iOS |
| **Testing Framework** | unittest / pytest |
| **Automation Type** | Mobile (Native, Hybrid, WebView) |
| **Design Pattern** | Page Object Model (POM) |
| **IDE Used** | PyCharm / VS Code |
| **Build Tool** | Manual / Non-Maven |

---

## Folder Structure

```yaml
Mobile-App-Automation-Testing-Exercises-Python/
│
├── tests/                   # Test cases for different mobile modules
│ ├── test_login.py
│ ├── test_registration.py
│ └── test_settings.py
│
├── pages/                   # Page Object Model (POM) classes
│ ├── login_page.py
│ ├── registration_page.py
│ └── settings_page.py
│
├── utils/                   # Utility classes (drivers, waits, config)
│ ├── driver_setup.py
│ ├── config_reader.py
│ └── wait_utils.py
│
├── data/                    # Test data files
│ ├── credentials.json
│ └── testdata.xlsx
│
├── reports/                 # Execution reports (pytest-html, allure)
│
├── screenshots/             # Captured screenshots on test failure
│
├── requirements.txt         # Python dependencies
│
└── README.md                # Project documentation
```

---

## Setup Instructions

### **1️. Prerequisites**
- Install **Python 3.10+**
- Install **Appium Server** (Desktop or via npm)
- Install **Android SDK / Xcode** for device emulation
- Set environment variables for: `ANDROID_HOME`, `JAVA_HOME`

### **2️. Install Dependencies**
Run:

```bash
  pip install -r requirements.txt
```

### **3. Example `requirements.txt`**

```css
  appium-python-client
  pytest
  pytest-html
  selenium
  openpyxl
```

---

## Run Test Cases

**Using Pytest:**

```bash
  pytest -v -s tests/test_login.py --html=reports/report.html
```

**Using unittest:**

```bash
  python -m unittest discover -s tests
```

---

## Example Test Flow

1. Launch Appium server

2. Connect your Android/iOS device or emulator

3. Update desired capabilities in `driver_setup.py`

4. Run the tests via `pytest` or `unittest`

5. View HTML report and screenshots for failed tests

---

## Learning Objectives

- Automate **native**, **hybrid**, and **webview** mobile applications

- Implement **Page Object Model (POM)** for mobile testing

- Use **Appium desired capabilities** effectively

- Handle mobile gestures (tap, swipe, scroll)

- Capture screenshots and generate reports

- Build reusable utility classes for mobile automation

---

## Sample Modules Automated

- Login Flow

- Registration Screen

- Profile Update

- Settings Page

- Logout Functionality

---

## Author

**Vimalkumar Murugesan**

_Manual & Automation Tester_

- Specialized in Web, API & Mobile Testing
- [LinkedIn](https://www.linkedin.com/in/vimalkumar-m/) | [GitHub](https://github.com/itsVimalkumaR)

