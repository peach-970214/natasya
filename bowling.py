frame = []
frames = []
tframe = []
keseluruhan =[]
extras=[]
mengira = 0
throwed=0
throws=0
total=0
totals=0
extra=0

#1-10 frame throw
for i in range (4):
    print("\nEnter frame ",i+1," result: ")
    print("1st ball: ")
    throw = int(input())
    frame.append(throw)

    while(throw>10 or throw<0):
        frame.pop(i)
        print("Please enter the correct number of pin(s).")
        print("1st ball: ")
        throw = int(input())
        frame.append(throw)

    if(throw==10):
        print("STRIKE!!!!!!!!")
        throws=0
        frames.append(throws)
    
    if(throw<10):
        
        print("2nd ball: ")
        throws = int(input())
        frames.append(throws)
        throwed=throw + throws
        if(throwed==10):
            print("SPARE!!!!!!!!")
   
    while(throwed>10 or throws<0):            
        frames.pop(i)
        print("Please enter the correct number of pin(s).")
        print("2nd ball: ")
        throws = int(input())
        frames.append(throws)
        throwed=throw + throws
        if(throwed==10):
            print("SPARE!!!!!!!!")
    totals=throw+throws
    tframe.append(totals)

    if(i == 0):
        mengira = sum(tframe)
    if(i != 0):
        mengira = sum(tframe)
    keseluruhan.append(mengira)

    #final calculation
    lewns=str(frame[i])
    kate=int(lewns)
    slew=str(frames[i])
    kats=int(slew)
    lewn=str(tframe[i])
    kat=int(lewn)
    if(lewns[i]==10):
        extra=kate[i]+kate[i+1]+kats[i+1]
        extras.append(extra)
        if(kate[i+1]==10):
            extra.pop(i)
            extra=extra+kate[i+2]
            extras.append(extra)
    elif(lewn[i]==10):
        extra=kat[i]+kate[i+1]
        extras.append(extra)

#extra throw if 10th frame is a strike
lasts=repr(frame)
lewns=str(frame[-1])
kate=int(lewns)
if (kate==10):
    print("\nEnter extra frame result: ")
    print("1st ball: ")
    throw = int(input())
    frame.append(throw)
    
    while(throw>10 or throw<0):
        frame.pop(i)
        print("Please enter the correct number of pin(s).")
        print("1st ball: ")
        throw = int(input())
        frame.append(throw)

    if(throw==10):
        print("STRIKE!!!!!!!!")
        print("2nd ball: ")
        throws= int(input())
        frames.append(throws)
        throwed=throw + throws
        while(throw>10 or throw<0):
            frames.pop(i)
            print("Please enter the correct number of pin(s).")
            print("2nd ball: ")
            throws = int(input())
            frames.append(throws)
        if(throwed==20):
            print("STRIKE!!!!!!!!")
        else:
            print("Good Game")

    if(throw<10):
        print("2nd ball: ")
        throws = int(input())
        frames.append(throws)
        throwed=throw + throws
        if(throwed==10):
            print("SPARE!!!!!!!!")

        while(throwed>20 or throws<0):
            frames.pop(i)
            print("Please enter the correct number of pin(s).")
            print("2nd ball: ")
            throws = int(input())
            frames.append(throws)
            throwed=throw + throws
            if(throwed==10):
                print("SPARE!!!!!!!!")
            else:
                print("Good Game")
    tframe.append(throwed)

#extra throw if 10th frame is a spare
last=repr(tframe)
lewn=str(tframe[-1])
kat=int(lewn)
if (kat==10):
    print("\nEnter extra frame result: ")
    print("1st ball: ")
    throw = int(input())
    frame.append(throw)
    while(throw>10 or throw<0):
        frame.pop(i)
        print("Please enter the correct number of pin(s).")
        print("1st ball: ")
        throw = int(input())
        frame.append(throw)
    if(throw==10):
        print("STRIKE!!!!!!!!")
        throws=0
        frames.append(throws)
    else:
        throws=0
        frames.append(throws)
        print("Good Game") 
    
#extra frame if user get all 10 frame spare or strike
if sum(tframe)==100:
    print("Enter bonus frame result: ")
    print("1st ball: ")
    throw = int(input())
    frame.append(throw)
    while(throw>10 or throw<0):
        frame.pop(i)
        print("Please enter the correct number of pin(s).")
        print("1st ball: ")
        throw = int(input())
        frame.append(throw)

    if(throw==10):
        print("STRIKE!!!!!!!!")
        throws=0
        frames.append(throws)

    if(throw<10):
        print("2nd ball: ")
        throws = int(input())
        frames.append(throws)
        throwed=throw + throws
        if(throwed==10):
            print("SPARE!!!!!!!!")

        while(throwed>10 or throws<0):
            frames.pop(i)
            print("Please enter the correct number of pin(s).")
            print("2nd ball: ")
            throws = int(input())
            frames.append(throws)
            throwed=throw + throws
            if(throwed==10):
                print("SPARE!!!!!!!!")
    tframe.append(throwed)



print("\n")
print("1st ball\t", frame)
print("2nd ball\t", frames)
print("Total pin(s)\t",tframe)
print("  Total \t", keseluruhan)
print("Totals\t",extras)
