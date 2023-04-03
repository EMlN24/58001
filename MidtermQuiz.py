class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance

    def mtocm(self):
        return self.__distance * 100

    def mtokm(self):
        return self.__distance / 1000

    def mtoin(self):
        return self.__distance * 39.37

    def display(self):
        print(self.mtocm(), "cm")
        print(self.mtokm(), "km")
        print(self.mtoin(), "in")

convert = DistanceConversion(float(input("Please Enter a Distance in Meters: ")))
convert.display()