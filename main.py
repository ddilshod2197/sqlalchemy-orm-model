from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ma'lumotlar bazasi uchun yaratilgan engine
engine = create_engine('sqlite:///ma'lumotlar_bazasi.db')

# SQLAlchemy ORM uchun declarative_base
Base = declarative_base()

# Ma'lumotlar bazasi modeli
class Ma'lumotlarBazasiModel(Base):
    __tablename__ = 'ma'lumotlar_bazasi'

    id = Column(Integer, primary_key=True)
    ism = Column(String)
    familiya = Column(String)
    tug'ilgan_sana = Column(Date)

# Ma'lumotlar bazasi modelini yaratish
Base.metadata.create_all(engine)

# Session yaratish
Session = sessionmaker(bind=engine)
session = Session()

# Ma'lumotlar bazasiga ma'lumotlar qo'shish
ma'lumotlar_bazasi_model = Ma'lumotlarBazasiModel(
    ism='Ali',
    familiya='Vali',
    tug'ilgan_sana='1990-01-01'
)
session.add(ma'lumotlar_bazasi_model)
session.commit()

# Ma'lumotlar bazasidan ma'lumotlar olish
ma'lumotlar_bazasi_model = session.query(Ma'lumotlarBazasiModel).first()
print(ma'lumotlar_bazasi_model)
