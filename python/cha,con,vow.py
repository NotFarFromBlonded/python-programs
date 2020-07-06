def string(string):
    ctr = 0
    if string.isalpha():
        for i in string:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                ctr+=1
        print "no. of characters = ",len(string)
        print "no. of consonants = ",len(string)-ctr
        print "no. of vowels = ",ctr
def main():
    str = raw_input("enter a string=")
    string(str)
main()
            
