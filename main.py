import pdf

pdfFile = pdf.File()
#print( pdfFile.fs )
page = pdfFile.addPage()
page.addContents()

raw = str(pdfFile.fs)
print( raw )

f = open('test.pdf', 'w', newline='\n')

f.write(raw)
f.close()

