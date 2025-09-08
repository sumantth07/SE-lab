# WEATHER MODELING - Different Development Modes

# Coefficients for quadratic model
a = -0.2
b = 1.5
c = 24

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c

# ===== WATERFALL MODE =====
print("=== WATERFALL MODE ===")
# Plan -> Develop -> Test -> Deliver (one cycle)
for hour in range(0, 25, 6):  # every 6 hours
    temp = quadratic_weather_model(hour)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")

# ===== ITERATIVE MODE =====
print("\n=== ITERATIVE MODE ===")
# Small updates in multiple cycles
for iteration in range(1, 4):
    print(f"Iteration {iteration}:")
    for hour in range(0, 25, 12):  # every 12 hours
        temp = quadratic_weather_model(hour)
        print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
    print("---")

# ===== AGILE MODE =====
print("\n=== AGILE MODE ===")
# Quick sprints, immediate feedback
times_to_check = [0, 6, 12, 18, 24]
for sprint in range(1, 3):
    print(f"Sprint {sprint}:")
    for hour in times_to_check:
        temp = quadratic_weather_model(hour)
        print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
    print("Feedback incorporated.\n")
