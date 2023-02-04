#====================================================
# Filename: Prob3.py
# 
# Your name: Jake Grossamn
# Who did you work with (if anyone)?:none
# Estimate for time spent (in hrs)?:
#====================================================


def print_divisible_by_six_or_seven():
    """
    Prints all the numbers between 1 and 100 which are evenly divisible by 6 or 7,
    but not both. One number printed per line, and nothing is returned.
    """
    # Add your code here!
    n = 0
    while n<=100:
        if n%7==0 or n%6==0:
            if n%7!=0 and n%6==0:    
                print(f"this number is a multiple of 7 or 6, but not both: {n}")
            if n%7==0 and n%6!=0:
                print(f"this number is a multiple of 7 or 6, but not both: {n}")
        n += 1
    



def list_divisible_by_six_or_seven(min,max): # You'll need to add some parameters here
    """
    Takes two inputs to determine the minumum and maximum values in a range, and
    then returns a list of all the values between those numbers (including the ends)
    which are evenly divisible by 6 or 7, but not both.
    """
    # Add your code here!
    min = int(input("pick a minimum number for your range between 1 and 100:"))
    max = int(input("pick a maximum number for your range between 1 and 100:"))
    a = []
    n = min

    while n <= max:
        if n % 7 == 0 or n % 6 == 0:
            if n % 7 != 0 and n % 6 == 0:    
                a = a + [n]
            if n % 7 == 0 and n % 6 != 0:
                a = a + [n]

        n = n + 1

    return a

            

    














if __name__ == '__main__':
    print('Result of print_divisible_by_six_or_seven:')
    print_divisible_by_six_or_seven()
    print('Result of list_divisible_by_six_or_seven:') # You can uncomment this once you get to Part B
    print(list_divisible_by_six_or_seven(1,150)) # You can uncomment this once you get to Part B


