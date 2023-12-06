def sol(tm, dst, task):
    number_of_ways = 1

    for t,d in zip(tm,dst):
        sum = 0
        for speed in range(0,t):
            time_left = t-speed
            if time_left * speed > d:
                sum += 1
        number_of_ways *= sum

    print(f"Solution {task}", number_of_ways)


if __name__ == "__main__":
    times = [45, 98, 83, 73]
    distances = [295, 1734, 1278, 1210]

    time = [45988373]
    distance = [295173412781210]

    sol(times,distances, 1)
    sol(time,distance, 2)
