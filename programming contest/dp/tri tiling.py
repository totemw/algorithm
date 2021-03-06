"""
Given n , find the number of ways to fill a 3 * n board with dominoes (1 * 2)



********   AA*******   AA******   A*******
******** = BB******* + B******* + A*******
********   CC*******   B*******   BB******
  f(n)   =  f(n-2)   +  g(n-1)  +  g(n-1)

********   A********   AA*******
******** = A******** + BB*******
 *******    ********    CC******
  g(n)   =   f(n-1)  +   g(n-2)


"""