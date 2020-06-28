#так было бы быстрее но просите wail((
#def max_num(val):
    #maxi = 0
    #for i in val:
      #  if int(i) > maxi:
     #       maxi = int(i)
    #return maxi

#value = input("Введите число")
#print(max_num(value))

def max_num(val):
    maxi = 0
    i = len(val)
    val = int(val)
    while i:
        if (val//(10**(i-1))) > maxi:
            maxi = (val//(10**(i-1)))

        val -= ((val//(10**(i-1)))*(10**(i-1)))
        i -= 1
    return maxi

value = input("Введите число")
print(max_num(value))