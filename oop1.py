import os 

class Vehicle:
    total_vehicles = 0 
    def __init__(self,vehicle_id , brand , model , rental_price_per_day  ):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.is_rented = False
        Vehicle.total_vehicles += 1
    def rent(self):
        if self.is_rented:
            print("Vehicle is already rented")
        else:
            self.is_rented = True
            print(f"{self.brand} rented successfully!")
   
    def return_vehicle(self):
        self.is_rented = False
        print(f"{self.brand} available to rent")

    def calculate_rental_cost(self,days):
        return days* self.rental_price_per_day        
        
    def get_details(self):
        status = "Rented" if self.is_rented else "Available"
        return f"{self.brand}{self.model} - ${self.rental_price_per_day}/day - {status}"

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day,num_doors):
        super().__init__(vehicle_id, brand, model, rental_price_per_day, )
        self.num_doors = num_doors
        self.multiplier = 1.0

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * self.multiplier
    def get_details(self):
        status = "Rented" if self.is_rented else "Available"
        return f"car - {self.brand} {self.model} ({self.num_doors} tons) - ID: {self.vehicle_id} - ${self.rental_price_per_day}/day - {status}"

class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day,engine_cc):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.engine_cc = engine_cc
        self.multiplier=0.7

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * self.multiplier
    
    def get_details(self):
        status = "Rented" if self.is_rented else "Available"
        return f"Motorcycle - {self.brand} {self.model} ({self.engine_cc} tons) - ID: {self.vehicle_id} - ${self.rental_price_per_day}/day - {status}"

class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day,cargo_capacity_tons):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.cargo_capacity_tons = cargo_capacity_tons
        self.multiplier = 1.5

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * self.multiplier

    def get_details(self):
        status = "Rented" if self.is_rented else "Available"
        return f"Truck - {self.brand} {self.model} ({self.cargo_capacity_tons} tons) - ID: {self.vehicle_id} - ${self.rental_price_per_day}/day - {status}"

class Variable(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day,is_rented,total_vehicles):
        super().__init__(vehicle_id, brand, model, rental_price_per_day,is_rented)
        self.total_vehicles = total_vehicles
car = Car("V001", "Toyota", "Camry", 50, 4)
motorcycle = Motorcycle("V002", "Harley", "Street 750", 40, 750)
truck = Truck("V003", "Ford", "F-150", 80, 2.5)


car.rent()
print(car.is_rented)  

cost = car.calculate_rental_cost(5)
print(f"Rental cost for 5 days: ${cost}")

print(motorcycle.get_details())

car.rent()  

car.return_vehicle()
print(car.is_rented)  

print(f"Total vehicles: {Vehicle.total_vehicles}")