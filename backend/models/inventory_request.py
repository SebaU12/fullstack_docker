from database import db_sql, ma 

db = db_sql

class IRequest(db.Model):
    __tablename__ = "inventory_request"
    __bind_key__ = "two"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(250), nullable=False)
    request_date = db.Column(db.Date, nullable = False)
    motive = db.Column(db.String(250), nullable = False)
    value = db.Column(db.Numeric(10,2), nullable=False)
    state = db.Column(db.Boolean, nullable = False, default=False)
    email_check= db.Column(db.String(250), nullable = True)

    def __init__(self, product_id, request_date, motive, value):
        self.product_id = product_id 
        self.request_date = request_date 
        self.motive = motive 
        self.value = value;

class IRequestSchema(ma.Schema):
    class Meta: 
        fields = ("id","product_id", "request_date", "motive", "value", "state")

irequest_schema = IRequestSchema() 
irequests_schema = IRequestSchema(many=True) 
