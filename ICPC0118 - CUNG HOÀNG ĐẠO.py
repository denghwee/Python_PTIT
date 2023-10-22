# I'm DengHwee or you can call me Chimmey

for i in range(int(input())):
    day, month = list(map(int, input().split()))
    if month == 1 :
        if day < 20 :
            print("Ma Ket")
        else :
            print("Bao Binh")
    elif month == 2 :
        if day < 19 :
            print("Bao Binh")
        else :
            print("Song Ngu")
    elif month == 3 :
        if day < 21 :
            print("Song Ngu")
        else :
            print("Bach Duong")
    elif month == 4 :
        if day < 20 :
            print("Bach Duong")
        else :
            print("Kim Nguu")
    elif month == 5 :
        if day < 21 :
            print("Kim Nguu")
        else :
            print("Song Tu")
    elif month == 6 :
        if day < 21 :
            print("Song Tu")
        else :
            print("Cu Giai")
    elif month == 7 :
        if day < 23 :
            print("Cu Giai")
        else :
            print("Su Tu")
    elif month == 8 :
        if day < 23 :
            print("Su Tu")
        else :
            print("Xu Nu")
    elif month == 9 :
        if day < 23 :
            print("Xu Nu")
        else :
            print("Thien Binh")
    elif month == 10 :
        if day < 23 :
            print("Thien Binh")
        else :
            print("Thien Yet")
    elif month == 11 :
        if day < 23 :
            print("Thien Yet")
        else :
            print("Nhan Ma")
    else :
        if day < 22 :
            print("Nhan Ma")
        else :
            print("Ma Ket")
