# Outline is a structure of bookmarks.  See sec. 8.2.2

class Outline():
    def __init__(self, ds):
        self.objectNumber = ds.nextObjectNumber()
        self.count = 0
        ds.objects.append(self)


    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Outlines
       /Count {self.count}
    >>
endobj

"""