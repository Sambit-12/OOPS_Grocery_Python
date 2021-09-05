"""element which is close to its mean"""
import statistics
lst_n = [3.64, 5.2, 9.42, 9.35, 8.5, 8]


def closest(lst, mean):
    """closest number"""
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - mean))]


mean_n = statistics.mean(lst_n)
print("The number closest to mean is", closest(lst_n, mean_n))
