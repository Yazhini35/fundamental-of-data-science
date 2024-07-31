import numpy as np
fuel_efficiency = np.array([25, 30, 22, 35, 28, 32])
average_fuel_efficiency = np.mean(fuel_efficiency)
print("Average fuel efficiency:", average_fuel_efficiency)
efficiency_model_1 = fuel_efficiency[1]
efficiency_model_2 = fuel_efficiency[4]
percentage_improvement = ((efficiency_model_2 - efficiency_model_1) / efficiency_model_1) * 100
print("Percentage improvement in fuel efficiency between model 2 and model 5:", percentage_improvement)
