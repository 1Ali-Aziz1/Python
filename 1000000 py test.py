import time

currentTime = time.time()
oneMillion = 1000000
to_a_milloin = 0

while to_a_milloin < oneMillion:
    print(to_a_milloin)
    to_a_milloin = to_a_milloin + 1

after_test_time = currentTime - time.time()
print(currentTime)
