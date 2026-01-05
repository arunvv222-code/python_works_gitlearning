lst=[10,20,40,24,64,74]

even_list=[n%2==0 for n in lst]

is_all_even=all(even_list)

print(is_all_even)


lst=["housefull","bueautiful","peaceful","harmful","thinkful","powerful"]

end_ful=[w.endswith("ful") for w in lst ]

is_all_ful=all(end_ful)

print(is_all_ful)

