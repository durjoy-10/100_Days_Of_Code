"""write a program to manipulate pdf files using pyPDF.Your programs should be able to merge multiple
pdf files into a single pdf.You are welcome to add more functionalities. pyPDF is a free and
open-source pure-python pdf library capable of splitting,merging,cropping,and transforming the pagea
to pdf files.It can also add custom data, viewing options, and passwords to pdf files. pypdf can retrive
text from PDFs as well"""

from PyPDF2 import PdfMerger

import os

merger=PdfMerger()

files = ("pd1.pdf", "pd2.pdf", "pd3.pdf")

for pdf in files:
     merger.append(pdf)
     
     
merger.write("merged_file.pdf")
merger.close()