##def getInfo():
##    var1 = input("\nplease provide the first numberic value: ")
##    var2 = input("\nplease provide the second numberic value: ")
##    return var1, var2
##
##
##def compute():
##    go = True
##    while go:
##        var1, var2 = getInfo()
##        try:
##            var3 = int(var1) + int(var2)
##            go = False
##        except ValueError as e:
##            print("{}: \n\nyou did not provide a numeric value".format(e))
##        except:
##            print("\n\noops, you provided invalid input, program will close now")
##    print("{} + {} = {}".format(var1, var2, var3))
##


def getN():
    go = True
    while go:
        letter = input("enter a lower case n: ")
        try:
            if letter == 'n':
                print("you correctly entered {}!".format(letter))
            go = False
        except:
            print("your letter is {}, please enter a letter n".format(letter))
        finally:
            print("invalid input. program failed")
    







if __name__ == "__main__":
    getN()

