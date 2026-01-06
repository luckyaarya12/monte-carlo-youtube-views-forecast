# =========================
# PROJECT-MONTE CARLO SIMULATION OF YOUTUBE DAILY VIEWS
# =========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('youtube_views_60days.xlsx')
views = data['Views']

# Convert K-values to numbers
def convert_to_number(x):
    try:
        if pd.isna(x):
            return np.nan
        x = str(x).replace('K', 'e3').replace(',', '').strip()  # 1.3K -> 1.3e3
        return float(eval(x))
    except:
        return np.nan

views = views.apply(convert_to_number)
views = views.dropna()  # drop invalid rows

print("First 5 cleaned views:\n", views.head())

# Calculate mean and std
mean_views = views.mean()
std_views = views.std()

print("\nHistorical Stats:")
print("Mean Views:", mean_views)
print("Standard Deviation:", std_views)

# Monte Carlo Simulation
simulations = 1000
forecast_days = 30
simulation_results = []

for i in range(simulations):
    simulated_daily_views = np.random.normal(mean_views, std_views, forecast_days)
    simulation_results.append(np.mean(simulated_daily_views))

simulation_results = np.array(simulation_results)

# Simulation stats
mean_sim = np.mean(simulation_results)
median_sim = np.median(simulation_results)
std_sim = np.std(simulation_results)
p10, p90 = np.percentile(simulation_results, [10, 90])

print("\nMonte Carlo Simulation Stats:")
print("Simulated Mean:", mean_sim)
print("Simulated Median:", median_sim)
print("Simulated Std Dev:", std_sim)
print(f"10th percentile: {p10:.2f}, 90th percentile: {p90:.2f}")

# Histogram
plt.figure(figsize=(10,6))
sns.histplot(simulation_results, bins=30, kde=True, color='skyblue')
plt.title("Monte Carlo Simulation: Avg Daily Views (Next 30 Days)")
plt.xlabel("Average Views")
plt.ylabel("Frequency")
plt.grid(True, alpha=0.3)
plt.show()

# Sample simulation runs
plt.figure(figsize=(10,6))
for i in range(10):
    plt.plot(np.arange(1, forecast_days+1),
             np.random.normal(mean_views, std_views, forecast_days),
             alpha=0.7)
plt.title("Sample Monte Carlo Simulation Runs (Next 30 Days)")
plt.xlabel("Day")
plt.ylabel("Views")
plt.grid(True, alpha=0.3)
plt.show()

# Insights
print("\nSample Insights to Include in Report:")
print(f"1. Based on 60 days of historical views, expected average daily views for the next 30 days is around {mean_sim:.2f}.")
print(f"2. The standard deviation of {std_sim:.2f} shows natural variability in daily engagement.")
print("3. Histogram shows distribution of possible average views, confirming expected variability.")
print("4. Line plots illustrate multiple possible daily view trajectories, helping forecast high and low periods.")
print("5. 10th and 90th percentiles ({p10:.2f}, {p90:.2f}) provide a range for likely engagement.")
print("6. This simulation can guide content planning and estimate expected engagement for the upcoming month.")
