distance = float(input ("Enter distance traveled waiting_time = int(input("Enter waiting time ")) fare = 0

if distance <= 100:
fare = distance * 10
elif distance <= 200:
fare = (100 * 10) + ((distance 100) * 9)
elif distance <= 700:
fare = (100 * 10) + (100 * 9) + ((distance - 200) * 6)
else:
fare = (100 * 10) + (100 * 9) + (500 6) + ((distance 700) * 6)

fare += waiting_time * 5 
print("Total Fare = Rs", fare)
