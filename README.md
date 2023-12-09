## **Random PDF Merger**

This script merges multiple PDFs, adding two random pages from each file in a directory, into one PDF.

## **Requirements:**

-   Python 3.11+
-   PyPDF2 library

## **Instructions:**

1. Create two folders: `questions` and `solutions`.
2. Place your PDF files into the appropriate folder.
3. Run the `merge_pdfs_with_random_two_pages.py` script.
4. Two new PDFs will be created: `merged_random.pdf` and `merged_random_solutions.pdf` with two random pages from each question and solution PDF, respectively.

**Example Usage:**

**Bash**

```
python merge_pdfs_with_random_two_pages.py questions solutions
```

**Output:**

`Merged PDFs into merged_random.pdf and merged_random_solutions.pdf`

## **Note:**

-   This script assumes all PDF files are in the same directory.
-   The script will not overwrite existing files.

