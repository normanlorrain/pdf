import pdf

pdfFile = pdf.File()
page = pdfFile.addPage()
page.addText("Hello World")

fileStructure = str(pdfFile.fs)
print( fileStructure )

f = open('test.pdf', 'w', newline='\n')

f.write( fileStructure )
f.close()

