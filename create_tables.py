from sqlalchemy import create_engine
from app.database.base import Base # Correct import based on your folder structure

# Path to your existing SQLite database
DATABASE_URL = "sqlite:///C:/Users/owena/OneDrive/Contract Business June 2025 Build/gov_contracts.db"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create missing tables safely (won't overwrite existing ones)
Base.metadata.create_all(engine)

print("Tables created or confirmed existing.")
