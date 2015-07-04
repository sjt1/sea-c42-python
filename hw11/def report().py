
donor_list = [['Spencer Tower', 20, 5, 10], ['Bill Gates', 100, 1000, 30],
              ['Incredible Hulk', 20, 15, 70], ['Gandalf', 1, 400, 4],
              ['Smeagle', 10, 40, 50]]


def report():
    print('Name      |    Total   |    #   |    Average')
    for donor in donor_list:
        x = 0
        for i in donor[1:]:
            x = x + i
        print("%s   |   %s   |   %s   |     %s" % (donor[0], x, len(donor[1:], (x / len(donor[1:])))



print(report())
    