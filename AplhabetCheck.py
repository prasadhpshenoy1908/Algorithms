#############################################################
#
#Check the largest alphabet which is present in both capital and small letter
#  eg : Sms ZZ ate -> correct answer S. Incorrect answer Z
#
#############################################################
def solution(A):
    lowercase = [False] * 26
    uppercase = [False] * 26

    for char in A:
        if char.islower():
            ASCIIvalue = ord(char) - 97
            lowercase[ASCIIvalue] = True
        elif char.isupper():
            ASCIIvalue = ord(char) - 65
            uppercase[ASCIIvalue] = True
    iTer = 25
    while iTer :
        if  uppercase[iTer] and lowercase[iTer]:
            return chr(iTer + 65)
        iTer -= 1
    return "NO"


def main():
    A = "SMS messages are really w"
    print(solution(A))

if __name__ == "__main__":
    main()