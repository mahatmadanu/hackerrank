def libraryFine(d1, m1, y1, d2, m2, y2):
    # Complete this function
    fine = 0
    diffYear = y1-y2
    diffMonth = m1-m2
    diffDate = d1-d2
    if diffYear > 0:
        fine = 10000
    elif diffMonth > 0 and diffYear == 0:
        fine = 500 * diffMonth
    elif diffDate > 0 and diffMonth == 0 and diffYear == 0:
        fine = 15 * diffDate
    else:
        fine = 0
    return fine