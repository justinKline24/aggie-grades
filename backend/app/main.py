from fastapi import FastAPI,Depends
from .database import engine,get_db
from . import models
from sqlalchemy.orm import Session,sessionmaker,scoped_session

models.Base.metadata.create_all(bind=engine)
conn=scoped_session(sessionmaker(bind=engine))

app = FastAPI()

@app.get("/class/{course}-{number}")
def get_class(number: int,course: str, db: Session = Depends(get_db)):
    result=conn.execute("""SELECT prof, COUNT(*), MAX(year),  SUM(atotal) AS suma, SUM(btotal),SUM(ctotal),SUM(dtotal),SUM(ftotal),SUM(aftotal), SUM(qtotal), CAST(AVG(gpa) AS DECIMAL(3,2)) FROM gradestable\
                WHERE code = %s AND subject= '%s' GROUP BY prof\
                ORDER BY MAX(year) DESC, AVG(gpa) DESC"""%(str(number),course))
    rows = result.fetchall()
    chart_result = conn.execute("""SELECT prof, gpa, semester,year FROM gradestable\
                WHERE code = %s AND subject= '%s'\
                """%(str(number),course))
    chart_rows = chart_result.fetchall()
    conn.commit()
    return {"all classes": rows, "chart return": chart_rows}
