from sqlalchemy import create_engine
def connectDB():
    engine = create_engine('sqlite:///bookkeeping.db', echo=True)

    print("Connected to DB!")