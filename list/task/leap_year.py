leap_year=[2021,1999,1920,2024,1852,1991,2026,2000,2023,2016,2009]

for y in leap_year:
    if y%100==0 and y%400==0 or y%100!=0 and y%4==0:

        print(y)

        