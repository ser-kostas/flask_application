from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Bank

# Create a Blueprint for the routes
main_blueprint = Blueprint('main', __name__)

# Route: Home page to display all banks
@main_blueprint.route('/')
def index():
    banks = Bank.query.all()  # Fetch all banks from the database
    return render_template('index.html', banks=banks)


# Add a new bank
@main_blueprint.route('/add', methods=['GET', 'POST'])
def add_bank():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        location = request.form['location']

        # Create a new bank record
        new_bank = Bank(name=name, location=location)

        # Add to database session and commit
        db.session.add(new_bank)
        db.session.commit()

        # Redirect to the home page
        return redirect(url_for('main.index'))

    return render_template('add_bank.html')


# Route: Form to edit an existing bank
@main_blueprint.route('/edit/<int:bank_id>', methods=['GET', 'POST'])
def edit_bank(bank_id):
    bank = Bank.query.get_or_404(bank_id)
    if request.method == 'POST':
        bank.name = request.form['name']
        bank.location = request.form['location']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit_bank.html', bank=bank)


# Route: Delete a bank
@main_blueprint.route('/delete/<int:bank_id>')
def delete_bank(bank_id):
    bank = Bank.query.get_or_404(bank_id)
    db.session.delete(bank)
    db.session.commit()
    return redirect(url_for('main.index'))

