from email.policy import default
from .database import Base
from sqlalchemy import Column, Integer, String,Boolean,Float
from sqlalchemy.sql.expression import null


class Post(Base):
    __tablename__ = "gradestable"
    id = Column(Integer, primary_key=True, nullable=False)
    semester=Column(String, nullable=False)
    year=Column(Integer, nullable=False)
    subject = Column(String, nullable=False)
    code = Column(Integer, nullable=False)
    section=Column(String, nullable=False)
    atotal = Column(Integer,nullable = False)
    btotal = Column(Integer,nullable=False)
    ctotal = Column(Integer,nullable=False)
    dtotal= Column(Integer,nullable=False)
    ftotal= Column(Integer,nullable=False)
    aftotal = Column(Integer,nullable=False)
    gpa = Column(Float,nullable=False)
    itotal = Column(Integer,nullable=False)
    stotal = Column(Integer,nullable=False)
    utotal = Column(Integer,nullable=False)
    qtotal = Column(Integer,nullable=False)
    xtotal = Column(Integer,nullable=False)
    total = Column(Integer,nullable=False)
    prof = Column(String, nullable=False)
    mathcredit = Column(Boolean,nullable=False,default=False)
    commcredit = Column(Boolean,nullable=True,default=False)
    sciencecredit = Column(Boolean,nullable=True,default=False)
    langcredit = Column(Boolean,nullable=True,default=False)
    artcredit = Column(Boolean,nullable=True,default=False)
    americanhistorycredit = Column(Boolean,nullable=True,default=False)
    govcredit = Column(Boolean,nullable=True,default=False)
    socialcredit = Column(Boolean,nullable=True,default=False)





