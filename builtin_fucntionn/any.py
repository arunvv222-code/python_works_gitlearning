lst=["program","problem","perfect","apple"]

str_pro=[w.startswith("pro") for w in lst ]

is_any_ful=any(str_pro)

print(is_any_ful)