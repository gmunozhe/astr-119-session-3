#string

s = "I am a string."
print(type(s))		#will say string

#Boolean

yes = True			#Boolean true
print(type(yes))

no = False			#Boolean false
print(type(no))

#List -- ordered and changeable

alpha_list = ["a", "b", "c"]	#list initialization
print(type(alpha_list))			#will say tuple
print(type(alpha_list[0]))	#will say string
alpha_list.append("d")		#will add "d" to the list end
print(alpha_list)

#Tuple -- ordered and unchangeable

alpha_tuple = ("a", "b", "c")	#tuple initialization
print(type(alpha_tuple))	#will say tuple

try:								#attempt the following line
	alpha_tuple[2] = "d"				#won't work and will raise TypeError
except TypeError:
	print("We can't add elements to tuples!")	#print this msg
print(alpha_tuple)		#will print tuple


#purpose of tuples:  useful to prevent us from doing bad things??