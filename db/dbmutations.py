from sqlalchemy import create_engine
engine = create_engine('sqlite:///bookkeeping.db', echo=True)
def connectDB():
    engine.connect()
    print("Connected to DB!")

