Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> r = 0.05 / 12
>>> n =20 *12
>>> P =10000000
>>> A = P * (r *(1+r)**n)/((1+r)**n-1)
>>> print(A)
65995.57392166588
>>> outstanding =P
>>> print ('\t'. join(('Month', 'Instalment','Interest','Principal','Outstanding')))
Month	Instalment	Interest	Principal	Outstanding
>>> for i in range(1,13):
	i = i+1
	interest= r * outstanding
	principal=A-r*outstanding
	outstanding = outstanding-principal
	print('t\'.join(('{:03}'.format(i),'{0:.2f}'.format(A), '{0:.2f}'.format(interest),'{0:.2f}'.format(principal),'{0:.2f}'.format(outstanding))))
	      
SyntaxError: invalid syntax
>>> print('t\'.join(('{:03f}'.format(i),'{0:.2f}'.format(A), '{0:.2f}'.format(interest),'{0:.2f}'.format(principal),'{0:.2f}'.format(outstanding))))
	  
SyntaxError: invalid syntax
>>> print('t\'.join(('{:03}'.format(i),'{0:.2f}'.format(A), '{0:.2f}'.format(interest),'{0:.2f}'.format(principal),'{0:.2f}'.format(outstanding))))
	  
SyntaxError: invalid syntax
>>> 
