from .models import session

class CRUD:
    def __init__(self,model):
        self.session = session
        self.model = model
    def add(self,**kwargs):
        obj=self.model(**kwargs)
        self.session.add(obj)
        self.session.commit()
        print("Successfully Added")

    def select_all(self):
        objects=self.session.query(self.model).all()
        return objects

    def select_column(self, column):
        return self.session.query(column).all()

    def select_filter_all(self,**kwargs):
        objs=self.session.query(self.model).filter_by(**kwargs).all()
        return objs

    def select_by_filter(self,**kwargs):
        try:
            obj=self.session.query(self.model).filter_by(**kwargs).first()
            return obj
        except Exception as e:
            print(e)

