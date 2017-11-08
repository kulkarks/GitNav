# GitNav
A tool for navigating the most starred public python projects on Github.

Using the github API, a database was created by requesting the most starred public python projects.  These projects were saved in the Repositories.db file, which is a sqlite database.

Using Python's Flask framework, the application was created with a single endpoint where a web page is displayed.  The application queries the database file using sqlalchemy and displays the repositories in the database in an HTML file using Jinja templating.  Jquery 3.2.1 and Bootstrap 3.7 were used to display the collapsible panels in the HTML file.
