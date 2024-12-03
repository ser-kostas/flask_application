Bank Management System - Flask CRUD Application
-----------------------------------------------------------------------------------------------------------------
Description
This is a CRUD (Create, Read, Update, Delete) application built with Flask and SQL Server Management Studio.
The app allows you to create a list of bank, (name and address) and then you can add, view, edit or delete your info

-----------------------------------------------------------------------------------------------------------------

Project Structure:
flaskProject_validata/
├── app.py               # Main entry point for the Flask application
├── models.py            # Defines the database model for the 'Banks' table
├── routes.py            # Contains routes and handles the requests of the user
├── test_app.py          # Contains the tests to check the flask application
├── static/
│   ├── styles.css       # Contains a CSS file for styling the HTML templates
├── templates/
│   ├── base.html        # Base template for consistent layout
│   ├── index.html       # Homepage shows the list of banks
│   ├── add_bank.html    # Form to add a new bank
│   ├── edit_bank.html   # Form to edit an existing bank

-----------------------------------------------------------------------------------------------------------------

Database Setup
Create the Database
    Open Microsoft SQL Server Management Studio (SSMS).
    -Create a new database named validata
    -Create a table named Banks with 3 columns, 'id', 'name' and 'location'

-----------------------------------------------------------------------------------------------------------------

Database Configuration
In app.py, configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://@DESKTOP-H11M6GN/validata?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
)
Replace DESKTOP-H11M6GN with your SQL Server name.
    - Run SELECT @@ServerName; to find the Server name

-----------------------------------------------------------------------------------------------------------------

Installation and Setup
Prerequisites
Install Python 3.x on your system.
Install Microsoft SQL Server and SQL Server Management Studio
Install Flask and necessary libraries:

-----------------------------------------------------------------------------------------------------------------

Steps to Run the Application
Clone or download the project files.
Navigate to the project directory and make sure it has the correct structure as described in the project structure
Ensure the validata database and Banks table exist as described earlier in the setup instructions.
Run the app.py

-----------------------------------------------------------------------------------------------------------------

Steps the Run the test_app
Run the Flask application to confirm it starts successfully.
Install the pytest in your system
Run the following command to check the results 'pytest test_app.py'