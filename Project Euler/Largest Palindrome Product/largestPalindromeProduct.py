import time
start_time = time.time()

palindrome = (0, 0, 0)
for i in range(100, 999):
    for e in range(100, 999):
        num = i * e
        res = str(num) == str(num)[::-1]
        if res:
            if num > palindrome[0]:
                palindrome = (num, i, e)

print(f"The largest palindrome product of two three-digit numbers is {palindrome[0]} ({palindrome[1]} * {palindrome[2]})")
    
print(f"Program took {(time.time() - start_time)} seconds ")
