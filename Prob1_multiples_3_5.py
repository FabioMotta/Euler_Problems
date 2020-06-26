
# Problem 1: Multiples of 3 and 5
# Author: Fabio Motta, 15.06.2020
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.


def sum_multiples(x):
    sum_of_multiples = 0

    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i

    return sum_of_multiples


def main():
    print(sum_multiples(1000))

    return 0


# The code above is missing a call! The interpreter cannot read the main function in this way. Two solutions:"
# calling the main function directly in the source code -main(), in line 29- or setting the special variable "
# __name__ to have value __main__ (line 32,33)"

main()


# if __name__ == "__main__":
#    main()
