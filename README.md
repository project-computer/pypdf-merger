# pdf-merger

This script allows you to merge multiple PDFs into one PDF, selecting pages based on different algorithms.

## Creates a virtual environment using venv

This function creates a virtual environment using the venv module in Python. It is compatible with both Windows and Linux operating systems.

Usage:

- For Windows:
  - Open Command Prompt or PowerShell.
  - Navigate to the directory where you want to create the virtual environment.
  - Run the following command:
     `python -m venv <venv_name>`
  - Activate the virtual environment by running:
      `<venv_name>\Scripts\activate`
- For Linux:
  - Open Terminal.
  - Navigate to the directory where you want to create the virtual environment.
  - Run the following command:
      `python3 -m venv <venv_name>`
  - Activate the virtual environment by running:
      `source <venv_name>/bin/activate`

Note: Replace `<venv_name>` with the desired name for your virtual environment.

For more information about using venv in Python, you can refer to the following blog post: [Python Virtual Environment (venv)](https://devhub.in.th/blog/python-virtual-environment-venv)

## **Requirements**

- Python 3
- PyPDF2 library (install using `pip install PyPDF2`)

## **Features**

- Merges multiple PDFs from a directory.
- Supports three page selection algorithms:
  - **Random (r):** Randomly selects a specified number of pages from each PDF file.
  - **Split (s):** Selects pages from each PDF file starting from a specified page number with a specified step size.
  - **Manual (m):** Allows the user to manually select pages from each PDF file.
- Handles invalid user input and provides clear instructions.
- Generates informative messages during execution.

## **Usage**

0. Create directory contain pdfs name `questions` and `solutions`
1. Download the script and save it to your computer.
2. Open a terminal and navigate to the directory containing the script and your PDF files.
3. Run the script with the following command:

```bash
 python main.py
 ```

1. Choose the desired page selection algorithm by entering 'r' for random, 's' for split, or 'm' for manual.
2. If choosing the random or split algorithm, enter the number of pages to grab per file.
3. For the split algorithm, enter the starting page and step size (optional).
4. The script will merge the PDFs and save the merged PDF to a file named `merged_random.pdf` for questions and `merged_random_solutions.pdf` for solutions.

### **Example**

```bash
>>> python main.py
Select pages by (r)andom or (s)plit or (m)anual:  r
Enter number of pages to grab per file: 2
{   'questions\\01-ข้อยากเซต.pdf': [11, 16],
    'questions\\02-ข้อยาก ตรรกะศาสตร์.pdf': [8, 3],
    'questions\\03-ข้อยากจำนวนจริง.pdf': [8, 20],
    'questions\\04-ข้อยากฟังก์ชัน.pdf': [41, 8],
    'questions\\05-ข้อยากภาคตัดกรวย.pdf': [27, 29],
    'questions\\06-ข้อยากเมทริก.pdf': [22, 14],
    'questions\\07-ข้อยาก Expo Log.pdf': [17, 20],
    'questions\\08-ข้อยากตรีโกณ.pdf': [23, 1],
    'questions\\09-ข้อยากเวกเตอร์.pdf': [3, 19],
    'questions\\10-ข้อยากจน.เชิงซ้อน.pdf': [6, 8],
    'questions\\11-ข้อยาก ทวินาม.pdf': [6, 5],
    'questions\\11-ข้อยาก อนุกรม.pdf': [8, 18],
    'questions\\12-ข้อยากแคล.pdf': [12, 56],
    'questions\\13-ข้อยาก สถิติ.pdf': [37, 18],
    'questions\\14-ข้อยาก คนจป.pdf': [3, 35],
    'questions\\15-ข้อยาก กำหนดการ.pdf': [18, 5]}
{   'solutions\\01-ข้อยากเซต.pdf': [11, 16],
    'solutions\\02-ข้อยาก ตรรกะศาสตร์.pdf': [8, 3],
    'solutions\\03-ข้อยากจำนวนจริง.pdf': [8, 20],
    'solutions\\04-ข้อยากฟังก์ชัน.pdf': [41, 8],
    'solutions\\05-ข้อยากภาคตัดกรวย.pdf': [27, 29],
    'solutions\\06-ข้อยากเมทริก.pdf': [22, 14],
    'solutions\\07-ข้อยาก Expo Log.pdf': [17, 20],
    'solutions\\08-ข้อยากตรีโกณ.pdf': [23, 1],
    'solutions\\09-ข้อยากเวกเตอร์.pdf': [3, 19],
    'solutions\\10-ข้อยากจน.เชิงซ้อน.pdf': [6, 8],
    'solutions\\11-ข้อยาก ทวินาม.pdf': [6, 5],
    'solutions\\11-ข้อยาก อนุกรม.pdf': [8, 18],
    'solutions\\12-ข้อยากแคล.pdf': [12, 56],
    'solutions\\13-ข้อยาก สถิติ.pdf': [37, 18],
    'solutions\\14-ข้อยาก คนจป.pdf': [3, 35],
    'solutions\\15-ข้อยาก กำหนดการ.pdf': [18, 5]}
```

This example merges PDFs with the split algorithm, selecting 2 pages per file starting from page 1 with a step size of 2.
