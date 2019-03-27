from catalog import Catalog
from outline import Outline
from pagetree import PageTree

class DocumentStructure():
    def __init__(self):
        self._objectNumber = 0
        self.objects = list()
        self.catalog = Catalog(self)
        self.outline = Outline(self)
        self.pageTree = PageTree(self)
        self.catalog.outlinesNumber = self.outline.objectNumber
        self.catalog.pageTreeNumber = self.pageTree.objectNumber


    def nextObjectNumber(self,):
        self._objectNumber += 1
        return self._objectNumber
        


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

        xref += '\n'
        return bodyString, xref


    def addPage(self):
        page = self.pageTree.addPage()
        return page


