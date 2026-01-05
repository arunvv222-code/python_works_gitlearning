teachers_salar={

    "soumya":10000,
    "varsha":25000,
    "revathi":30000,
    "saranya":50000
}

srt_teachers=sorted(teachers_salar,key=lambda s : teachers_salar.get(s),reverse=True)

print(srt_teachers)