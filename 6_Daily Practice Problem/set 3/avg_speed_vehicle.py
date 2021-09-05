"""average speed of a vehicle"""
import statistics
distance = [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]
mean_n = statistics.mean(distance)
print("Average speed is ", mean_n)
