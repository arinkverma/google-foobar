import copy
from fractions import Fraction, gcd


def lcm(numbers): 
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

def create_M(r,c):
    row = []
    col = [0]*c
    for i in range(r):
        row.append(copy.deepcopy(col))
    return row

def mult_M(X,Y):
    result = create_M(len(X),len(Y[0]))
    # iterate through rows of X
    for i in range(len(X)):
       # iterate through columns of Y
       for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
    return result


def invert(X):
    """
    Invert a matrix X according to gauss-jordan elimination
    """
    #copy X to avoid altering input
    X = copy.deepcopy(X)

    #Get dimensions of X
    rows = len(X)
    cols = len(X[0])

    #Get the identity matrix and append it to the right of X
    #This is done because our row operations will make the identity into the inverse
    identity = []
    for i in xrange(0,rows):
        row = []
        for j in xrange(0,cols):
            row.append((1 if i==j else 0))
        identity.append(row)

    for i in xrange(0,rows):
        X[i]+=identity[i]

    i = 0
    for j in xrange(0,cols):
        print("On col {0} and row {1}".format(j,i))
        #Check to see if there are any nonzero values below the current row in the current column
        zero_sum, first_non_zero = check_for_all_zeros(X,i,j)
        #If everything is zero, increment the columns
        if zero_sum==0:
            if j==cols:
                return X
            raise Exception("Matrix is singular.")
        #If X[i][j] is 0, and there is a nonzero value below it, swap the two rows
        if first_non_zero != i:
            X[first_non_zero], X[i] = X[i], X[first_non_zero]
        #Divide X[i] by X[i][j] to make X[i][j] equal 1
        X[i] = [m/X[i][j] for m in X[i]]

        #Rescale all other rows to make their values 0 below X[i][j]
        for q in xrange(0,rows):
            if q!=i:
                scaled_row = [X[q][j] * m for m in X[i]]
                X[q]= [X[q][m] - scaled_row[m] for m in xrange(0,len(scaled_row))]
        #If either of these is true, we have iterated through the matrix, and are done
        if i==rows or j==cols:
            break
        i+=1

    #Get just the right hand matrix, which is now our inverse
    for i in xrange(0,rows):
        X[i] = X[i][cols:len(X[i])]

    return X

def check_for_all_zeros(X,i,j):
    non_zeros = []
    first_non_zero = -1
    for m in xrange(i,len(X)):
        non_zero = X[m][j]!=0
        non_zeros.append(non_zero)
        if first_non_zero==-1 and non_zero:
            first_non_zero = m
    zero_sum = sum(non_zeros)
    return zero_sum, first_non_zero


def answer(r):
    # r = [
    #   [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
    #   [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
    #   [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
    #   [0,0,0,0,0,0],  # s3 is terminal
    #   [0,0,0,0,0,0],  # s4 is terminal
    #   [0,0,0,0,0,0],  # s5 is terminal
    # ]

    if len(r) <= 2:
        return [1,1]
    
    m = []
    terminal = []
    terminal_count = 0
    transitional = []
    transitional_count = 0
    for i in xrange(len(r)):
        s = sum(r[i])
        if s == 0:
            terminal.append((terminal_count,i))
            terminal_count += 1
            m.append(list(Fraction(0,1) for k in r[i]))
        else:
            transitional.append((transitional_count,i))
            transitional_count += 1 
            m.append(list(Fraction(k,s) for k in r[i]))

    I_Q = create_M(transitional_count,transitional_count)
    R = create_M(transitional_count,terminal_count)
    for i in transitional:
        for j in transitional:
            if i == j:
                I_Q[i[0]][j[0]] = 1 - m[i[1]][j[1]]
            else:
                I_Q[i[0]][j[0]] = -1 * m[i[1]][j[1]]

        for j in terminal:
            R[i[0]][j[0]] = m[i[1]][j[1]]

    F = invert(I_Q)
    FR = mult_M(F,R)

    nr = []
    dr = []
    for a in FR[0]:
        nr.append(a.numerator)
        dr.append(a.denominator)

    l = lcm(dr)
    a = list(i[0]*l/i[1] for i in zip(nr,dr))
    a.append(l)

    return a


