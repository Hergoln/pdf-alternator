from pypdf import PdfReader

reader = PdfReader("example-pdfs/Character-sheet-2e.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)