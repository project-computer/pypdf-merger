import random
# feature random
def get_random(num_pages, per_file=2):
  """
  Generates a list of random page numbers.

  Args:
    num_pages: The total number of pages in the PDF.
    per_file: The number of pages to select.

  Returns:
    A list of random page numbers.
  """
  return random.sample(range(num_pages), per_file)
# Feature manual
def get_manual(file_name,num_pages):
  """
  Gets user input for selecting pages from a PDF.

  Args:
    num_pages: The total number of pages in the PDF.

  Returns:
    A list of valid page numbers selected by the user.
  """
  pages = []
  while True:
    # Prompt user for input
    user_input = input(f"for {file_name} Enter page numbers separated by spaces (0-{num_pages-1}): ")

    # Check if input is empty
    if not user_input:
      break

    # Split input into individual numbers
    try:
      page_numbers = [int(x) for x in user_input.split()]
    except ValueError:
      print("Invalid input: Please enter only integers.")
      continue

    # Validate page numbers
    for page_number in page_numbers:
      if page_number < 0 or page_number >= num_pages:
        print(f"Invalid page number: {page_number}. Please enter a number between 0 and {num_pages-1}.")
        continue
      pages.append(page_number)

    # Check if user wants to add more pages
    add_more = input("Add more pages (y/N): ")
    if add_more.lower() != "y":
      break

  return pages

# Feature ทุก start step เช่นเว้นว่าง 3 4 5

def get_split(num_pages, start, step, max_pages_per_split=10):
  """
  Generates a list of page numbers by splitting the document into chunks.

  Args:
    num_pages: The total number of pages in the PDF.
    step: The step size for splitting the page range.
    max_pages_per_split: The maximum number of pages allowed in each chunk.

  Returns:
    A list of page numbers for the first chunk of the document.
  """
  # Create a list of page numbers with the specified step size
  page_list = list(range(start, num_pages, step))

  # Limit the number of pages returned to the maximum per split
  return page_list[:max_pages_per_split]