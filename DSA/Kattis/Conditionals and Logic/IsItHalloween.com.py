# get month and day
m, d = map(str, input().split())

(
    print("yup")
    if ((m == "OCT" and d == "31") or (m == "DEC" and d == "25"))
    else print("nope")
)
