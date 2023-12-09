from PyPDF2 import PdfReader, PdfWriter
import os
import glob
import random
def merge_pdfs_with_random_two_pages(pdf_directory, output_path):
  """
  Merges multiple PDFs, adding two random pages from each file in a directory, into one PDF.

  Args:
    pdf_directory: Path to the directory containing PDF files.
    output_path: Path to the merged PDF file.
  """

  writer = PdfWriter()

  # Get all PDF paths in the directory
  pdf_paths = glob.glob(os.path.join(pdf_directory, "*.pdf"))
  print(pdf_paths)
  # Process each PDF
  for pdf_path in pdf_paths:
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)

    # Randomly select two pages
    selected_pages = random.sample(range(num_pages), 2)
    print(pdf_path,selected_pages)
    for page_index in selected_pages:
      page = reader.pages[page_index]
      writer.add_page(page)

  # Write the merged PDF
  with open(output_path, 'wb') as output_file:
    writer.write(output_file)

# Example usage
pdf_questions = "questions"
pdf_solutions = "solutions"
question_output_path = "merged_random.pdf"
solution_output_path = "merged_random_solutions.pdf"
merge_pdfs_with_random_two_pages(pdf_questions, question_output_path)
merge_pdfs_with_random_two_pages(pdf_solutions, solution_output_path)

print(f'Merged PDFs into {question_output_path} and {solution_output_path}')
