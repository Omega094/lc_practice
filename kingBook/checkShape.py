def checkShape(shape):
    lengthSet = set(shape)
    if len(lengthSet) == 1: return "Square"
    if len(lengthSet) == 2: return "Rectangle"
    else:
        return "Other"

if __name__ == "__main__":
    lengths = [(4,4,4,4), (6,5,6,5),(1,2,3,4),(1,1,1,1),(2,3,4,8)]
    for length in lengths:
        print checkShape(length)
