#

This script allows you to merge multiple PDFs into one PDF, selecting pages based on different algorithms.

### **Requirements**

-   Python 3
-   PyPDF2 library (install using `pip install PyPDF2`)

### **Features**

-   Merges multiple PDFs from a directory.
-   Supports three page selection algorithms:
    -   **Random (r):** Randomly selects a specified number of pages from each PDF.
    -   **Split (s):** Selects pages at a specified interval with an optional starting point.
    -   **Manual (m):** Allows user to manually select pages for each PDF.
-   Handles invalid user input and provides clear instructions.
-   Generates informative messages during execution.

### **Usage**

1. Download the script and save it to your computer.
2. Open a terminal and navigate to the directory containing the script and your PDF files.
3. Run the script with the following command:

`python main.py`

1. Choose the desired page selection algorithm by entering 'r' for random, 's' for split, or 'm' for manual.
2. If choosing the random or split algorithm, enter the number of pages to grab per file.
3. For the split algorithm, enter the starting page and step size (optional).
4. The script will merge the PDFs and save the merged PDF to a file named `merged_random.pdf` for questions and `merged_random_solutions.pdf` for solutions.

### **Additional notes**

-   You can customize the output filenames by modifying the script.
-   The `per_file` parameter for the random and split algorithms defaults to 2.
-   The `start` and `step` parameters for the split algorithm are optional and default to 0.

### **Example**

```bash
Python 3.11.0
Type "help", "copyright", "credits" or "license" for more information.
>>> python merge_pdfs.py
Select pages by (r)andom or (s)plit: s
Enter number of pages to grab per file: 2
Enter start page: 1
Enter step size: 2
Merged PDFs into merged_random.pdf and merged_random_solutions.pdf
```

This example merges PDFs with the split algorithm, selecting 2 pages per file starting from page 1 with a step size of 2.
