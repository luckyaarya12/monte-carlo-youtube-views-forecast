# Monte Carlo Simulation of YouTube Daily Views

## Project Overview
This project uses **Monte Carlo simulation** to estimate the expected range and uncertainty of **average daily YouTube views** over the next 30 days. By simulating multiple possible future outcomes based on historical data, the project helps understand variability in audience engagement and supports data-driven content planning.

---

## Dataset
- Daily YouTube views collected over a **60-day period**.  
- Data is numeric, time-indexed, and contains no missing values.  
- Values like "1.3K" are converted to numeric format for analysis.

---

## Research Question
> Based on historical YouTube daily views, what is the expected range of average daily views for the next 30 days, and how uncertain is this forecast?

---

## Methodology
1. Cleaned the dataset and converted any non-numeric view counts to numbers.  
2. Calculated **historical mean** and **standard deviation** of daily views.  
3. Ran **1,000 Monte Carlo simulations** of daily views over a 30-day horizon using a normal distribution.  
4. Calculated statistics on simulation outcomes: mean, median, standard deviation, and percentiles.  
5. Visualized results using:  
   - Histogram of simulated average daily views  
   - Sample simulation runs showing possible daily view trajectories  

---

## Statistical Output
| Metric                     | Value       |
|-----------------------------|------------|
| Historical Mean Views       | 422.72     |
| Historical Std Dev          | 369.34     |
| Simulated Mean Views        | 423.70     |
| Simulated Median Views      | 423.52     |
| Simulated Std Dev           | 64.98      |
| 10th Percentile             | 340.78     |
| 90th Percentile             | 505.52     |

---

## Results & Insights
- **Expected average daily views:** ~424  
- **Variability:** Standard deviation of ~65 shows natural fluctuations in engagement.  
- **Histogram:** Confirms distribution of possible average views.  
- **Line plots:** Illustrate multiple possible daily view trajectories.  
- **Percentile range (10th–90th):** 341–506, indicating moderate uncertainty.  
- This analysis helps **guide content planning** and estimate expected engagement over the next month.

---

## Assumptions
- Daily views follow an approximately **normal distribution**.  
- Historical daily view patterns are representative of near-future performance.  
- External events like viral spikes or algorithm changes are **not explicitly modeled**.

---

## Limitations
- Normal distribution may underrepresent extreme viral spikes.  
- Does not account for time-based trends or seasonality.  
- Analysis limited to a 60-day historical dataset.

---

## Files Included
- `youtube_views_60days.xlsx` – Historical dataset  
- `monte_carlo_youtube_views.py` – Python code for simulation  
- `Monte Carlo Forecast – Average Daily Views (Next 30 Days).png` – Forecast histogram  
- `Sample Monte Carlo Simulation Runs.png` – Sample simulation runs  
- `.gitignore` – Python ignore file

