# Tadhack 2017 - Brisbane QUT

## Region Board

### Website
To get the website to run:
- download Xampp, start both the MySQL and Apache modules.
- Click on the 'Explorer' tab on the right side of Xampp and navigate into 'htdocs'
- Place the index.php file inside 'htdocs'
- Open a browser and type 'localhost' in the search bar and press ENTER

### Database
The website should now be up and running. However there may be issues with the database.
To get the database running:
- download MySQL Workbench
- setup a new connection with whatever name wanted, and a password within the 'store in vault'
- within index.php, which is the home page, change the 'new PDO' line parameters. Host to 'localhost' and dbname to the name of the schema.

This should fix, there should not be any errors, and it is possible to print out data to test that it works.

### Apifonica messages
The code within the index.php for the site, contains the code necessary to send
msgs to Apifonica, which will send them to a specific phone number. On the file,
There are instructions on what to change, and what to leave, as well as descriptions
of what most things are. The main thing, would be changing the account name and
password, for a new Apifonica account, as well as the phone number to which the
messages are sent.
