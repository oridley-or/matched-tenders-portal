from sqlalchemy import create_engine, text

# Use raw string to handle Windows path correctly
DATABASE_URL = r"sqlite:///C:/Users/owena/OneDrive/Contract Business June 2025 Build/gov_contracts.db"

try:
    engine = create_engine(DATABASE_URL, echo=True)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
        print("Tables in database:")
        for row in result:
            print(row)
except Exception as e:
    print("Error connecting to the database:", e)
