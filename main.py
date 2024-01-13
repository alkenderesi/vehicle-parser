from vehicle_parser import VehicleHandler


def main():
    car = VehicleHandler.load("data/A/AA0001.dat")
    print(car)


if __name__ == "__main__":
    main()
