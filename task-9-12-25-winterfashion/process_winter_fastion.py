file_path="task-9-12-25-winterfashion\\Winter_Fashion_Trends_Dataset.csv"

fr=open(file_path,"r",encoding='utf-8')

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

#print length of data set

# print(len(data))

# print category and trending status

categry_trending={r.get("Category"):r.get("Trend_Status") for r in data}

# print(categry_trending)


#Find the top 5 highest-priced items.

lst_data=list(data)

sorted_data=sorted(lst_data,key=lambda x: float(x["Price(USD)"]), reverse=True)

highest_priced=[r.get("Brand") for r in sorted_data][:5]

# print(highest_priced)

# which is most popular brand

popularity=[float(r.get("Popularity_Score")) for r in data ]

max_pop=max(popularity)

most_pop_brand=[r.get("Brand")  for r in data if float(r.get("Popularity_Score"))==max_pop]

# print(most_pop_brand)

# trending brand in 2025

trending_brand_2025=[r.get("Brand") for r in data if r.get("Season")=="Winter 2025"
                     and r.get("Trend_Status")=="Trending"]

# print(set(trending_brand_2025))


# top 10 selling items

sorted_data_coustemer=sorted(lst_data,key=lambda x : x["Customer_Rating"],reverse=True)

selling_brand=[r.get("Category") for r in sorted_data_coustemer][:10]

# print(set(selling_brand))

#list of outdated fashion for men

fashion_outated=[r.get("Style") for  r in data if r.get("Trend_Status")=="Outdated" 
                 and r.get("Gender")=="Men"]

print(fashion_outated)
