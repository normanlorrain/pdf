# Outline is a structure of bookmarks.  See sec. 8.2.2

import documentstructure as ds
class Outline():
    def __init__(self):
        self.objectNumber = ds.nextObjectNumber()
        self.count = 0


    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Outlines
       /Count {self.count}
    >>
endobj

"""