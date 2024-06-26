import sqlite3
import os

# Database file path
DATABASE = '/nfs/demo.db'

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE)

def generate_test_data(num_contacts):
    """Generate test data for the contacts table."""
    db = connect_db()
    # Add the "email" column to the table if it doesn't exist
    db.execute('''ALTER TABLE contacts ADD COLUMN email TEXT''')
    db.commit()
    for i in range(num_contacts):
        name = f'Test Name {i}'
        phone = f'123-456-789{i}'
        email = f'test_email_{i}@example.com'  # Add email address
        db.execute('INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)', (name, phone, email))  # Include email in INSERT statement
    db.commit()
    print(f'{num_contacts} test contacts added to the database.')
    db.close()


if __name__ == '__main__':
    generate_test_data(10)  # Generate 10 test contacts.
