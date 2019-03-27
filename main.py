import pdf

pdfFile = pdf.File()
page = pdfFile.addPage()
page.addContents("BT\n/F1 72 Tf\n100 100 Td\n1 Tr\n(Hello World) Tj\nET")

fileStructure = str(pdfFile.fs)
print( fileStructure )

f = open('test.pdf', 'w', newline='\n')

f.write( fileStructure )
f.close()

