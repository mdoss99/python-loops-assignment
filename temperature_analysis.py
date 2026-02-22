# Name: Mohandoss R
# Roll Number: iitp_aimltn_2602389
# Assignment: Python Loops & Automation - Subjective Question


print("===== Task 1: Find Maximum and Minimum =====")

temperatures = [28, 32, 35, 29, 31, 27, 30]

highest = temperatures[0]
lowest = temperatures[0]

for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

print("Highest Temperature:", highest, "°C")
print("Lowest Temperature:", lowest, "°C")


print("\n===== Task 2: Count Hot Days =====")

temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0

for temp in temperatures:
    if temp <= 30:
        continue
    hot_days += 1

print("Hot Days (>30°C):", hot_days)


print("\n===== Task 3: Alert System =====")

temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0

for i in range(len(temperatures)):
    temp = temperatures[i]

    if temp >= 40:
        print("Hot Days before alert:", hot_days)
        print("Alert! Extreme temperature", temp, "°C detected on Day", i + 1)
        break

    if temp > 30:
        hot_days += 1