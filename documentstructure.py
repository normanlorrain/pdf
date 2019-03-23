from catalog import Catalog
from outline import Outline
from pagetree import PageTree


def nextObjectNumber():
    nextObjectNumber.n+=1
    return nextObjectNumber.n
nextObjectNumber.n = 0






class DocumentStructure():
    def __init__(self):
        self.objects = list()
        self.catalog = Catalog()
        self.outline = Outline()
        self.pageTree = PageTree(self)
        self.catalog.outlinesNumber = self.outline.objectNumber
        self.catalog.pageTreeNumber = self.pageTree.objectNumber
        
        self.objects.append( self.catalog )
        self.objects.append( self.outline )
        self.objects.append( self.pageTree )

    # Serialize the objects in our structure. At the same time build the cross reference table.
    def generateBody(self, offsetInit ):
        offset = offsetInit
        bodyString = ""

        # Cross reference, indicated by "xref". For new doc, only have one of these "sections", 
        # next line indicates number of subsection (always 0 in our case), 
        # and number of entries to follow
        # See 3.4.3 in spec.
        xref = f"""xref
0 {len(self.objects)+1}
0000000000 65535 f
"""
        for pdfObject in self.objects:
            objectString = str(pdfObject)
            bodyString += objectString
            xref += f'{offset:010} 00000 n\n'
            offset += len(objectString)

        
        return bodyString, xref


    def addPage(self):
        page = self.pageTree.addPage()
        self.objects.append(page)


