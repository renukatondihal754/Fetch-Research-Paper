# Fetch-Research-Paper

## 📄 Overview

This Python project allows you to fetch research papers from **PubMed** based on a specific query. It extracts research papers with at least one author affiliated with **pharmaceutical or biotech companies** and generates a CSV file containing the extracted data.

The script uses the **PubMed API (Entrez)** to search for papers and captures relevant information like **title, publication date, company affiliations, and corresponding author email.**

---

## ✅ Features
- **Fetch research papers** using the PubMed API.
- Identify non-academic authors affiliated with pharmaceutical/biotech companies.
- Extract corresponding author email addresses.
- Save the extracted data into a CSV file.
- Provide command-line options for flexibility.
- Merge multiple CSV files into one consolidated CSV file.



---


## 📥 Installation
### **Step 1: Clone the repository**
```shell
git clone https://github.com/renukatondihal754/Fetch-Research-Paper.git
cd Fetch-Research-Paper
```

### **Step 2: Create a virtual environment (optional)**
```shell
python -m venv venv
source venv/bin/activate  # On MacOS or Linux
venv\Scripts\activate   # On Windows
```

### **Step 3: Install dependencies**
```shell
pip install -r requirements.txt
```

---

## 🚀 Usage
### **Basic Usage (Display Output on Console)**
Fetch papers for a specific query (like "cancer") and display the output:
```shell
python fetch_paper.py "cancer"
```

### **Save Output to CSV File**
If you want to save the output to a CSV file, use the `-f` or `--file` flag:
```shell
python fetch_paper.py "cancer" -f output.csv
```

This will generate a CSV file in the same directory with the following columns:
| PubmedID  | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|-----------|-------|------------------|------------------------|------------------------|----------------------------|
| 40063049  | Cell-based Immunotherapy in Esophageal Cancer. | Mar 10, 2025 | NKMAX Co., Ltd. | NKMAX Co., Ltd., Seongnam, Republic of Korea | inspector@yuhs.ac |


### **Enable Debug Mode**
If you want to see detailed logs during execution, use the `-d` or `--debug` flag:
```shell
python fetch_paper.py "cancer" -d
```

The output will show API responses, article IDs, and intermediate steps.

### **Combine File + Debug Mode**
Save the output and enable debug mode:
```shell
python fetch_paper.py "cancer" -f output.csv -d
```

## 📜 Merge CSV Files
If you have multiple output files like `pubmed_output.csv` and `output.csv`,
you can merge them using:
```shell
python merge_csv.py

## 📜 Merge CSV Usage
To merge the CSV files and generate a final consolidated file (final_output.csv):
```shell
python merge_csv.py

Expected Output in final_output.csv
PubmedID	Title	Publication Date	Non-academic Author(s)	Company Affiliation(s)	Corresponding Author Email
40063049	Cell-based Immunotherapy in Esophageal Cancer.	Mar 10, 2025	NKMAX Co., Ltd.	NKMAX Co., Ltd., Seongnam, Republic of Korea	inspector@yuhs.ac

| PubmedID  | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|-----------|-------|------------------|------------------------|------------------------|----------------------------|
| 40063049  | Cell-based Immunotherapy in Esophageal Cancer. | Mar 10, 2025 | NKMAX Co., Ltd. | NKMAX Co., Ltd., Seongnam, Republic of Korea | inspector@yuhs.ac |


### **Help Command**
If you're confused about the options, you can always run:
```shell
python fetch_paper.py -h
```
Output:
```
Usage: fetch_paper.py [QUERY] [OPTIONS]

Options:
  -f, --file TEXT     File to save the output (Optional)
  -d, --debug         Enable debug mode (Optional)
  -h, --help          Show this message and exit
```

---

## 📊 Output File Structure
The CSV file will have the following columns:
| PubmedID  | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|-----------|-------|------------------|------------------------|------------------------|----------------------------|
| 40063049  | Cell-based Immunotherapy in Esophageal Cancer. | Mar 10, 2025 | NKMAX Co., Ltd. | NKMAX Co., Ltd., Seongnam, Republic of Korea | inspector@yuhs.ac |

---

## 💡 Notes
- This program only captures articles where **at least one author** is affiliated with a **pharmaceutical or biotech company**.
- It uses email addresses and company names to identify non-academic authors.
- The PubMed API has a rate limit, so avoid querying too frequently.

---

## 📬 Contact
If you have any questions or issues, feel free to reach out to me at:
- **Email:** renukatondihal754@gmail.com
- **GitHub:** [renukatondihal754](https://github.com/renukatondihal754)

---

## ✅ Future Enhancements
- ✅ Deploy this tool as a Python package to **TestPyPI**.
- ✅ Add support for advanced query syntax.
- ✅ Integrate multi-threading for faster data extraction.

---

**Enjoy extracting research papers! 🚀😎**
