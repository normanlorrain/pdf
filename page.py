import documentstructure as ds
class Page():
    def __init__(self, parent):
        self.parent = parent
        self.objectNumber = ds.nextObjectNumber()

    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Page
       /Parent {self.parent} 0 R
    >>
endobj

"""        

