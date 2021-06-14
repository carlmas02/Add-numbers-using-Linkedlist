class Node:
	def __init__(self,digit):
		self.digit = digit
		self.next = None

class Number:
	""" Represented as a linkedlist"""
	def __init__(self):
		self.head = None

	def reverse(self):
		curr = self.head
		prev,next_node = None,None
		while curr is not None:
			next_node = curr.next
			curr.next = prev
			prev = curr
			curr = next_node
		self.head = prev

	def traverse(self):
		num = ''
		curr = self.head
		while curr is not None:
			num+= str(curr.digit)
			curr = curr.next
		return num


	def node_at_beginning(self,data):
		new_node = Node(data)
		new_node.next = self.head 
		self.head = new_node


def getnumber(num,linkednum):
	linkednum = Number()
	while num>0:
		rem = num%10
		num//=10
		linkednum.node_at_beginning(rem)
	return linkednum	




#part2 reversing

 
#part3

def calculation(a,b):
	solution = Number()
	sum_,carry = 0,0
	a =a.head
	b =b.head
	while (a or b) is not None:
		sum_ = 0

		if a :
			sum_ += a.digit
		if b :
			sum_ += b.digit

		sum_ += carry
		carry = sum_//10

		solution.node_at_beginning(sum_%10)
		
		if a:
			a = a.next
		if b:
			b = b.next

	if carry:
		solution.node_at_beginning(carry)

	return solution







if __name__ == '__main__':
	#part1 - input and converting to a Linkedlist
	a = int(input("Enter a number :"))
	b = int(input("Enter second number :"))
	
	lst = getnumber(a,'num1')
	lst2 = getnumber(b,'num2')

	# part2 - reversing the linkedlist
	lst.reverse()
	lst2.reverse()

	#part3 - performing the calculation
	solution = calculation(lst,lst2).traverse()
	
	print(f'Solution obtained adding {a} and {b} is : {solution}')