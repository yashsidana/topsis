# TOPSIS Package

This is a Python package for implementing TOPSIS.

## Installation

```bash
pip install Topsis-Yash-102303973
# TOPSIS Decision Making Tool (Assignment Project)
project link
https://pypi.org/project/Topsis-Yash-102303973/

This project is an implementation of the **TOPSIS** method  
(**Technique for Order of Preference by Similarity to Ideal Solution**) as part of the academic assignment.

The project is completed in three parts:

- ✅ Part I: CLI-based TOPSIS implementation  
- ✅ Part II: Python package published on PyPI  
- ✅ Part III: Web application with Email result service  

---

## 📌 What is TOPSIS?

TOPSIS is a Multi-Criteria Decision Making (MCDM) technique used to rank alternatives based on their closeness to the ideal solution.

It selects the best alternative by calculating:

- Distance from the Ideal Best  
- Distance from the Ideal Worst  
- TOPSIS Score  
- Final Ranking

---

---

# ✅ PART I: Command Line TOPSIS Tool

## Features

- Accepts input CSV file  
- Accepts weights and impacts  
- Produces ranked output file  
- Handles all required validations  

---

## Input File Format

The input file must be a CSV with:

- First column: Alternative names  
- Remaining columns: Numeric criteria values  

Example:

```csv
Fund Name,P1,P2,P3,P4
M1,0.67,0.45,6.5,42.6
M2,0.60,0.36,3.3,53.3
M3,0.82,0.67,3.8,61.7



