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

    def __repr__(self):
        bodyString = ""
        for pdfObject in self.objects:
            bodyString += str(pdfObject)

        return bodyString

    def addPage(self):
        page = self.pageTree.addPage()
        self.objects.append(page)


