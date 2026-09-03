def getWindLevelName(speed):
    if speed >= 32.7:
        print("Farvidri")
    elif speed >= 28.5:
        print("Ofsavedur")
    elif speed >= 24.5:
        print("Rok")
    elif speed >= 20.8:
        print("Stormur")
    elif speed >= 17.2:
        print("Hvassvidri")
    elif speed >= 13.9:
        print("Allhvass vindur")
    elif speed >= 10.8:
        print("Stinningskaldi")
    elif speed >= 8.0:
        print("Kaldi")
    elif speed >= 5.5:
        print("Stinningsgola")
    elif speed >= 3.4:
        print("Gola")
    elif speed >= 1.6:
        print("Kul")
    elif speed >= 0.3:
        print("Andvari")
    elif speed >= 0:
        print("Logn")


n = float(input())
getWindLevelName(n)
