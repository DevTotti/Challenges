"""
Name: Osuntolu Paul
Email: neptunecody@gmail.com
Phone: 09025111684

Question B7: A recursive searching algorithm
"""

def binSearch(a_list, item):

    first = 0
    last = len(a_list) - 1

    while first <= last:
        i = (first + last) / 2

        if a_list[i] == item:
            return '{%s} found at position {%s}'%(item, i)
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        else:
            return '{item} not found in the list'.format(item=item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print "The list of number is: %s" %testlist
i = int(input("Enter a value from the list above: "))
print (binSearch(testlist, i))
