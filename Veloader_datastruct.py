import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column

Base = declarative_base()

class velovtable(Base):
    __tablename__ = 'velovmaxence'

    index = Column (sqlalchemy.types.SmallInteger, primary_key=True)
    address = Column (sqlalchemy.types.String(300),index=True)
    address2 = Column (sqlalchemy.types.String(300),index=True)
    availability = Column (sqlalchemy.types.String(10))
    availabilitycode = Column (sqlalchemy.types.SmallInteger)
    available_bike_stands = Column (sqlalchemy.types.SmallInteger)
    available_bikes = Column (sqlalchemy.types.SmallInteger)
    banking = Column (sqlalchemy.types.String(10))
    bike_stands = Column (sqlalchemy.types.SmallInteger)
    bonus = Column(sqlalchemy.types.String(20))
    commune = Column (sqlalchemy.types.String(50),index=Tue)
    gid = Column (sqlalchemy.types.SmallInteger, primary_key=True)
    last_update= Column (sqlalchemy.types.DateTime,index=True)
    last_update_fme= Column (sqlalchemy.types.DateTime,index=True)
    lat= Column (sqlalchemy.types.Float(precision=18),index=True)
    lng= Column (sqlalchemy.types.Float(precision=18),index=True)
    name= Column (sqlalchemy.types.String(51),index=True)
    nmarrond= Column (sqlalchemy.types.SmallInteger,index=True)
    number= Column (sqlalchemy.types.SmallInteger)
    pole= Column (sqlalchemy.types.String(70))
    status= Column (sqlalchemy.types.String(10))
    dateinsert= Column (sqlalchemy.types.DateTime, primary_key=True)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)

velovTableColumnTypes={'index':sqlalchemy.types.SmallInteger,
                  'address':sqlalchemy.types.String(300),
                  'address2':sqlalchemy.types.String(300),
                  'availability':sqlalchemy.types.String(10),
                  'availabilitycode':sqlalchemy.types.SmallInteger,
                  'available_bike_stands':sqlalchemy.types.SmallInteger,
                  'available_bikes':sqlalchemy.types.SmallInteger,
                  'banking':sqlalchemy.types.String(10),
                  'bike_stands':sqlalchemy.types.SmallInteger,
                  'bonus':sqlalchemy.types.String(20),
                  'commune':sqlalchemy.types.String(50),
                  'geometry':sqlalchemy.types.Binary, #Inutile car on nettoie plus loin, mais je le laisse pour exemple
                  'gid':sqlalchemy.types.SmallInteger,
                  'last_update':sqlalchemy.types.DateTime,
                  'last_update_fme':sqlalchemy.types.DateTime,
                  'lat':sqlalchemy.types.Float(precision=18),
                  'lng':sqlalchemy.types.Float(precision=18),
                  'name':sqlalchemy.types.String(51),
                  'nmarrond':sqlalchemy.types.SmallInteger,
                  'number':sqlalchemy.types.SmallInteger,
                  'pole':sqlalchemy.types.String(70),
                  'status':sqlalchemy.types.String(10),
                  'dateinsert':sqlalchemy.types.DateTime,
                  }