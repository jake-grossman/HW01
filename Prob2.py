#====================================================
# Filename: Prob2.py 
# 
# Your name: Jake Grossman
# Who did you work with (if anyone)?:none
# Estimate for time spent (in hrs)?: 5 min
#====================================================


# Define negate here

def negate(n):
    return "un" + n







# Define intensify here

def intensify(n):
    return "plus" + n







# Define reinforce here


def reinforce(n):
    return "double" + n






if __name__ == '__main__':
    # I've included the example in the description here for you to test against!
    print(negate("cold"))
    print(intensify("cold"))
    print(reinforce(intensify("cold")))
    print(reinforce(intensify(negate("good"))))
