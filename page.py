import documentstructure as ds
class Page():
    def __init__(self, parent):
        self.parent = parent
        self.objectNumber = ds.nextObjectNumber()
        self.contentsObjectNumber = 0
        self.resourcesString = "<< >>" 
            #    /Contents {self.contentsObjectNumber} 0 R

    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Page
       /Parent {self.parent} 0 R
       /MediaBox [0 0 612 792]
       /Resources {self.resourcesString}

    >>
endobj

"""        

