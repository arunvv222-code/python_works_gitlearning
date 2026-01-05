words=["hello","hai","hello","is"]

recursive_word=[]
non_recursive=[]

for ch in words:
  occ=  words.count(ch)
  if occ>1 and ch not in recursive_word:
    recursive_word.append(ch)
  elif occ ==1:
    non_recursive.append(ch)

  
  

print("recursive word=",recursive_word)
print("non recurisve word=",non_recursive)

    
