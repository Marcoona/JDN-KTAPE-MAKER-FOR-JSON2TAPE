print("ktape maker made by marcoona <3 this is used for yunyls json2tape tool \nplease credit me if you use this tool for your mods, thanks")

file=open("Lyrics.json", "w+")

starxdance = '''    "lyrics": [\n        {'''
file.write(starxdance)

def cum():

    time = input("time: ")
    dura = input("endtime: ")
    text = input("text: ")
    line = input("isLineEnding: ")

    timepar = '''            "time": ''' + time + ''',\n'''

    file.write(timepar)

    pissclit = int(dura) - int(time)

    durapar = '''            "duration": ''' + str(pissclit) + ''',\n'''

    file.write(durapar)

    tanpon = '''            "text": "''' + text + '''",\n'''

    file.write(tanpon)

    lain = '''            "isLineEnding": ''' + line + '''\n'''

    file.write(lain)

    corny = "        },\n        {\n"

    fag = "        }\n    ],"

    chase = input("do you want to continue? 1 = yes 2 = no ")

    if chase == "2":
        file.write(fag)
        file.close()
        input("Thanks for using this tool! if you use this tool in your mods please credit me,thanks! you can now close this by pressing enter")
        exit()
    if chase == "1":
        file.write(corny)
        cum()
    else:
        file.write(corny)
        cum()

cum()
