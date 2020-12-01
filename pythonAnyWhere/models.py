from app import db
import datetime
from sqlalchemy import DateTime

class allSensors(db.Model):
    __tablename__ = 'sensors'

    id = db.Column(db.Integer, primary_key=True)
    ts = db.Column(DateTime, default=datetime.datetime.utcnow)
    Temp1d4 = db.Column(db.Float())
    Temp2d5 = db.Column(db.Float())
    Temp3d6 = db.Column(db.Float())
    Temp4d13 = db.Column(db.Float())
    Temp5d19 = db.Column(db.Float())
    Temp6d26 = db.Column(db.Float())
    Temp7d21 = db.Column(db.Float())
    Temp8d20 = db.Column(db.Float())
    Temp9d16 = db.Column(db.Float())
    Temp10d12 = db.Column(db.Float())
    Temp11d1 = db.Column(db.Float())
    Temp12d7 = db.Column(db.Float())
    Temp13d8 = db.Column(db.Float())
    Temp14d24 = db.Column(db.Float())
    Temp15d23 = db.Column(db.Float())
    Temp16d18 = db.Column(db.Float())
    Temp17d15 = db.Column(db.Float())
    Temp18d14 = db.Column(db.Float())
    Temp19d2 = db.Column(db.Float())

    def __init__(self, id, ts, Temp1d4,Temp2d5,Temp3d6,Temp4d13,Temp5d19,Temp6d26,Temp7d21,Temp8d20,Temp9d16,Temp10d12,Temp11d1,Temp12d7,Temp13d8,Temp14d24,Temp15d23,Temp16d18,Temp17d15,Temp18d14,Temp19d2):
        self.id = id
        self.ts = ts
        self.Temp1d4 = Temp1d4
        self.Temp2d5 = Temp2d5
        self.Temp3d6 = Temp3d6
        self.Temp4d13 = Temp4d13
        self.Temp5d19 = Temp5d19
        self.Temp6d26 = Temp6d26
        self.Temp7d21 = Temp7d21
        self.Temp8d20 = Temp8d20
        self.Temp9d16 = Temp9d16
        self.Temp10d12 = Temp10d12
        self.Temp11d1 = Temp11d1
        self.Temp12d7 = Temp12d7
        self.Temp13d8 = Temp13d8
        self.Temp14d24 = Temp14d24
        self.Temp15d23 = Temp15d23
        self.Temp16d18 = Temp16d18
        self.Temp17d15 = Temp17d15
        self.Temp18d14 = Temp18d14
        self.Temp19d2 = Temp19d2




    def __repr__(self):
        return '<id {}>'.format(self.id)
    def serialize(self):
        return {
            'id': self.id,
            'ts': self.ts,
            'Temp1d4': self.Temp1d4,
            'Temp2d5':self.Temp2d5,
            'Temp3d6': self.Temp3d6,
            'Temp4d13': self.Temp4d13,
            'Temp5d19': self.Temp5d19,
            'Temp6d26': self.Temp6d26,
            'Temp7d21': self.Temp7d21,
            'Temp8d20': self.Temp8d20,
            'Temp9d16': self.Temp9d16,
            'Temp10d12': self.Temp10d12,
            'Temp11d1': self.Temp11d1,
            'Temp12d7': self.Temp12d7,
            'Temp13d8': selfTemp13d8,
            'Temp14d24': self.Temp14d24,
            'Temp15d23': self.Temp15d23,
            'Temp16d18': self.Temp16d18,
            'Temp17d15': self.Temp17d15,
            'Temp18d14': self.Temp18d14,
            'Temp19d2': self.Temp19d2
        }
