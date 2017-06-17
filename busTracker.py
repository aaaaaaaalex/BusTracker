import math
from urllib.request import urlopen
from xml.etree.ElementTree import parse
import time


# here , I calculate the distance between two points on the surface of the Earth at sea-level.
# Since a change in the angle of a circle can represent different distances along the circumference
# depending on the radius, this function will lose accuracy as the altitude of a geographical area deviates.
def calculate_distance(lat_a, long_a, lat_b, long_b):
    earth_radius_sl = 6371
    earth_circ_sl = 2 * math.pi * earth_radius_sl
    given_circ_segment = math.sqrt(((lat_b - lat_a) ** 2) + ((long_b - long_a) ** 2))
    size_ratio_of_segment = given_circ_segment / 360
    distance_in_km = round((earth_circ_sl * size_ratio_of_segment), 3)
    return distance_in_km

# loop indefinitely, this loop will reiterate after a delay and get refreshed data from the web.
while 1 < 2:
    refreshTime = 20

    officeLat = 41.980262
    officeLong = -87.668452
    proximityWarning = 0.5
    # This is the distance within-which, any bus approaching
    # the above coordinates will alert the user.

    # Take data from the web and store it in an XML file for parsing
    u = urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
    data = u.read()
    f = open("rt22.xml", "wb")
    f.write(data)
    f.close()
    print("")
    print("")
    print("File Written Successfully")
    print("")


    print("Incoming Buses")
    doc = parse("rt22.xml")
    for bus in doc.findall("bus"):
        #parse the data for bus coordinates
        busLat = float(bus.findtext("lat"))
        busLong = float(bus.findtext("lon"))

        # Print different console notifications depending on the bus's direction and proximity to the
        # user, whose position is stored in the variables officeLat and officeLong
        if busLat >= officeLat:
            busName = bus.findtext("id")
            direction = bus.findtext("d")
            if direction.startswith("South"):
                proximity = calculate_distance(officeLat, officeLong, busLat, busLong)
                if proximity <= proximityWarning:
                    printString = "This bus is within " + str(proximity) + " KM of your position."
                    print(printString)
                print(busName, direction, busLat, busLong)
                print("")

        if busLat <= officeLat:
            busName = bus.findtext("id")
            direction = bus.findtext("d")
            if direction.startswith("North"):
                proximity = calculate_distance(officeLat, officeLong, busLat, busLong)
                if proximity <= proximityWarning:
                    printString = "This bus is within " + str(proximity) + " KM of your position."
                    print(printString)
                print(busName, direction, busLat, busLong)
                print("")

    # Delay the loop reiteration to control network usage and avoid redundant updates.
    startTime = time.monotonic()
    while abs(startTime-time.monotonic()) <= refreshTime:
        timeElapsed = abs(startTime - time.monotonic())
