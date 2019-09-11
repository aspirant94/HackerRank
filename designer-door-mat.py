height = int((input().split())[0])
width = height * 3
half = int((height - 1) / 2)

# Top half
for line in range(1, half + 1):
    non_dashes = ((line * 2) - 1)
    dashes = int((width - (non_dashes * 3)) / 2)

    print("%s%s%s" % ("-" * dashes, ".|." * non_dashes, "-" * dashes))

# Middle line
print("%s%s%s" % (
    "-" * (int(width / 2) - 3),
    "WELCOME",
    "-" * (int(width / 2) - 3)
))

# Lower half
for line in range(half, 0, -1):
    non_dashes = ((line * 2) - 1)
    dashes = int((width - (non_dashes * 3)) / 2)

    print("%s%s%s" % ("-" * dashes, ".|." * non_dashes, "-" * dashes))