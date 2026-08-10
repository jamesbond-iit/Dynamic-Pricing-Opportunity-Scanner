# Dynamic Pricing Opportunity Scanner

## Project Overview

The Dynamic Pricing Opportunity Scanner is an end-to-end pricing analytics project that identifies products that may be underpriced, overpriced, or appropriately priced using demand, margin, competitor pricing, elasticity, and simulated revenue impact.

The project uses a synthetic transaction dataset and combines PostgreSQL, Python, regression analysis, price elasticity, revenue simulation, and an interactive Streamlit dashboard.

## Business Question

Which products should the business increase, decrease, or maintain in price, and what could be the estimated revenue impact?

## Business Objectives

1. Identify products priced materially above or below competitors.
2. Estimate the relationship between price and demand.
3. Measure price elasticity.
4. Identify products with attractive margins and pricing headroom.
5. Simulate revenue impact from price changes.
6. Rank pricing opportunities.
7. Provide an interactive decision-support dashboard.

## Dataset

The synthetic dataset contains 15,000 transactions across 120 products and 4,500 customers. Fields include product category, brand tier, channel, customer segment, base cost, listed price, competitor price, discount, units sold, revenue, gross profit, margin, price gap, and elasticity assumptions.

No real customer or company data is used.

## Methodology

### Competitive Price Gap

Price Gap % = (Listed Price - Competitor Price) / Competitor Price x 100

A negative value means the product is priced below the competitor benchmark.

### Price Elasticity

A log-log regression is used as a simple estimate of price elasticity:

ln(Units Sold) = alpha + beta ln(Price) + error

The coefficient beta represents the approximate percentage change in demand associated with a one-percent change in price, subject to the limitations of observational data.

### Pricing Opportunity Score

Products are prioritized using a combination of competitor price gap, elasticity, margin, sales volume, and simulated revenue impact.

### Revenue Scenarios

The project simulates price changes of -10%, -5%, +5%, and +10%. Expected quantity is adjusted using the elasticity relationship. These are directional planning scenarios, not guaranteed financial outcomes.

## SQL Analysis

The SQL layer includes overall KPIs, category performance, products priced below competitors, high-volume relatively inelastic products, monthly product ranking using window functions, and customer-segment pricing behavior.

Example:

```sql
SELECT category,
       SUM(units_sold) AS units,
       ROUND(SUM(revenue), 2) AS revenue,
       ROUND(SUM(gross_profit), 2) AS gross_profit,
       ROUND(AVG(margin_pct), 2) AS avg_margin_pct
FROM pricing_sales
GROUP BY category
ORDER BY revenue DESC;
```

## Dashboard

The Streamlit dashboard provides revenue, gross profit, units, margin, competitor price gap, category performance, elasticity analysis, recommended pricing actions, top product opportunities, and portfolio-level price scenarios.

Filters are available for category, channel, and customer segment.

## Run the Dashboard

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run dashboard/app.py
```

## PostgreSQL Setup

Create a database named `pricing_analytics`, run `sql/schema.sql`, import `data/pricing_sales_data.csv` into the `pricing_sales` table, and then execute `sql/analysis.sql`.

## Project Structure

```text
dynamic-pricing-opportunity-scanner/
|-- data/
|   `-- pricing_sales_data.csv
|-- sql/
|   |-- schema.sql
|   `-- analysis.sql
|-- notebooks/
|   `-- dynamic_pricing_analysis.ipynb
|-- dashboard/
|   `-- app.py
|-- docs/
|   |-- price_scenarios.csv
|   |-- product_pricing_opportunities.csv
|   `-- screenshots/
|-- analysis.py
|-- requirements.txt
|-- .gitignore
|-- LICENSE
`-- README.md
```

## Business Recommendations

### Increase price selectively

Review products with relatively inelastic demand, healthy margins, prices below competitors, and stable sales volume.

### Decrease price selectively

Review products that are materially above competitors and have highly price-sensitive demand where the expected volume response could offset the lower unit price.

### Maintain price

Maintain products where competitive positioning, margins, elasticity, and scenario analysis do not show a strong pricing advantage.

### Validate with experiments

Pricing recommendations should be tested using controlled experiments. Success should be evaluated using units, conversion, revenue, gross profit, and customer response rather than revenue alone.

## Skills Demonstrated

SQL, PostgreSQL, Python, Pandas, NumPy, Scikit-learn, regression, price elasticity, revenue simulation, competitive pricing analysis, profitability analysis, Streamlit, Plotly, window functions, and business recommendation.

## Limitations

This project uses synthetic data. Observational price-demand relationships do not automatically establish causality. A production pricing system would require richer historical data, competitor price history, inventory information, promotion history, seasonality controls, customer-level behavior, margin constraints, and controlled pricing experiments.

## Author

K. James Bond

Aspiring Data Analyst | Business Analyst

IIT Madras

GitHub: https://github.com/jamesbond-iit
