def minion_game(string):
    # your code goes here
    vowel = 'AEIOU'
    ks = 0 # kevin score
    ss = 0 # stuart score
    
    for i in range(len(s)):
        if s[i] in vowel:
            ks += (len(s)-i)
        else:
            ss += len(s)-i
            
    if ks > ss:
        print(f"Kevin {ks}")
    elif ks < ss:
        print(f"Stuart {ss}")
    else:
        print(f"Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)