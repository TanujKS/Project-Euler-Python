import time
start_time = time.time()

multiples = []
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)

sum = 0
for m in multiples:
    sum += m

print(f"The sum of all multiples of 3 and 5 under 1000 is {sum}")

print(f"Program took {(time.time() - start_time)} seconds ")
