# Trading Behavior vs Market Sentiment Analysis

## Data Science Assignment - Web3 Trading Team

This repository contains a comprehensive analysis of the relationship between trader behavior and market sentiment using Bitcoin Fear & Greed Index and historical trading data from Hyperliquid.

## 📁 Directory Structure

```
ds_analysis/
├── notebook_1.ipynb          # Main analysis notebook
├── csv_files/                # Processed data files
│   ├── sentiment_aggregated_metrics.csv
│   ├── profitability_by_sentiment.csv
│   ├── volume_analysis_by_sentiment.csv
│   ├── risk_analysis_by_sentiment.csv
│   └── ...
├── outputs/                  # Visualizations and charts
│   ├── 1_trades_per_sentiment.png
│   ├── 2_avg_pnl_per_sentiment.png
│   ├── 3_win_rate_per_sentiment.png
│   └── ...
├── ds_report.md              # Final analysis report (Markdown format - can be converted to PDF)
├── comprehensive_analysis.py # Analysis script
└── README.md                 # This file
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Required packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - jupyter

### Installation

1. Install required packages:
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

2. Place the following CSV files in the root directory:
   - `fear_greed_index.csv` - Bitcoin Market Sentiment Dataset
   - `historical_data.csv` - Historical Trader Data from Hyperliquid

3. Run the analysis:
```bash
python comprehensive_analysis.py
```

Or open the Jupyter notebook:
```bash
jupyter notebook notebook_1.ipynb
```

## 📊 Analysis Overview

### Datasets
1. **Bitcoin Market Sentiment Dataset**
   - Columns: `timestamp`, `value`, `classification`, `date`
   - Classification: Extreme Fear, Fear, Neutral, Greed, Extreme Greed
   - 2,644 rows covering market sentiment from 2018-2025

2. **Historical Trader Data from Hyperliquid**
   - Columns: Account, Coin, Execution Price, Size Tokens, Size USD, Side, Timestamp, Closed PnL, Fee, etc.
   - 211,224 trades from 2023-2025

### Key Analyses Performed

1. **Overall Metrics by Sentiment**
   - Total trades, volume, average PnL, win rates

2. **Profitability Analysis**
   - Total and average PnL by sentiment
   - Winning vs losing trades distribution

3. **Volume Analysis**
   - Trading volume patterns across sentiment categories

4. **Risk Analysis**
   - Risk metrics including absolute PnL, standard deviation, quartiles

5. **Buy vs Sell Analysis**
   - Comparison of buy and sell behavior by sentiment

6. **Time-based Trends**
   - Monthly trends in trading behavior and sentiment

## 🔍 Key Findings

### Main Insights:

1. **Extreme Greed Periods**
   - Highest average PnL: $67.89
   - Highest win rate: 46.5%
   - Best profitability but requires caution for reversals

2. **Fear Periods**
   - Highest trading volume: $483M
   - Most trades: 61,837
   - Most active trading during uncertain times

3. **Extreme Fear Periods**
   - Highest average absolute PnL: $94.01
   - Highest risk indicator
   - Requires careful position sizing

4. **Neutral Periods**
   - Most balanced trading behavior
   - Moderate risk and returns

### Trading Strategy Implications:

- **During Extreme Greed**: Higher profitability but watch for market reversals
- **During Fear**: High trading activity suggests opportunities but with increased volatility
- **During Extreme Fear**: Highest risk - requires conservative position sizing
- **During Neutral**: Balanced approach with moderate risk/return profile

## 📈 Visualizations

The analysis includes 9 comprehensive visualizations:
1. Trades per sentiment
2. Average PnL per sentiment
3. Win rate per sentiment
4. Total volume per sentiment
5. Risk metrics per sentiment
6. PnL distribution
7. Volume time series
8. Correlation heatmap
9. Buy vs Sell comparison

All visualizations are saved in the `outputs/` directory.

## 📝 Files Generated

### CSV Files (in `csv_files/`)
- `sentiment_aggregated_metrics.csv` - Overall metrics by sentiment
- `profitability_by_sentiment.csv` - Profitability analysis
- `volume_analysis_by_sentiment.csv` - Volume analysis
- `risk_analysis_by_sentiment.csv` - Risk metrics
- `buy_sell_analysis.csv` - Buy vs Sell comparison
- `time_trends.csv` - Monthly trends
- `top_accounts_by_sentiment.csv` - Top performing accounts

### Output Files (in `outputs/`)
- 9 PNG visualizations
- `analysis_summary.json` - Summary statistics

## 🔗 Google Colab

The notebook can be uploaded to Google Colab for interactive analysis. Ensure the CSV files are uploaded to the Colab environment.

## 📧 Contact

For questions or clarifications about this analysis, please refer to the assignment instructions.

---

**Note**: This analysis was completed as part of the Data Science assignment for the Web3 Trading Team position.

