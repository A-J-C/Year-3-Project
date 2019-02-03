#
#    File: baby_step.py
#    Author: Alexander Craig
#    Project: An Analysis of the Security of RSA & Elliptic Curve Cryptography
#    Supervisor: Maximilien Gadouleau
#    Version: 1.0
#    Date: 03/02/18
#
#    Functionality: uses the babystep-giant-step method to caclualte
#                   a private ECC key from a given public key set
#
#    Instructions: intended use is to import this file and use the Class as defined
#
#    CLI: for testing can be used from command line -
#           python3 baby_step.py PK_C PK_Q PK_G [verbose]
#

############ IMPORTS #########

import sys
import math

# allows me to run this file directly, i.e. not wrapped up in the package
if not __package__:
    sys.path.append('../')

from RSA.solver import Solver


############ MAIN CODE #########

class BFSolver(Solver):
    """ inherits from the default solver Class """

    def __init__(self, C = None, Q = None, G = None, v = True):
        super(BFSolver, self).__init__(C, Q, G, v)

    def solve(self):
        """ brute force by adding base point to itself until
            inf point is reached """

        # sanity check
        if self.G == None or self.C == None or self.Q == None:
            print("Can't solve not all parameters are set")
            return False                                            # unsuccessful

        ############ FIND MULTIPLIER #########
        self.count = 1                                              # initial count
        P = G                                                       # copy point

        # loop through all numbers looking for candidate until infinity
        while P != Q and P != C.pointAtInf():
            P += G                                                  # add another G
            self.count += 1                                         # increment count

        # sanity check
        if P != Q:
            print ("Point not found")
            return 0

        # set k once candidate found
        self.k = self.count

        if self.verbose:
            print("k:", self.k)

        return True


############ COMMAND LINE INTERFACE #########

if __name__ == '__main__':
    solver = BFSolver()

    if len(sys.argv) >= 3:
        solver.setN(int(sys.argv[1]))
        solver.setE(int(sys.argv[2]))
    if len(sys.argv) == 4:
        solver.setVerbose(int(sys.argv[3]))

    solver.solve()
