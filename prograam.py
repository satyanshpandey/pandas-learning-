def wrapperToffee(toffee, wrapper):
    totaltoffee = toffee   # initial toffees
    wrappers = toffee      # wrappers after eating

    while wrappers >= wrapper:
        new_toffees = wrappers // wrapper   # wrappers se naye toffee
        totaltoffee += new_toffees
        wrappers = wrappers % wrapper + new_toffees  # bache huye wrappers + naye wrappers

    return totaltoffee

toffee = 15
wrapperPerToffee = 3

print(wrapperToffee(toffee, wrapperPerToffee))  # Output: 22
