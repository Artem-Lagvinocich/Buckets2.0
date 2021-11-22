bucket3 = 0
bucket5 = 0
i = 0

while bucket5 != 4:
    i += 1
    print("What to do with buckets?\n"
          "1 - Fill the bucket\n"
          "2 - Pour from bucket3 to bucket5\n"
          "3 - Pour from bucket5 to bucket3\n"
          "4 - Pour the water from bucket3 away\n"
          "5 - Pour the water from bucket5 away\n")

    choice = int(input())
    if choice == 1:
        print("What bucket to fill, 3 or 5 liters?")
        bucket = int(input())
        if bucket == 3:
            bucket3 = 3
        if bucket == 5:
            bucket5 = 5
        if bucket != 3 and bucket != 5:
            print("Try again")

    if choice == 2:
        if bucket3 == 3 and bucket5 == 3:
            bucket3 = bucket5 + bucket3 - 5
            bucket5 = 5
        else:
            bucket5 = bucket3 + bucket5
            bucket3 = 0

    if choice == 3:
        bucket5 -= 3
        bucket3 += 3
        if bucket3 > 3:
            bucket5 = bucket5 - (3 - bucket3)
            bucket3 = 3
        if bucket5 < 0:
            bucket3 += bucket5
            bucket5 = 0

    if choice == 4:
        bucket3 = 0

    if choice == 5:
        bucket5 = 0

    print("Bucket3 is", bucket3, "litre full\n"
          "Bucket5 is", bucket5, "litre full\n")
    continue

print("Good job, you did this! You make", i, "steps")
