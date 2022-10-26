"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []
    i = 1

    if number_of_primes <= 0:  # Good error check
        raise (ValueError("This number is out of range!"))

    for x in range(0, number_of_primes):
        prime_found = False

        while (
            prime_found == False
        ):  # Can be a bit confusing constantly changing this variable
            i += 1
            prime_found = True
            for x in range(2, int(i**0.5) + 1):
                if i % x == 0:
                    prime_found = False
                    break
        list.append(i)

    return list
