import filestructure 
import documentstructure


class File():
    def __init__(self):
        self.ds = documentstructure.DocumentStructure()
        self.fs = filestructure.FileStructure(self.ds)
        #print(dir(self.ds))
    def addPage(self):
        print("adding page to pdf file ")
        return self.ds.addPage()


