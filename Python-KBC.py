print("Kon Banega Crorepati")

q = ("What is the capital of France?", "Which planet is known as the Red Planet?", "Who wrote the play Romeo and Juliet?", "What is the chemical symbol for water?", "Which is the largest continent by area?")
op = ("A) Berlin\nB) Madrid\nC) Paris\nD) Rome", "A) Venus\nB) Saturn\nC) Mars\nD) Jupiter", "A) Charles Dickens\nB) William Shakespeare\nC) Jane Austen\nD) Mark Twain", "A) H₂O\nB) O₂\nC) CO₂\nD) NaCl","A) Africa\nB) Europe\nC) Asia\nD) North America")

print(q[0])
print(op[0])
s = str(input("Enter your Answer: "))

if s=="C":
    print("Sahi jawaab!!, \nAapne jeete h 340000")
    
    print("Agla sawaal apki screen par ye rhaaaa\n")
    print(q[1])
    print(op[1])
    t = str(input("Enter your Answer: "))
    if t=="C":
        print("Sahi jawaab!!, \nAapne jeete h 640000")
        
        print("Agla sawaal apki screen par ye rhaaaa\n")
        print(q[2])
        print(op[2])
        a = str(input("Enter your Answer: "))
        if a == "B":
            print("Sahi jawaab!!, \nAapne jeete h 1250000 ")
        
            print("Agla sawaal apki screen par ye rhaaaa\n")
            print(q[3])
            print(op[3])
            b = str(input("Enter your Answer: "))
            if b =="A":
                print("Sahi jawaab!!, \nAapne jeete h 5000000")
        
                print("Agla sawaal apki screen par ye rhaaaa\n")
                print(q[4])
                print(op[4])
                c = str(input("Enter your Answer: "))
                if c=="C":
                    print("Sahi jawaab!!, \nAapne jeete h 1 crore\n Mubaarak ho aap bane h Crorepati ")
                else:
                    print("Afsos, aap haar chuke h apka safar yahi tak tha ")
            else:
                print("Afsos, Apka safar yahi tak thaa")
            
        else:
            print("Afsos, Apka safar yahi tak thaa")
    else:
        print("Afsos, Apka safar yahi tak thaa")
else:
    print("Afsos, Apka safar yahi tak thaa")
