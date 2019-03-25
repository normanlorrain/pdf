
class Catalog():
    def __init__(self,ds):
        self.objectNumber = ds.nextObjectNumber()
        self.outlinesNumber = 0
        self.pageTreeNumber = 0
        ds.objects.append(self)

    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Catalog
       /Outlines {self.outlinesNumber} 0 R
       /Pages {self.pageTreeNumber} 0 R
    >>
endobj

"""
