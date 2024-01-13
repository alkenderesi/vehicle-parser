import os
from dotenv import load_dotenv
from vehicle_parser import VehicleHandler, VehicleCollection


def main():
    load_dotenv()
    DATA_DIR = os.getenv("DATA_DIR") or "data"

    vehicles = VehicleCollection()
    vehicles.load(DATA_DIR, VehicleHandler)

    print(vehicles)


if __name__ == "__main__":
    main()
