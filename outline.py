import documentstructure as ds
class Outline():
    def __init__(self):
        self.objectNumber = ds.nextObjectNumber()
        self.kids = None
        self.count = 0


    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Outlines
       /Count {self.count}
    >>
endobj

"""