import psycopg2
from pymongo import MongoClient

# 1. Connect to PostgreSQL
pg_conn = psycopg2.connect(
    dbname="VehicleServiceDB",  # name of your PostgreSQL database
    user="postgres",            # your PostgreSQL username
    password="admin",        # ← change this to your actual password
    host="localhost",
    port="5432"
)
pg_cursor = pg_conn.cursor()

# 2. Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["VehicleService"]         # name of the MongoDB database
mongo_collection = mongo_db["Vehicles"]           # name of the collection

# 3. Fetch all vehicles with their client information from PostgreSQL
pg_cursor.execute("""
SELECT v.VehicleID, v.PlateNumber, v.Brand, v.Model, v.Year,
       c.FullName, c.PhoneNumber, c.Email
FROM Vehicles v
JOIN Clients c ON v.ClientID = c.ClientID
""")
vehicles = pg_cursor.fetchall()

# 4. Loop through each vehicle
for vehicle in vehicles:
    vehicle_id, plate, brand, model, year, client_name, phone, email = vehicle

    # 5. Fetch all services related to the current vehicle
    pg_cursor.execute("""
    SELECT s.Name, s.Price, s.DurationMinutes, vs.ServiceDate, vs.Notes, m.FullName
    FROM VehicleServices vs
    JOIN Services s ON vs.ServiceID = s.ServiceID
    JOIN Mechanics m ON vs.MechanicID = m.MechanicID
    WHERE vs.VehicleID = %s
    """, (vehicle_id,))
    service_rows = pg_cursor.fetchall()

    # 6. Build a list of services for this vehicle
    services = []
    for s in service_rows:
        services.append({
            "name": s[0],
            "price": float(s[1]),
            "durationMinutes": s[2],
            "date": str(s[3]),       # convert date to string
            "notes": s[4],
            "mechanic": s[5]
        })

    # 7. Construct the document to insert into MongoDB
    document = {
        "plateNumber": plate,
        "brand": brand,
        "model": model,
        "year": year,
        "client": {
            "fullName": client_name,
            "phone": phone,
            "email": email
        },
        "services": services
    }

    # 8. Insert the document into MongoDB
    mongo_collection.insert_one(document)

# 9. Done!
print("✅ Migration completed successfully!")
