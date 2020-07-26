###################################################
#
#Given an array of positive and negative integers, 
#return the sign of product of all elements in array
#eg : [10, 11,-10,-10,-11] : -1
#
###################################################
def Test(A):
    if len(A) == 0:
        return 0

    Neg = 0
    for i in range(len(A)):
        if A[i] == 0:
            return 0
        elif A[i] < 0:
            Neg += 1
        
    if Neg > 0 and Neg%2 != 0:
        return -1
    else:
        return 1

def main():
    A = [-10,-10,10,-10]
    Test(A)

if __name__ == "__main__":
    main()
