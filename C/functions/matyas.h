#ifndef matyas_h
#define matyas_h

#include <stdio.h>
#include <stdlib.h>

double valueonly(int dim, double *x);
double valueandderivatives(int dim, double *x, double* grad,
  double *hessian_vecshaped);

#endif
