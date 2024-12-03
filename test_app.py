import pytest
from app import app, db
from models import Bank

@pytest.fixture
def client():
    # Set up a test client and database for each test
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory SQLite for testing
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up after tests

def test_home_page(client):
    """Test if the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bank Table" in response.data

def test_add_bank(client):
    """Test adding a bank."""
    response = client.post('/add', data={
        'name': 'Test Bank',
        'location': 'Test City'
    })
    assert response.status_code == 302  # Redirect after adding
    with app.app_context():
        banks = Bank.query.all()
        assert len(banks) == 1
        assert banks[0].name == "Test Bank"

def test_edit_bank(client):
    """Test editing a bank."""
    with app.app_context():
        # Create a bank in the database
        bank = Bank(name="Old Name", location="Old Location")
        db.session.add(bank)
        db.session.commit()

        # Send a POST request to edit the bank
        response = client.post(f'/edit/{bank.id}', data={
            'name': 'New Name',
            'location': 'New Location'
        }, follow_redirects=True)

        # Fetch the updated bank
        updated_bank = Bank.query.get(bank.id)
        assert response.status_code == 200
        assert updated_bank.name == "New Name"
        assert updated_bank.location == "New Location"

def test_delete_bank(client):
    """Test deleting a bank."""
    with app.app_context():
        # Create a bank to delete
        bank = Bank(name="Bank to Delete", location="Location")
        db.session.add(bank)
        db.session.commit()

        # Send a POST request to delete the bank
        response = client.post(f'/delete/{bank.id}', follow_redirects=True)

        # Check that the bank no longer exists
        deleted_bank = db.session.get(Bank, bank.id)
        assert response.status_code == 200
        assert deleted_bank is None

