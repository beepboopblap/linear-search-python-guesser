import time

inp =  int(input("Type a number from 1-100: "))
guesses = int()

start = time.time()

for i in range(1,100):
    if i == inp:
        print("Found in", int(guesses), "guesses")
        end = time.time()
        time_took = end - start
        time_took = float(time_took)
        print("Time Took", time_took)
    else:
        guesses += 1
