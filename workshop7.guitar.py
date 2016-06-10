class Guitars:
    def __init__(self,name,year,cost):
        self.name=name
        self.year=year
        self.cost=cost
    def get_age(self):
        year=2016-self.year
        return year
    def is_vintage(self):
        if self.get_age()>50:
            return True
        else:
            return False
    def __str__(self):
        return '{:>20}({}),worth ${:10,.2f}'.format(self.name,self.year,self.cost)
