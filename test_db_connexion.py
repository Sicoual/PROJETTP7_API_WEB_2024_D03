from sqlalchemy import create_engine

# Database URL
DATABASE_URL = 'mysql+pymysql://digi:Digi123@localhost:3306/api_digicheese'

def test_connection():
    try:
        # Create an engine instance
        engine = create_engine(DATABASE_URL)

        # Connect to the database
        connection = engine.connect()
        print("Connection to the database was successful!")

        # Close the connection
        connection.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_connection()