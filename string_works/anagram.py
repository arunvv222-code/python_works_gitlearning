def anagram(text1,text2):
   srt_txt1 = sorted(text1)
   srt_txt2 = sorted(text2)

   return srt_txt1 == srt_txt2

print(anagram("cat","actt"))
print(anagram("cat","act"))