from prac_09.unreliable_car import UnreliableCar

car1 = UnreliableCar("honda_trial_car", 2000, 40.0)
trials = 100
successful_drives = 0
distance_per_trial = 10

#Run trials
for i in range(trials):
    distance_driven = car1.drive(distance_per_trial)
    if distance_driven > 0:
        successful_drives += 1
#calculate success rate and check if it's in range or not
success_rate = (successful_drives/trials)*100
assert 30 <= success_rate <= 50, f"Success rate {success_rate}% not within expected range for 40% reliability"
print(f"Drive test: {successful_drives} successful drives out of {trials} (Success rate: {success_rate:.1f}%)")

