#Hello Jiho, it was a glad talking with you. 
#Here is my thinking process to the solution without using recursion. 

#The idea is :
#1:  Check the last byte, if it is larger than 127, return 2
#2:  Otherwise, starting from the second byte from the last, 
#    move to backwards until we can find the first byte that is 
#    smaller than 128. 
#3: Once we find that point, we just count how many bytes are in between and we 
#   can directly return the length of last char. 


#The reason is that once we find a value that is less than 128, we can make sure 
#that is an endpoint , either 1 byte char or 2 byte char, but we don't care. 
#And add bytes in between are in value larger than 128, and they are all double bytes chars, 
#So we just need to find if the last byte is connected with the one in front of it. 


def checkByte(byteArr):
    end = len(byteArr) - 1
    if byteArr[end] > 127: return 2
    currentPtr = end-1
    end = end - 1
    while (currentPtr > 0 and byteArr[currentPtr] > 127):
        currentPtr -= 1
    if byteArr[currentPtr] >127: currentPtr -= 1
    return (end - currentPtr) %2 + 1

#test 
arr1 = [125,129,129,127]
arr2 = [125,129,129,129,127]
arr3 = [129,127]
arr4 = [125,125]
print checkByte(arr1)
print checkByte(arr2)
print checkByte(arr3)
print checkByte(arr4)
