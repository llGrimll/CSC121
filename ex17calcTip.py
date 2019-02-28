# ex17calcTip
###############################################################################
#
# In-class activity 28 Feb. 2019
#
###############################################################################


def calcTip(m, t):
    return m * ((t * .01) + 1)


m = 20
t = 25
tip_amount = calcTip(20, 25)

statement = f"A ${m:.2f} meal with a {t}% tip is ${tip_amount:.2f}."

print(statement)
