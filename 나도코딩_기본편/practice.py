def profile(name, age, *language):
    print(f"이름 : {name}\t나이 : {age}", end="\t")
    for lang in language:
        print(lang, end=" ")
profile("유재석", 20, "Python", "Kotlin")
    