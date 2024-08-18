def carFleet(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)
    fleets = []
    for pos, sp in cars:
        TimeToReach = (target - pos) / sp
        # print(TimeToReach)
        if not fleets or TimeToReach > fleets[-1]:
            fleets.append(TimeToReach)
    return len(fleets)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(carFleet(target, position, speed))  # Output: 2
