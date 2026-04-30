class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return (2026 - self.year) <= n


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        return f"[Car] VID: {self.vid} | {self.model} ({self.year}) | Fuel: {self.fuel_type} | {self.doors} Doors"


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return f"[Truck] VID: {self.vid} | {self.model} ({self.year}) | Load: {self.max_load}kg | {self.axles} Axles"


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.type = type

    def __str__(self):
        return f"[Motorcycle] VID: {self.vid} | {self.model} ({self.year}) | Eng: {self.engine_cc}cc | Type: {self.type}"



def save_fleet_to_file(vehicles, filename):
    file = open(filename, "w")
    for v in vehicles:
        if isinstance(v, Car):
            line = f"Car,{v.vid},{v.model},{v.year},{v.fuel_type},{v.doors}\n"
        elif isinstance(v, Truck):
            line = f"Truck,{v.vid},{v.model},{v.year},{v.max_load},{v.axles}\n"
        elif isinstance(v, Motorcycle):
            line = f"Motorcycle,{v.vid},{v.model},{v.year},{v.engine_cc},{v.type}\n"
        file.write(line)
    file.close()



def load_fleet_from_file(filename):
    vehicles = []
    file = open(filename, "r")
    for line in file:
        line = line.strip()
        parts = line.split(",")
        vehicle_type = parts[0]
        if vehicle_type == "Car":
            v = Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))
        elif vehicle_type == "Truck":
            v = Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]))
        elif vehicle_type == "Motorcycle":
            v = Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5])
        vehicles.append(v)
    file.close()
    return vehicles

my_vehicles = [
    Car("V001", "Tesla Model 3", 2023, "Electric", 4),
    Truck("T101", "Volvo FH16", 2019, 25000, 6),
    Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
    Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
    Truck("T102", "Mercedes Actros", 2021, 18000, 4),
    Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
]

save_fleet_to_file(my_vehicles, "fleet.txt")

print("Loading fleet data from 'fleet.txt'...")
loaded_vehicles = load_fleet_from_file("fleet.txt")
print(f"{len(loaded_vehicles)} vehicles loaded successfully.")

print("\n--- All Vehicles ---")
for v in loaded_vehicles:
    print(v)


print("\n--- Recent Vehicles (Last 4 Years) ---")
for v in loaded_vehicles:
    if v.is_new(4):
        print(v)

print("\n--- Electric Cars Only ---")
for v in loaded_vehicles:
    if isinstance(v, Car) and v.fuel_type == "Electric":
        print(v)
