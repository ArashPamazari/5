n=int(input('tedad pishravi mosalas ra vared konid: '))

for i in range(1, n+1):
	for j in range(0, n-i+1):
		print(' ', end='')

	aval = 1
	for j in range(1, i+1):

		print(' ', aval, sep ='', end='')

		aval = aval * (i - j) // j
	print()
