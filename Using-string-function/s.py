email = input("Enter Your Email: ")
k=0
j = 0
d = 0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j=1  
                    elif i.isdigit():
                        continue
                    elif i=="_"  or i=="." or i=="@":
                        continue
                    else:
                        d=1           
                if k==1 or j==1 or d==1:
                    print("Wrong Email | Check for symbols")        
                else:
                    print("Right Email")    
            else:
                print("Wrong Email | Please check if '.' is present or not and at what position ")
        else:
            print("Wrong Email | Please check if @ is present or how many @ is present") 
    else:
        print("Wrong Email | Please check if first letter is alphabet or not")
else:
    print(" Wrong Email | Please check the length of the email")