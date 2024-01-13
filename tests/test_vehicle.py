import os
from dotenv import load_dotenv
from vehicle_parser import Car, Bicycle, VehicleHandler, VehicleCollection


load_dotenv()
DATA_DIR = os.getenv("DATA_DIR") or "data"


def test_load_car():
    car_data_path = f"{DATA_DIR}/A/AA0001.dat"
    vehicle_a: Car = VehicleHandler.load(car_data_path)
    vehicle_b = Car(id="AA0001", brand="Opel", doors=5)

    assert vehicle_a == vehicle_b


def test_load_bicycle():
    bicycle_data_path = f"{DATA_DIR}/B/BS3234.dat"
    bicycle_a: Bicycle = VehicleHandler.load(bicycle_data_path)
    bicycle_b = Bicycle(id="BS3234", brand="Csepel", max_weight=130)

    assert bicycle_a == bicycle_b


def test_load_vehicle_collection():
    vehicles = VehicleCollection()
    vehicles.load(DATA_DIR, VehicleHandler)

    test_vehicles = {
        Car(id="AA0001", brand="Opel", doors=5),
        Car(id="CD1234", brand="BMW", doors=3),
        Bicycle(id="BS3234", brand="Csepel", max_weight=130),
        Bicycle(id="DD0001", brand="Merida", max_weight=150),
    }

    assert len(vehicles.vehicles) == len(test_vehicles)

    for vehicle in vehicles.vehicles:
        assert vehicle in test_vehicles
