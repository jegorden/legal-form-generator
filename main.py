from docx import Document

document = Document()

document.add_heading('Patent Form', 0)

document.add_page_break()

document.save('demo.docx')
