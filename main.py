from PyPDF2 import PdfReader, PdfWriter
import os
import glob
import random

from select_algorithm import get_manual, get_split

# def read_files(pdf_directory):
#   """
#   Reads all PDF files in a directory.

#   Args:
#     pdf_directory: Path to the directory containing PDF files.

#   Returns:
#     A list of PdfReader objects.
#   """
#   # Get all PDF paths in the directory
#   pdf_paths = glob.glob(os.path.join(pdf_directory, "*.pdf"))

#   # Process each PDF
#   path_pages = {}
#   for pdf_path in pdf_paths:
#     reader = PdfReader(pdf_path)
#     num_pages = len(reader.pages)
#     path_pages[pdf_path] = num_pages

#   return path_pages

def merge_pdfs(pdf_directory, output_path, select_algorithm='r', per_file=2, step=2, start=0):
  """
  Merges multiple PDFs, adding two random pages from each file in a directory, into one PDF.

  Args:
    pdf_directory: Path to the directory containing PDF files.
    output_path: Path to the merged PDF file.
  """
 

  writer = PdfWriter()

  # Get all PDF paths in the directory
  pdf_paths = glob.glob(os.path.join(pdf_directory, "*.pdf"))
  # Process each PDF
  for pdf_path in pdf_paths:
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)

    # Randomly select two pages
    
    if (select_algorithm == 'r'):
      selected_pages = random.sample(range(num_pages), per_file)
    elif (select_algorithm == 's'):
      selected_pages = get_split(num_pages, start, step, per_file)
    elif (select_algorithm == 'm'):
      selected_pages = get_manual(pdf_path,num_pages)

    # selected_pages = random.sample(range(num_pages), 2)
    print(pdf_path,selected_pages)
    for page_index in selected_pages:
      page = reader.pages[page_index]
      writer.add_page(page)

  # Write the merged PDF
  with open(output_path, 'wb') as output_file:
    writer.write(output_file)

if __name__ == "__main__":
  select_algorithm = input("Select pages by (r)andom or (s)plit:  ")
  per_file = 2
  step=0
  start=0
  if (select_algorithm == 'r' or select_algorithm == 's'):
    per_file = int(input("Enter number of pages to grab per file: "))
    if (select_algorithm == 's'):
      start = int(input("Enter start page: "))
      step = int(input("Enter step size: "))
  # # Example usage
  pdf_questions = "questions"
  pdf_solutions = "solutions"
  question_output_path = "merged_random.pdf"
  solution_output_path = "merged_random_solutions.pdf"
  
  # print(read_files(pdf_questions))
  # print(read_files(pdf_solutions))
  merge_pdfs(pdf_questions, question_output_path, select_algorithm, per_file, step, start)
  merge_pdfs(pdf_solutions, solution_output_path, select_algorithm, per_file, step, start)

  print(f'Merged PDFs into {question_output_path} and {solution_output_path}')
