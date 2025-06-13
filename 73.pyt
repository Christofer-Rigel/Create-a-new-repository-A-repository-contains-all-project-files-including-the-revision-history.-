keypad = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def currentcombonation(combonation , curr , output , n):
    if (curr == n) : 
        print(*output,sep=" ")
        return
    
    for i in range (len(keypad[combonation[curr]])):
        output.append(keypad[combonation[curr]][i])
        currentcombonation(combonation,     curr + 1,   output,  n)
        output.pop()
        if (combonation[curr] == 0 or combonation[curr] == 1) : 
            return
        
combonation = [4,3,2]
n = len(combonation)
currentcombonation(combonation , 0 ,[], n)