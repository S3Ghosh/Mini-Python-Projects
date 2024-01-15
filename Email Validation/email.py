email = input("enter your email :")
j,k,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]=='.') ^ (email[-3]=="."):             # Using xor operator, if both true or both are false then answer is false. Have not used or operator, if mail has 2 .. then also condition is true
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                       if i==i.upper():
                          j=1  
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1                  # %,&, for special characters
                if k==1 or j==1 or d==1:
                    print("wrong email, condition 5 not satisfied.")
                else:
                    print("Email is right")         
            else:
                print("wrong email, condition 4 not satisfied.")                                
        else:                                                                                   
            print("wrong email, condition 3 not satisfied.")
    else:
        print ("wrong email, condition 2 not satisfied.")
else:
    print("wrong email, condition 1 not satisfied.")
