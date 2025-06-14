README – Vehicle Services: Relational to NoSQL Migration Project
Project Title
Migration of Data from a Relational Database to a NoSQL Database

Description
This project demonstrates how to design a relational database, populate it with realistic data, and migrate that data into a NoSQL database (MongoDB) using Python.

The topic I chose is Vehicle Services, which involves managing information about clients, vehicles, mechanics, and the services performed on those vehicles. The goal was to build an efficient data model in both SQL and NoSQL environments, justify the transition between them, and automate the migration process using code.

Technologies Used
I used PostgreSQL for the relational database and MongoDB for the NoSQL part. I managed PostgreSQL using pgAdmin4 and used MongoDB Compass to view the NoSQL data. The migration was written in Python, using the psycopg2 library to connect to PostgreSQL and pymongo to connect to MongoDB.

Database Design
In the relational model, I created five tables: Clients, Vehicles, Mechanics, Services, and a linking table called VehicleServices. These tables are connected with foreign key relationships to maintain data integrity. For example, each vehicle is linked to a specific client, and each record in VehicleServices links a vehicle, a service, and a mechanic, along with a service date and optional notes.

In MongoDB, I used a denormalized structure to make data access easier. Each document in the Vehicles collection represents a single vehicle. Inside that document, I embedded the client’s information as an object and included a list of all services performed on the vehicle. Each service includes the name, price, duration, date, notes, and the mechanic who performed it. This design avoids the need for joins and simplifies how we access data.

Steps Performed
I first created the database schema in PostgreSQL and inserted 15 realistic records into each table. After designing the relational model, I chose MongoDB as the target NoSQL database because its document-based format was perfect for grouping related data together in a single structure.

Then, I wrote a Python script that connects to PostgreSQL, performs SQL queries with joins to gather related data, and builds Python dictionaries to represent each vehicle, its client, and its service history. The script then connects to MongoDB and inserts these documents into the Vehicles collection. I used MongoDB Compass to confirm that the documents were correctly structured and all data was migrated successfully.

How to Run the Migration Script
Make sure you have Python installed and that both PostgreSQL and MongoDB are running on your machine.

Install the required libraries using the following command:
pip install psycopg2 pymongo

Open the migrate.py file and update the PostgreSQL credentials if needed.

Run the script using:
python migrate.py

If everything is configured correctly, you should see a message that says the migration completed successfully.

To check the results, open MongoDB Compass, connect to mongodb://localhost:27017, and open the VehicleService database. Go to the Vehicles collection to view the full documents with embedded client and service data.

Files Included
This project includes the Python script (migrate.py), this README file, a full project report in PDF (report.pdf), and a folder with screenshots from both pgAdmin and MongoDB Compass showing the populated data.

Author Notes
This project helped me understand how both relational and document-based databases work in practice. I learned how to model data for real-life use cases, how to automate data migration using code, and how to validate the results using database tools. Going through each step—from schema design, to writing code, to checking the final output—was a valuable hands-on learning experience.

