import numpy as np
import matplotlib.pyplot as plt

#
# # Sampling from an exponential distribution (iid), until the sum of these holding times
# # is larger than the length of the given integer.
#


def holding_times(exp_parameter, max_time):
    """

    :param exp_parameter: Parameter of the Exponential distribution. In Python it is
                          beta = 1/lambda.
    :param max_time: Continue to sample from the Exp. distr. until the sum of these
                     holding times is larger than the length of the given interval.
    :return: Removes the last sample so that all of the events that we keep track of
             definitely occur in our time interval of interest.
    """
    x = []

    while sum(x) < max_time:
        sample = np.random.exponential(scale=1/exp_parameter, size=None)
        x.append(sample)

    return x[:-1]


def arrival_times(exp_parameter, max_time):
    """
    Generating the arrival times by summing the previous holding times. Having the arrival
    times we know at what times each event in the time interval (0, max_time) occurs.

    :param exp_parameter: Parameter of the Exponential distribution for the holding times.
    :param max_time:
    :return: Return a vector consisting of the arrival times. Where S_k is the time of the
             k-th arrival.
    """
    x = holding_times(exp_parameter, max_time)
    s = []

    for i in range(0, len(x)):
        s.append(sum(x[0:i+1]))

    return s


def hom_poisson_process(exp_parameter, max_time):
    """
    :param exp_parameter: Parameter of the Exponential distribution.
    :param max_time:
    :return: Finding the value of
    """
    arrivals = arrival_times(exp_parameter, max_time)
    poisson_process = []
    for i in range(0, max_time):
        sum_of_arrivals = 0

        for item in arrivals:
            if item <= i:
                sum_of_arrivals += item

        poisson_process.append(sum_of_arrivals)

    return poisson_process


pp = np.array(hom_poisson_process(0.6, 20))
xpoints = np.array(list(range(0, 20)))

plt.plot(xpoints, pp, linestyle='dashed')
plt.xticks(np.arange(0, 20, step=1))
plt.show()
