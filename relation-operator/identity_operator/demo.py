# to chk object is pointing the same location or not

resin_fvt_food = "biriyani"     # in small string case python doesnt share two location 
arun_fvt_food = "biriyani"

print(resin_fvt_food == arun_fvt_food)

print(resin_fvt_food is arun_fvt_food)

print("a" in resin_fvt_food)

resin_fvt_place = ["wayanad","iddukki","banglore"]
arun_fvt_place = ["wayanad","iddukki","banglore"]   
                                                   
print(resin_fvt_place is arun_fvt_place)

# in the case of collection it creates diffrent locations
# exception in small string cases
