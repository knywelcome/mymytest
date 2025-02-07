def bottle_song(num):
	# write your code here!
	if num == 1:
		print("...")
		print("...")
		print("...")
		print("Take one down and pass it around, 1 bottle of beer on the wall.")
		print("1 bottle of beer on the wall, 1 bottle of beer.")
		print("Take one down and pass it around, no more bottles of beer on the wall.")
		print("No more bottles of beer on the wall, no more bottles of beer.")
		return "Go to the store and buy some more, 99 bottles of beer on the wall."
	else:
		print(f"{num} bottles of beer on the wall, {num} bottles of beer.")
		print(f"Take one down and pass it around, {num} bottles of beer on the wall.")
		return bottle_song(num-1)
		# print(num)

		

bottles = bottle_song(100)
print(bottles)

####kldjsfalkfdajalskdfjdfls