## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	i = 1
	j = 0

	while i <= x:
		if x % i == 0:
			j = j + 1
		i = i + 1

	l = x - 1
	k = 0

	while l >= 1 and k < j:
		a = 1
		k = 0
		while a <= l:
			if l % a == 0:
				k = k + 1
			a = a + 1
		l = l - 1

	if k >= j:
		res = "not anti-prime"
		return("not anti-prime")
	else:
		res = "anti-prime"
	
	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
		return("anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	import sys	
	if len(sys.argv) > 1:
		x = int(sys.argv[1])
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
		print(main(x))
