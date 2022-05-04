# Identifying and getting the hyperlinks in a pdf file
import pdfx
 

pdf = pdfx.PDFx("Cheran.pdf")
 

print(pdf.get_references_as_dict())
