def load_card(num_1bills,num_5bills,num_10bills,num_20bills):
	total_balance = (num_1bills*1) + (num_5bills*5) + (num_10bills*10) + (num_20bills*20)
	return total_balance	

print load_card(0,0,0,0)
print load_card(0,0,0,9)
print load_card(2,3,0,0)
print load_card(3,1,1,3)
