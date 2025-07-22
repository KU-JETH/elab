mydict = {
    "arm": ('n', "แขน"),
    "hello": ('v', "สวัสดี"),
    "beautiful": ('adj', "สวย"),
    "toilet": ('n', 'ห้องน้ำ'),
    "kick": ('v', 'เตะ'),
    "handsome": ('adj', 'หล่อ')
    }

def main():
    while True:
        x = input("")
        
        if x == "0":
            return
        
        if x not in mydict.keys():
            print("Word not in dictionary.")
            continue
        
        while True:
            n = input("")
            
            if not n.isdigit() or int(n) > 2 or int(n) <= 0:
                print("Invalid option.")
                continue 
            
            n = int(n)
            
            print(mydict[x][n - 1])
            break 

main()