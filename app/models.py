from . import db

class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(15), nullable=False)
    is_selected = db.Column(db.Boolean, default=False)
    vendor = db.Column(db.String(100))  # 공급업체 필드 추가
    description = db.Column(db.String(255))  # 설명 필드 추가
    
    def __repr__(self):
        return f'<Server {self.name}>'
