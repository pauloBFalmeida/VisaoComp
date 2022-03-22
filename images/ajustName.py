import os

for i in range(1,5):
    for j in range(1, 201):
        num = ""
        if (j < 10):
            num += '00' + str(j)
        elif (j < 100):
            num += '0' + str(j)
        else:
            num = str(j)

        name = str(i)+'/ezgif-frame-'+num+'.png'
        # starts at 1/001.png      2/001.png
        # change to 0.png           200.png
        id = (i-1)*200 + j -1
        newName =  str(id)+'.png'

        old_file = os.path.join(".", name)
        new_file = os.path.join(".", newName)
        os.rename(old_file, new_file)
