user_time = int(input("Please enter the time in hours (HH:xx:xx): "))

if user_time > 24:
    print('That is not a real time.')
    print()
    new_user_time = int(input('Enter the correct time format: '))
    user_time = new_user_time
    print()

if user_time <= 0:
    print('That is not a real time.')
    print()
    new_user_time = int(input('Enter the correct time format: '))
    user_time = new_user_time
    print()

alarm_hours = int(input("How many hours until your alarm goes off?  (HH:xx:xx): "))
print()

military_alarm = user_time + alarm_hours

for i in range (alarm_hours):
    if military_alarm > 24:
        military_alarm = military_alarm - 24

print('Your alarm will sound at {}:00 Military Time'.format(military_alarm))


###CODE THAT DIDN'T WORK###

#
#
# elif user_time > 12:
#     user_time = user_time - 12
#     print('The time is now', user_time, 'o\'clock')
#     print()
#     print('How many hours until your alarm sounds?')
#     print()
#     alarm_hours = input("Please enter the time in hours (HH:xx:xx): ")
#
# else:
#     print('The time is now', user_time, 'o\'clock')
#     print()
#     print('How many hours until your alarm sounds?')
#     print()
#     alarm_hours = input("Please enter the time in hours (HH:xx:xx): ")
# for i in range(alarm_hours):
#     user_time + i
#     if user_time > 12:
#         user_time =
#timesofday = ['12AM','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12PM', '1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM']
# militarytime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# time_dictionary = dict(zip(timesofday,militarytime))