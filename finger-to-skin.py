# here used to be a mess of code attempting to generate the proper sequences
# but between things like 4k and 6k not using thumbs, or >10k modes
# I got confused so I decided to just hardcode them
# also today I learned that python identifiers cannot start with a number
# else it'll throw "invalid decimal literal" errors
# that's why it's "k1" instead of "1k" and so on

thumb = input("input your thumb note: ")
index = input("input your index note: ")
middle = input("input your middle note: ")
ring = input("input your ring note: ")
pinky = input("input your pinky note: ")
width = input("how wide are the notes supposed to be: ")
hitpos = input("what is your hit position: ")
scorepos = input("what is your score position: ")
combopos = input("what is your combo position: ")

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

def zeroes(n):
    r = ""
    for i in n:
        r += "0, "
    return r

for i in keycounts:
    print("[Mania]")
    print("Keys: " + str(len(i)))
    print("")
    print("TODO: other things for generating the whole skin.ini")
    print("")
    #CollumnStart: <- need to know the centering algorithm
    #ColumnWidth: <- need to know the centering algorithm
    print("ColumnLineWidth: " + zeroes(i))
    print("SplitStages: 0")
    print("HitPosition: " + str(hitpos))
    #LightPosition: <- do I need this even?
    #BarlineHeight: <- TODO figure this out
    #JudgementLine: <- TODO figure this out
    #NoteBodyStyle: <- TODO figure this out
    print("ScorePosition: " + str(scorepos))
    print("ComboPosition: " + str(combopos))
    count = 0
    for j in i:
        print("NoteImage" + str(count) + ": " + str(j))
        print("NoteImage" + str(count) + "H: " + str(j))
        print("NoteImage" + str(count) + "L: " + str(j))
        print("NoteImage" + str(count) + "T: " + str(j))
        count+=1
    print("")


