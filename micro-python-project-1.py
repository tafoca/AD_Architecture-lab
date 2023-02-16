import uos as os


def initDir():
    os.mkdir("School")
    os.chdir("School")
    os.mkdir("Admin")
    os.mkdir("Customer")
    os.mkdir("SFees")
    os.chdir("Admin")
    open("users.txt","w").close()
    os.chdir("../Customer")
    open("customer.txt","w").close()
    os.chdir("../SFees")
    open("carte-info.txt","w").close()
    
def readFile():
    os.chdir("School/SFees")
    with open("carte-info.txt", "r") as f:
        content = f.read()
        print(content)
        
def file_to_array():
    os.chdir("School/SFees")
    with open("carte-info.txt", "r") as f:
        x = list()
        y = list()
        for line in f:
            data = line.split(" ")
            print(data)
            x.append(data[0])
            y.append(data[1].replace("\n",""))
            
        print(x)
        print(y)

def writeFile():
    os.chdir("School/SFees")
    x =  range(-5, 5, 1) 
    with open("value.dat", "w") as f:
        for i in x:
            val = f"{i} {f1(i)} \n"
            f.write(val)
        
def f1(x):
    return 2*x**2 + 9*x + 4

#1- initDir()
#2- readFile()
#3- file_to_array()
writeFile()





