# here used to be a mess of code attempting to generate the proper sequences
# but between things like 4k and 6k not using thumbs, or >10k modes
# I got confused so I decided to just hardcode them
# also today I learned that python identifiers cannot start with a number
# else it'll throw "invalid decimal literal" errors
# that's why it's "k1" instead of "1k" and so on

thumb = input("please input your thumb note: ")
index = input("please input your index note: ")
middle = input("please input your middle note: ")
ring = input("please input your ring note: ")
pinky = input("please input your pinky note: ")

k1 = [thumb]
k2 = [index,index]
k3 = [index,thumb,index]
k4 = [middle,index,index,middle]
k5 = [middle,index,thumb,index,middle]
k6 = [ring,middle,index,index,middle,ring]
k7 = [ring,middle,index,thumb,index,middle,ring]
k8 = [ring,middle,index,thumb,thumb,index,middle,ring]
k9 = [pinky,ring,middle,index,thumb,index,middle,ring,pinky]
k10 = [pinky,ring,middle,index,thumb,thumb,index,middle,ring,pinky]
k13 = [ring,middle,index,ring,middle,index,thumb,index,middle,ring,index,middle,ring]
k17 = [pinky,ring,middle,index,pinky,ring,middle,index,thumb,index,middle,ring,pinky,index,middle,ring,pinky]
k18 = [pinky,ring,middle,index,pinky,ring,middle,index,thumb,thumb,index,middle,ring,pinky,index,middle,ring,pinky]

keycounts = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k13,k17,k18]

for i in keycounts:
    print(str(len(i)) + "K")
    count = 0
    for j in i:
        print("NoteImage" + str(count) + ": " + str(j))
        print("NoteImage" + str(count) + "H: " + str(j))
        print("NoteImage" + str(count) + "L: " + str(j))
        print("NoteImage" + str(count) + "T: " + str(j))
        count+=1


