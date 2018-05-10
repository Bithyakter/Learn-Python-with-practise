def main(): 
	
	print( "PrintDiamond_Demo" )
	
	print

	height = 5
	printDiamond( height )
	
def printDiamond( height ):
	
	width = height * 2 - 1
	
	for i in range( 0, height ):
		for j in xrange( width + 1 ):
			
			if j >= height - i and j <= height + i:
				print "a",
			else:
				print "  ",
		print
		
	for i in reversed( range( 0, height - 1 ) ):
		for j in xrange( width + 1 ):
			
			if j >= height - i and j <= height + i:
				print "a",
			else:
				print "  ",
		print
	
main()