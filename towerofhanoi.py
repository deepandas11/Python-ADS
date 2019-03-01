

def moveDisk(fp, tp):
    print("Moving disk from "+str(fp)+" to "+str(tp)+".")

def moveTower(height,fromP, withP, toP):
    if height>=1:
        moveTower(height-1, fromP,toP,withP)
        moveDisk(fromP,toP)
        moveTower(height-1, withP, fromP, toP)


moveTower(4, "A", "B", "C")

