import re

for i in range(40):
    age = int(input('Enter your age : '))
    if age <= 5:
        print("free ticket approved")
        print('Danger rides not approved ')
        continue
    elif age >=60 : 
        print('senior citizen, free passed approved')
        # Skip height input entirely for this group
        
    else:
        print('age above the free pass limit , free pass not approved')
        

    # Only ask for height if age > 5
    per_height = input('Enter your height in cm : ')
    ht_conv  = re.findall(r'\d+', per_height)
    ht_usecase = int(ht_conv[0])
    if ht_usecase >=160 : 
        print('danger rides are approved ')
    elif ht_usecase <160 : 
        print('danger rides are not approved')
        continue 
    if True: 
        print
    
        

    # if age > 60 and ht_usecase > 160:
    #     print('senior citizen , free pass approved')
    #     print('danger ride approved')
    # elif age > 60 and ht_usecase < 160:
    #     print('danger ride not approved')
    # elif ht_usecase > 160:
    #     print('Danger rides approved')
    # else:
    #     print('age above the free pass limit , free pass not approved')