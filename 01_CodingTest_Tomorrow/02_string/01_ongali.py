def ongali(babbling):
    able = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        for a in able:
            b = b.replace(a, ' ')
            
        b = b.strip()    
        if b == '':
            answer=answer+1    
    return answer

if __name__ == "__main__":
    res = ongali(babbling=["aya", "yee", "u", "maa", "wyeoo"])
    if res == 1:
        print("Correct")
    else:
        print("Wrong")

    res = ongali(babbling=["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])
    if res == 3:
        print("Correct")
    else:
        print("Wrong")