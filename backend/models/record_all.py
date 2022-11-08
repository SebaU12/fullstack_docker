from database import db_sql, ma 

db = db_sql

class Record(db.Model):
    __tablename__ = "records_all"
    __bind_key__ = "two"
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(25), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    value = db.Column(db.Numeric(10,2), nullable=False)
    transaction_date = db.Column(db.Date, nullable = False)

    def __init__(self, transaction_id, description, value, transaction_date):
        self.transaction_id = transaction_id
        self.description = description 
        self.value = value 
        self.transaction_date = transaction_date 

class RecordSchema(ma.Schema):
    class Meta: 
        fields = ("transaction_id", "description", "value", "transaction_date")

record_schema = RecordSchema() 
records_schema = RecordSchema(many=True) 


