# models.py

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = "sqlite:///ecommerce.db"

# Create a base class for the models
Base = declarative_base()

# Define the Order class (table in SQLite)
class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    address = Column(String)
    product = Column(String)
    price = Column(Float)
    date = Column(String)

# Set up the SQLite engine and create the tables
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to save an order to the database
def save_order_to_db(db, name, email, address, cart):
    for item in cart:
        order = Order(
            name=name,
            email=email,
            address=address,
            product=item['product'],
            price=item['price'],
            date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Timestamp for the order
        )
        db.add(order)
    db.commit()
