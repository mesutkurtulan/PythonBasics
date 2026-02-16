'''
Write a short expression in Python that does the following with a list comprehension:
Select only the even numbers from 1 to 20
Square each number
Put the result into a new list
Example output expected: [4, 16, 36, 64, ..., 400]
'''

squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(1, 21))))
print(f"squares: {squares}")

'''
Create the following list with a single line of list comprehension:
Pythonoriginal = [5, 12, 7, 3, 18, 9, 4, 15]
Let the new list be:
If the number is greater than 10 → multiply the number by 2
Otherwise → make the number -1 (negative)

Expected output:
[-1, 24, -1, -1, 36, -1, -1, 30]
'''
Pythonoriginal = [5, 12, 7, 3, 18, 9, 4, 15]
print(list([x*2 if x > 10 else -1 for x in Pythonoriginal]))

'''
test_data = [
    {"username": "user1", "password": "pass123", "expected": "success"},
    {"username": "user2", "password": "wrong", "expected": "fail"},
    {"username": "", "password": "pass456", "expected": "fail"},
    {"username": "admin", "password": "admin", "expected": "success"}
]
Just change the usernames of the "expected": "success" ones to uppercase and make a list.
Expected: ['USER1', 'ADMIN']
'''
test_data = [
    {"username": "user1", "password": "pass123", "expected": "success"},
    {"username": "user2", "password": "wrong", "expected": "fail"},
    {"username": "", "password": "pass456", "expected": "fail"},
    {"username": "admin", "password": "admin", "expected": "success"}
]
print(list([data["username"].upper() for data in test_data if data["expected"] == "success"]))

'''
test_results = {
    "login_test": "PASSED",
    "signup_test": "FAILED",
    "payment_test": "PASSED",
    "profile_update": "FAILED",
    "logout_test": "PASSED"
}
Create a list that takes only the test names that are marked "PASSED", converts them to lowercase, and sorts them alphabetically. Expected output (sorted):
['login_test', 'logout_test', 'payment_test']
'''
test_results = {
    "login_test": "PASSED",
    "signup_test": "FAILED",
    "payment_test": "PASSED",
    "profile_update": "FAILED",
    "logout_test": "PASSED"
}
print(sorted(test.lower() for test in test_results.keys() if test_results[test] == "PASSED"))
print(sorted(test.lower() for test in test_results if test_results[test] == "PASSED"))

results = {
"test_login": {"status": "passed", "duration": 2.1},
"test_logout": {"status": "failed", "duration": 1.8},
"test_dashboard": {"status": "passed", "duration": 3.5},
"test_payment": {"status": "passed", "duration": 4.2},
"test_search": {"status": "failed", "duration": 0.9}
}
'''
Sum the durations of only the "passed" tests and print the total time + the number of tests passed.
Expected output (example format):
Number of passed tests: 3, Total time: 9.8 seconds
'''
number_of_passed_tests = 0
total_time = 0.0
for values in results.values():
    if values["status"] == "passed":
        number_of_passed_tests += 1
        total_time += values["duration"]
print(f"Number of passed tests: {number_of_passed_tests}, Total time: {total_time} seconds")

passed_durations = [info["duration"] for info in results.values() if info["status"] == "passed"]
number_of_passed_tests = len(passed_durations)
total_time = sum(passed_durations)
print(f"Number of passed tests: {number_of_passed_tests}, Total time: {total_time} seconds")

total_time = sum(info["duration"] for info in results.values() if info["status"] == "passed")
number_of_passed_tests = sum(1 for info in results.values() if info["status"] == "passed")
print(f"Number of passed tests: {number_of_passed_tests}, Total time: {total_time} seconds")

test_names = [
"TC_Login_001_Positive",
"TC_Login_002_Negative_Invalid_Password",
"TC_Signup_001",
"TC_Payment_Fail_Expired_Card",
"TC_Profile_Update_Valid_Data"
]
'''
Split each test name and discard only the part starting with "TC_", convert the remaining part to lowercase and replace the hyphen (-) with a space.
Then sort alphabetically and list them. Expected output:
['login 001 positive',
'login 002 negative invalid password',
'payment fail expired card',
'profile update valid data',
'signup 001']
'''
print(sorted([test.lower().replace("_", " ")[3:] for test in test_names]))
print(sorted(" ".join(name.split("_")[1:]).lower().strip() for name in test_names))