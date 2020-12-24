def strCompare(sInput,sOfList):
    for i in range(len(min(sInput,sOfList))):
        if ord(sInput[i:i+1]) < ord(sOfList[i:i+1]):
            return True
        if ord(sInput[i:i+1]) > ord(sOfList[i:i+1]):
            return False

print(strCompare("zbc","cd"))