import random
import matplotlib.pyplot as plt
import numpy as np, scipy.stats as st



#1 - represents Heads
#2 - represents Tails
class Game:

    def Simulate(self):

        reward = -250
        twoBack = 0
        oneBack = 0
        for i in range(1,21):

            outcome = random.randint(1,2)

            if twoBack == 2 and oneBack == 2 and outcome == 1:
                reward = reward + 100

            twoBack = oneBack
            oneBack = outcome

        return reward

g = Game()

sumOfRewards = 0
results = []
numberOfLosses = 0
for i in range(0, 1000):
    rew = g.Simulate()
    results.append(rew)

    if rew < 0:
        numberOfLosses = numberOfLosses + 1

    sumOfRewards = sumOfRewards + rew

print("Average of 1000 realizations is {}".format( sumOfRewards/1000))
print("Probability of loss is {}".format( numberOfLosses/1000))
print("The minimum expected reward is -250")
print("The maximum expected reward is 350")

conf_int = st.t.interval(0.95, len(results)-1, loc=np.mean(results), scale=st.sem(results))

print("The 95% t-based confidence intervals for the expected reward is ", conf_int )



bin_edges = [-250, -150, -50, 50, 150, 250, 350]
plt.hist(results, bins=bin_edges, edgecolor='b')
plt.xlabel("Game Outcome")
plt.ylabel("Frequency")
plt.title("Fair Coin Game Outcome Histogram")
plt.show()

# Question 2: The 95% Confidence Interval tells us our end result will fall within the bounds of the interval 95% of the time, or if we played the game 1000 times
# our result would be observed in the interval 950 times out of 1000.
# Question 3: The gambler would want a projection interval to be able to bet with reduced uncertainty on the next realization of the game falling within
# an interval with a certain probability in a small number of realizations, for example to place a winning bet on the 10th realization after gathering data on the previous 9 realizations.
# The casino owner need only be concerned with the confidence interval to understand how much the casino will win or lose, the mean of a large number
# of realizations.