from page import Page

class PageTree():
    def __init__(self, ds):
        self.objectNumber = ds.nextObjectNumber()
        self.kids = []
        self.count = 0
        ds.objects.append(self)
        self.ds = ds


    def __repr__(self):
        return f"""{self.objectNumber} 0 obj
    << /Type /Pages
       /Kids {self.listKids()}
       /Count {self.count}
    >>
endobj

"""

    def listKids(self):
        kidString = '[ '
        for kid in self.kids:
            kidString+=f"{kid.objectNumber} 0 R\n"
        kidString+= '             ]'
        return kidString

    def addPage(self):
        print("adding page to tree")

        newPage = Page(self)
        self.kids.append(newPage)
        self.count += 1
        return newPage

