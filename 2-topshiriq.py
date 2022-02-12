k = int(input("bahoni kirit "))
if 1<= k<=5:
    s ={
        1: "yomon",
        2: "qoniqarsiz",
        3: "qoniqarli",
        4: "yaxshi",
        5: "a'lo"
        }
    print(s.get(k))
else:
    print("xato")
