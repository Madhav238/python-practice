with open("my_data.txt") as f:
    data=f.read()
with open("M.txt") as f:
    data2=f.read()
data+="\n"
data+=data2
with open("ABC.txt", "w") as f:
    f.write(data)
