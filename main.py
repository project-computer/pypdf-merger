from PyPDF2 import PdfReader, PdfWriter
import os
import glob
import random
import pprint
from select_algorithm import get_manual, get_random, get_split

def read_files(pdf_directory):
  """
  Reads all PDF files in a directory.

  Args:
    pdf_directory: Path to the directory containing PDF files.

  Returns:
    A list of PdfReader objects.
  """
  # Get all PDF paths in the directory
  pdf_paths = glob.glob(os.path.join(pdf_directory, "*.pdf"))

  # Process each PDF
  path_pages = {}
  for pdf_path in pdf_paths:
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)
    path_pages[pdf_path] = num_pages
  sorted_path_pages = dict(sorted(path_pages.items()))
  return sorted_path_pages


def select_pages(path_pages):
  """
  Selects pages from PDF files based on the specified algorithm.

  Args:
    path_pages (dict): A dictionary containing the paths of PDF files as keys and their corresponding page numbers as values.

  Returns:
    dict: A dictionary containing the selected pages for each PDF file.

  Algorithm Options:
    - 'r': Randomly selects a specified number of pages from each PDF file.
    - 's': Selects pages from each PDF file starting from a specified page number with a specified step size.
    - 'm': Manually selects pages from each PDF file.

  """
  select_algorithm = input("Select pages by (r)andom or (s)plit or (m)anual:  ")
  selected = {}
  i = 0

  if select_algorithm == 'r':
    per_file = int(input("Enter number of pages to grab per file: "))
    for value in path_pages.values():
      selected[i] = get_random(value, per_file)
      i += 1

  elif select_algorithm == 's':
    per_file = int(input("Enter number of pages to grab per file: "))
    start = int(input("Enter start page: "))
    step = int(input("Enter step size: "))
    for value in path_pages.values():
      selected[i] = get_split(value, start, step, per_file)
      i += 1

  elif select_algorithm == 'm':
    for key, value in path_pages.items():
      selected[i] = get_manual(key, value)
      i += 1

  return selected

def merge_pdfs(path_pages, output_path):
  writer = PdfWriter()
  for pdf_path, pages in path_pages.items():
    reader = PdfReader(pdf_path)
    for page_index in pages:
      page = reader.pages[page_index]
      writer.add_page(page)
  with open(output_path, 'wb') as output_file:
    writer.write(output_file)

def convert(d, m):
  a = {k: v for k, v in zip(d.keys(), m.values())}
  b = dict(sorted(a.items()))
  return b
           
def check_file_exists(file_path):
    """
    Checks if a file already exists.

    Args:
      file_path: Path to the file.

    Returns:
      True if the file exists, False otherwise.
    """
    return os.path.exists(file_path)

def generate_unique_file_name(file_path):
  """
  Generates a unique file name by appending a number to the file name.

  Args:
    file_path: Path to the file.

  Returns:
    A unique file name.
  """
  file_name, file_extension = os.path.splitext(file_path)
  counter = 1
  while check_file_exists(file_path):
    file_path = f"{file_name}_{counter}{file_extension}"
    counter += 1
  return file_path
if __name__ == "__main__":
  question_files =  read_files("questions")
  # solution_files = read_files("solutions")
  selected = select_pages(question_files)
  print(selected)
  print(question_files)
  # print(solution_files)
  selected_question = convert(question_files, selected)
  # selected_solution = convert(solution_files, selected)
  a = dict(sorted(selected_question.items()))
  # print(a)
  # print(selected_question)
  # print(selected_solution)
  # print(pprint.pformat(selected_question, indent=4))
  # print(pprint.pformat(selected_solution, indent=4))
  
  merged_random_file_path = generate_unique_file_name("exam-math.pdf")
  # merged_random_solutions_file_path = generate_unique_file_name("exam-math-sol.pdf")

  merge_pdfs(selected_question, merged_random_file_path)
  # merge_pdfs(selected_solution, merged_random_solutions_file_path)
