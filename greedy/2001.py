pasta1 = int(input())
pasta2 = int(input())
pasta3 = int(input())

juice1 = int(input())
juice2 = int(input())

#get cheapest price of pasta
cheapPasta = min(pasta1, pasta2, pasta3)

#get cheapest price of juice
cheapJuice = min(juice1, juice2)

totalPrice = cheapPasta + cheapJuice

print( "%.1f"%(totalPrice * 1.1) )