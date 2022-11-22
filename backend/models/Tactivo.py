from database import db_sql, ma 

db = db_sql

class Tactivo(db.Model):
    __tablename__ = "tabla_activo"
    __bind_key__ = "three"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10,2), nullable=False)
    id_request = db.Column(db.Integer)
    date_gen = db.Column(db.Date, nullable = False)

    def __init__(self, amount, id_request, date_gen):
        self.amount = amount 
        self.id_request = id_request 
        self.date_gen = date_gen 

class TactivoSchema(ma.Schema):
    class Meta: 
        fields = ("id", "amount", "id_request", "date_gen")

tactivo_schema = TactivoSchema() 
tactivos_schema = TactivoSchema(many=True) 
