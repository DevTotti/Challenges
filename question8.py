import numpy as np

a = np.random.choice([0, 1], size = 4)

x = a.astype(int, copy=False)


print x
if x.all() == 0000:
    print "%s to Base 10 is: 0" %a

elif a.all() == 0001:
    print "%s to Base 10 is: 1" %a

elif a.all() == 0010:
    print "%s to Base 10 is: 2" %a

elif a.all() == 0011:
    print "%s to Base 10 is: 3" %a

elif a.all() == 0100:
    print "%s to Base 10 is: 4" %a

elif a.all() == 0101:
    print "%s to Base 10 is: 5" %a

elif a.all() == 0110:
    print "%s to Base 10 is: 6" %a

elif a.all() == 0111:
    print "%s to Base 10 is: 7" %a

elif a.all() == 1000:
    print "%s to Base 10 is: 8" %a

elif a.all() == 1001:
    print "%s to Base 10 is: 9" %a

else:
    print "Thanks for using this program"
