class Trailer():
    def __init__(self):
        self.size=0
        self.root=0
        self.xrefOffset= 0

        pass
    def __repr__(self):
        return f"trailer\n<< /Size {self.size}\n/Root {self.root}\n>>\nstartxref\n{self.xrefOffset}\n%%EOF"
    