import documentstructure as ds
class Page():
    def __init__(self, parent):
        self.parent = parent
        self.objectNumber = ds.nextObjectNumber()
        self.contentsObjectNumber = 0
        self.resourcesString = 0 
        
    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Page
       /Parent {self.parent} 0 R
       /MediaBox [0 0 612 792]
       /Contents {self.contentsObjectNumber} 0 R
       /Resources {self.resourcesString}

    >>
endobj

"""        

