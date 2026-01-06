# YouTube Performance Analysis Report

## 1. Introduction
Understanding future uncertainty in digital engagement is essential for data-driven decision making. Rather than relying on single-point forecasts, probabilistic approaches allow analysts to estimate a range of possible outcomes. This study applies a Monte Carlo simulation to historical YouTube daily view data to estimate the expected range and uncertainty of average daily views over the next 30 days.

## 2. Dataset Description
The dataset consists of daily YouTube view counts collected over a period of 60 days. The data is numerical, time-indexed, and contains no missing values. Historical daily views were used as the basis for estimating statistical parameters required for the Monte Carlo simulation.

## 3. Research Questions
Given historical YouTube daily view data, what is the expected range of average daily views over the next 30 days, and how uncertain is this forecast?

## 4. Methodology
Historical daily views were summarized using descriptive statistics, including mean and standard deviation. A Monte Carlo simulation with 1,000 iterations was conducted to model possible future average daily views over a 30-day horizon, assuming a probabilistic distribution of daily engagement.

## 5. Statistical Output
- Historical Mean Views: 422.72  
- Historical Standard Deviation: 369.34  
- Simulated Mean Views: 423.70  
- Simulated Standard Deviation: 64.98  
- 10th Percentile: 340.78  
- 90th Percentile: 505.52  

## 6. Statistical Results
The Monte Carlo simulation estimates an expected average daily view count of approximately 424 views over the next 30 days. Approximately 80% of simulated outcomes lie between 341 and 506 views, indicating moderate uncertainty in future engagement levels. The observed variability reflects natural fluctuations in daily audience behavior rather than deterministic trends.

## 7. Assumptions
- Historical daily view patterns are representative of near-future performance.
- Daily views follow an approximately normal distribution.
- External shocks such as viral events or algorithm changes are not explicitly modeled.

## 8. Limitations
- The normal distribution assumption may underrepresent extreme viral spikes.
- The simulation does not account for time-based trends or seasonality.
- Analysis is limited to a 60-day historical dataset.

## 9. Implications
The results provide a probabilistic range of expected engagement rather than a single-point prediction. This can support content planning, expectation setting, and performance benchmarking by accounting for uncertainty in daily view behavior.

## 10. Conclusion
This analysis used Monte Carlo simulation to estimate the expected range of average daily YouTube views over a 30-day horizon. The results indicate a mean expected engagement of approximately 424 views, with most outcomes falling within a defined probabilistic range. While the simulation does not predict exact future values, it effectively captures uncertainty in audience engagement and provides useful insights for short-term planning and performance evaluation.
