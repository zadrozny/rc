"""
Project Euler Problem 78
========================

Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can separated into piles in
exactly seven different ways, so p(5)=7.

                            OOOOO

                            OOOO   O

                            OOO   OO

                            OOO   O   O

                            OO   OO   O

                            OO   O   O   O

                            O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

from functools import wraps

def memo(func):
	cache = {}                        # Stored subproblem solutions
	print cache
	@wraps(func)                      # Make wrap look like func
	def wrap(*args):                  # The memoized wrapper
		if args not in cache:         # Not already computed?
			cache[args] = func(*args) # Compute & cache the solution
		return cache[args]            # Return the cached solution
	
	return wrap                       # Return the wrapper


@memo
def make_change(amount, coin_types): 
    if coin_types < 1 or amount < 0:
        return 0
    elif amount == 0:
        return 1
    else:
        return make_change(amount, coin_types-1) + \
               make_change(amount - denominations[coin_types-1], coin_types)

amount = 1
while True:
    denominations = range(1, amount+1)
    partitions = make_change(amount, len(denominations))
    # print amount, partitions
    if partitions == 1000000:
    	break 
    amount+=1



