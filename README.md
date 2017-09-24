# Tadhack 2017 - Brisbane QUT

## Region Board

### website
To get the website to run:
- download Xampp, start both the MySQL and Apache modules.
- Click on the 'Explorer' tab on the right side of Xampp and navigate into 'htdocs'
- Place the index.php file inside 'htdocs'
- Open a browser and type 'localhost' in the search bar and press ENTER

The website should now be up and running. However there may be issues with the database.
To get the database running:
- download MySQL Workbench
- setup a new connection with whatever name wanted, and a password within the 'store in vault'
- within index.php, which is the home page, change the 'new PDO' line parameters. Host to 'localhost' and dbname to the name of the schema.

This should fix everything and data should appear.
