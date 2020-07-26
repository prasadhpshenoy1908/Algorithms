def solution (S, K):
    if len(S) == 0:
        return 0
    elif len(S) < K:
        return 1
    else:
        count = 0 
        smscount = 0
        messages = ''
        splitText = S.split()
        i = 0
        flag = False
        while i < len(splitText):
            text = splitText [i]
            flag = False
            if count + len(text) <= K:
                messages += text
                count += len(text)
                if len(messages) < K:
                    messages += ' '
                    count += 1
                    i += 1
                else:
                    flag = True
                    smscount += 1
                    messages = ''
                    count = 0
                    i += 1
            else:
                flag = True
                smscount += 1
                messages = ''
                count = 0
        if flag == False:
            smscount += 1

        return smscount 

def main():
    A = "SMS messages are really w"
    solution(A,13)

if __name__ == "__main__":
    main()