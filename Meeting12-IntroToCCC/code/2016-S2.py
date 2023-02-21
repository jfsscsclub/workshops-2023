qType = input()
totalSpeed = 0
if qType =='1':
    n = input() # dont need this input
    # looking for min total speed
    dmojStan = input().split()
    pegLand = input().split()
    # make sure to convert everything to int, otherwise sorting will be weird
    dmojStan = [int(x) for x in dmojStan]
    pegLand = [int(x) for x in pegLand]
    dmojStan.sort()
    pegLand.sort()
    for i in range(len(dmojStan)):
        bikeSpeed = max(int(dmojStan[i]), int(pegLand[i]))
        totalSpeed += bikeSpeed
    print(totalSpeed)
else:
    n = input() # dont need this input
    # looking for max total speed
    dmojStan = input().split()
    pegLand = input().split()
    # make sure to convert everything to int, otherwise sorting will be weird
    dmojStan = [int(x) for x in dmojStan]
    pegLand = [int(x) for x in pegLand]
    dmojStan.sort()
    pegLand.sort()
    pegLand.reverse()
    for i in range(len(dmojStan)):
        bikeSpeed = max(int(dmojStan[i]), int(pegLand[i]))
        totalSpeed += bikeSpeed
    print(totalSpeed)