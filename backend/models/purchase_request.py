from database import db_sql, ma 

db = db_sql

class PRequest(db.Model):
    __tablename__ = "purchase_request"
    __bind_key__ = "two"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10,2), nullable=False)
    supplier = db.Column(db.String(250), nullable=False)
    request_date = db.Column(db.Date, nullable = False)
    motive = db.Column(db.String(250), nullable = False)
    state = db.Column(db.Boolean, nullable = False, default=False)
    email_check= db.Column(db.String(250), nullable = True)

    def __init__(self, amount, supplier, request_date, motive):
        self.amount = amount 
        self.supplier = supplier 
        self.request_date = request_date 
        self.motive = motive 

class PRequestSchema(ma.Schema):
    class Meta: 
        fields = ("id", "amount", "supplier", "request_date", "motive", "state")

prequest_schema = PRequestSchema() 
prequests_schema = PRequestSchema(many=True) 
