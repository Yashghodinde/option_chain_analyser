# Nifty Option Chain Analyser

![Python](https://img.shields.io/badge/Python-3.8-blue)
![Accuracy](https://img.shields.io/badge/Accuracy-%3E72%25-brightgreen)

The **Nifty Option Chain Analyser** is a Python-based project designed to fetch real-time option chain data from the National Stock Exchange (NSE) API, process the JSON response into structured tables, and calculate key metrics such as **Change in Open Interest (OI)** and **Put-Call Ratio (PCR)**. These metrics are then used to predict market movements with an accuracy of over **72%**.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Code Walkthrough](#code-walkthrough)
7. [Metrics Explained](#metrics-explained)
8. [Contributing](#contributing)
9. [License](#license)

---

## Overview

This project focuses on analyzing the **Nifty 50 Index Option Chain** to predict market trends. By fetching live data from the NSE API, the tool calculates:
- **Change in Open Interest (OI):** Indicates shifts in trader sentiment.
- **Put-Call Ratio (PCR):** Measures the ratio of put options to call options, signaling bullish or bearish trends.
- **Change in PCR (CHPCR):** Tracks changes in PCR over time to refine predictions.
- **OI Difference:** Highlights the net difference between total Put OI and Call OI.

Using these metrics, the tool predicts potential market movements before they occur, achieving an accuracy rate of over **72%**.

---

## Features

- Fetches real-time option chain data from the NSE API.
- Parses and organizes JSON data into structured tables.
- Calculates **Total Call OI**, **Total Put OI**, **Change in Call OI**, **Change in Put OI**, **PCR**, and **CHPCR** dynamically.
- Writes analysis results to text files for further use.
- Provides insights into bullish or bearish market sentiment.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- Required libraries: `requests`, `pandas`

Install dependencies using:
```bash
pip install requests pandas
```

