import pdf

pdfFile = pdf.File()
#print( pdfFile.fs )
pdfFile.addPage()

raw = str(pdfFile.fs)
print( raw )

f = open('test.pdf', 'w', newline='\n')

f.write(raw)

