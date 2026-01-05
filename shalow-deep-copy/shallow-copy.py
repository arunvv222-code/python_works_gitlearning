from copy import copy

#used when we only need outter object copy

vri_fav_colour=["blue","black","red"]

shiva_fav_colour=copy(vri_fav_colour)

shiva_fav_colour.append("orange")

print(vri_fav_colour)

print(shiva_fav_colour)