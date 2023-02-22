
print("What proces do you need??")
print("[1] = Convert IP do binary")
print("[2] = Convert Binary ip to decial")
procces = int(input("Proces ID:"))

if procces == 1:
    print("Type IP")
    procces2 = input("IP:")
    ip = procces2
    split = ip.split('.')
    
if procces == 2:
    print("Type binary IP")
    procces2 = input("Binary IP:")
    binary_num = procces2





if procces == 1:
    def num_to_binary(number):
    # starší kod z mého githubu :D
        number = int(number)
        n2 = []
        n_SU = 0 
    
        while a == 0:
            n_SU = number % 2
            number = number // 2
            n2.append(n_SU)
            
            if number <= 0:
                n2.reverse()
                binary = ''.join(str(x) for x in n2)
            
                return binary
                a == 1

    final = []
    for number in split:
        a = 0
        binary = num_to_binary(number)

        final.append( binary + '.')
    
        
    else:
        final = ''.join(str(x) for x in final)
        print("##BINARY##")
        print(final)


if procces == 2:

    # Binary to Decimal

    binary_split = binary_num.split('.')
    def binary_to_decimal(binary):
        
        binary = int(binary)
        decimal = 0
        k = 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, k)

            binary = binary//10
            k += 1

        return decimal



    decnum = []
    for binary in binary_split:
        decimal = binary_to_decimal(binary)
        decnum.append(str(decimal) + '.')    
    else:
        final_decimal = ''.join(str(x) for x in decnum)
        print("##DECIMAL##")
        print(final_decimal)
        