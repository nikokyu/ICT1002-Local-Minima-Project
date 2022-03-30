#import numpy as np
#import matplotlib.pyplot as plt
global hessian_vecshaped 
hessian_vecshaped = [0,0,0,0]
global grad
grad = [0,0]

def valueonly_beale2d(dim, x):
    if (dim != 2):
        print("Dim is not 2")

    p1 = 1.5 - x[0] + x[0]*x[1]
    p2 = 2.25 - x[0] + x[0]*x[1]*x[1]
    p3 = 2.625 - x[0] + x[0]*x[1]*x[1]*x[1]

    ret = p1*p1 + p2*p2 + p3*p3

    return ret


def valueandderivatives_beale2d(dim, x):
    if (dim != 2):
        print("dim is not 2")
        exit(2)

    ret = valueonly_beale2d(dim, x)

    # gradient
    p1 = 1.5 - x[0] + x[0]*x[1]
    p2 = 2.25 - x[0] + x[0]*x[1]*x[1]
    p3 = 2.625 - x[0] + x[0]*x[1]*x[1]*x[1];

    grad[0] = 2*p1*(-1+x[1]) + 2*p2*(-1+x[1]*x[1]) + 2*p3*(-1+x[1]*x[1]*x[1])
    grad[1] = 2*p1*x[0] + 2*p2*2*x[0]*x[1] + 2*p3*3*x[0]*x[1]*x[1]

    q1 = -1+x[1]
    q2 = -1+x[1]*x[1]
    q3 = -1+x[1]*x[1] *x[1]
  
    hessian_vecshaped[0+2*0] = 2*q1*q1 + 2*q2*q2 + 2*q3*q3
    hessian_vecshaped[1+2*1] = 2*x[0]*x[0] + 8*x[0]*x[0]*x[1]*x[1] + 2*p2*2*x[0] + 18*x[0]*x[0]*x[1]*x[1]*x[1]*x[1] + 2*p3*6*x[0]*x[1]
  
    hessian_vecshaped[1+2*0] = 2*x[0]*q1 +2*p1 + 4*x[0]*x[1]*q2 + 2*p2*2*x[1] + 6*x[0]*x[1]*x[1]*q3 + 2*p3*3*x[1]*x[1]
                          
    hessian_vecshaped[0+2*1] = hessian_vecshaped[1+2*0]; 
    
    return ret



    

def main():
    x = [2, 0.5]
    #double = valueonly_beale2d(2, x)
    double = valueandderivatives_beale2d(2, x)
    print(double)
    print(hessian_vecshaped)
    print(grad)
    


main()
