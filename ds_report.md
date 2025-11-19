# Trading Behavior vs Market Sentiment Analysis

**Data Science Assignment - Web3 Trading Team**

**Analysis Date:** November 19, 2025

---

## Executive Summary

This report presents a comprehensive analysis of the relationship between trader behavior and market sentiment. The analysis covers **211,224 trades** from **May 2023 to May 2025**, correlated with Bitcoin Fear & Greed Index data. Key findings reveal significant differences in trading behavior across different market sentiment conditions, with Extreme Greed periods showing the highest profitability and Fear periods showing the highest trading volume.

---

## Key Findings

### Overall Statistics
- **Total Trades Analyzed:** 211,224
- **Trades with Sentiment Data:** 211,218 (99.97% coverage)
- **Date Range:** May 1, 2023 to May 1, 2025
- **Sentiment Categories:** Extreme Fear, Fear, Neutral, Greed, Extreme Greed

### Top-Level Insights
1. **Highest Average PnL:** Extreme Greed sentiment shows the best average profitability ($67.89)
2. **Highest Trading Volume:** Fear sentiment has the most trading activity ($483M)
3. **Highest Win Rate:** Extreme Greed sentiment shows the best win rate (46.5%)
4. **Most Active Period:** Fear periods account for the most trades (61,837), followed by Greed (50,303)

---

## Detailed Analysis by Sentiment

### 1. Extreme Greed
- **Total Trades:** 39,992
- **Total Volume:** $124.5M
- **Average Trade Size:** $3,112
- **Average PnL:** $67.89
- **Win Rate:** 46.5%
- **Total PnL:** $2.72M
- **Average Absolute PnL (Risk):** $81.44

**Key Insights:**
- Highest profitability among all sentiment categories
- Best win rate (46.5%)
- Moderate risk exposure
- Suggests traders perform best during extreme bullish sentiment
- **Warning:** Potential market reversal risks during extreme conditions

### 2. Fear
- **Total Trades:** 61,837
- **Total Volume:** $483.3M
- **Average Trade Size:** $7,816
- **Average PnL:** $54.29
- **Win Rate:** 42.1%
- **Total PnL:** $3.36M
- **Average Absolute PnL (Risk):** $73.49

**Key Insights:**
- Highest trading volume across all sentiments
- Most active trading period (61,837 trades)
- Second-highest total PnL
- Suggests traders are most active during uncertain market conditions
- **Implication:** Both opportunity and risk exist during fear periods

### 3. Extreme Fear
- **Total Trades:** 21,400
- **Total Volume:** $114.5M
- **Average Trade Size:** $5,350
- **Average PnL:** $34.54
- **Win Rate:** 37.1%
- **Total PnL:** $739K
- **Average Absolute PnL (Risk):** $94.01

**Key Insights:**
- Highest risk indicator (average absolute PnL: $94.01)
- Lowest win rate (37.1%)
- Lowest total PnL
- **Critical:** Requires conservative position sizing and careful risk management

### 4. Greed
- **Total Trades:** 50,303
- **Total Volume:** $288.6M
- **Average Trade Size:** $5,737
- **Average PnL:** $42.74
- **Win Rate:** 38.5%
- **Total PnL:** $2.15M
- **Average Absolute PnL (Risk):** $84.84

**Key Insights:**
- Moderate trading activity
- Balanced risk/return profile
- Second-highest number of trades
- Moderate profitability

### 5. Neutral
- **Total Trades:** 37,686
- **Total Volume:** $180.2M
- **Average Trade Size:** $4,783
- **Average PnL:** $34.31
- **Win Rate:** 40.0%
- **Total PnL:** $1.29M
- **Average Absolute PnL (Risk):** $54.97

**Key Insights:**
- Most balanced trading behavior
- Lowest risk exposure
- Moderate returns
- Stable trading environment

---

## Profitability Analysis

### Total PnL by Sentiment
1. **Fear:** $3.36M (32.7% of total)
2. **Extreme Greed:** $2.72M (26.5% of total)
3. **Greed:** $2.15M (21.0% of total)
4. **Neutral:** $1.29M (12.6% of total)
5. **Extreme Fear:** $739K (7.2% of total)

### Average PnL Rankings
1. **Extreme Greed:** $67.89
2. **Fear:** $54.29
3. **Greed:** $42.74
4. **Neutral:** $34.31
5. **Extreme Fear:** $34.54

### Win Rate Rankings
1. **Extreme Greed:** 46.5%
2. **Neutral:** 40.0%
3. **Fear:** 42.1%
4. **Greed:** 38.5%
5. **Extreme Fear:** 37.1%

---

## Risk Analysis

### Risk Metrics by Sentiment (Average Absolute PnL)
1. **Extreme Fear:** $94.01 (Highest Risk)
2. **Greed:** $84.84
3. **Extreme Greed:** $81.44
4. **Fear:** $73.49
5. **Neutral:** $54.97 (Lowest Risk)

**Key Observation:** Extreme Fear periods show the highest risk exposure, while Neutral periods show the lowest risk.

---

## Volume Analysis

### Trading Volume by Sentiment
1. **Fear:** $483.3M (Highest)
2. **Greed:** $288.6M
3. **Neutral:** $180.2M
4. **Extreme Greed:** $124.5M
5. **Extreme Fear:** $114.5M

**Key Observation:** Fear periods drive the highest trading volume, suggesting increased market activity during uncertain times.

---

## Buy vs Sell Analysis

### Key Patterns:
- **During Extreme Greed:** SELL orders show much higher average PnL ($114.58) compared to BUY orders ($10.50)
- **During Fear:** BUY orders show higher average PnL ($63.93) compared to SELL orders ($45.05)
- **During Greed:** SELL orders show higher average PnL ($59.69) compared to BUY orders ($25.00)
- **During Neutral:** SELL orders show higher average PnL ($39.46) compared to BUY orders ($29.23)
- **During Extreme Fear:** Similar PnL for both BUY ($34.11) and SELL ($34.98)

**Implication:** During Extreme Greed, selling (taking profits) is more profitable. During Fear, buying (accumulating) shows better returns.

---

## Trading Strategy Recommendations

### 1. During Extreme Greed Periods
- **Action:** While profitability is highest, traders should be cautious of potential market reversals
- **Strategy:** Consider taking profits and reducing position sizes
- **Risk Management:** Monitor for reversal signals and be prepared to exit positions quickly
- **Key Metric:** Win rate is highest (46.5%), but market conditions may be unsustainable

### 2. During Fear Periods
- **Action:** High trading volume suggests opportunities exist, but increased volatility requires careful risk management
- **Strategy:** Focus on quality setups with proper stop-losses
- **Risk Management:** Use conservative position sizing despite high volume
- **Key Metric:** Highest volume ($483M) but moderate win rate (42.1%)

### 3. During Extreme Fear Periods
- **Action:** Highest risk period - use conservative position sizing
- **Strategy:** Wait for clear reversal signals before entering positions
- **Risk Management:** Minimize exposure, use tight stop-losses
- **Key Metric:** Highest risk ($94.01 average absolute PnL) with lowest win rate (37.1%)

### 4. During Neutral Periods
- **Action:** Balanced approach works best
- **Strategy:** Focus on consistent strategy execution without over-leveraging
- **Risk Management:** Standard position sizing appropriate
- **Key Metric:** Lowest risk ($54.97) with moderate returns

### 5. During Greed Periods
- **Action:** Moderate bullish sentiment allows for balanced risk-taking
- **Strategy:** Maintain standard position sizing and risk management protocols
- **Risk Management:** Normal risk parameters apply
- **Key Metric:** Balanced risk/return profile

---

## Hidden Trends and Signals

### 1. Sentiment-Driven Trading Patterns
- **Fear periods** show the highest trading activity, suggesting traders are more reactive during uncertain times
- **Extreme Greed** shows the best profitability, indicating momentum trading works well during strong bullish sentiment
- **Neutral periods** show the most balanced behavior, suggesting stable market conditions

### 2. Risk-Return Relationship
- There's an inverse relationship between risk (absolute PnL) and win rate
- Extreme Fear shows highest risk but lowest win rate
- Extreme Greed shows moderate risk but highest win rate
- This suggests risk management is crucial during extreme fear periods

### 3. Volume-Volatility Correlation
- Fear periods have highest volume, suggesting increased market participation during uncertainty
- This could indicate both panic selling and opportunistic buying
- The high volume during fear periods may create trading opportunities for skilled traders

### 4. Profitability Patterns
- Extreme Greed and Fear periods generate the most total PnL
- This suggests that extreme market conditions (both bullish and bearish) create the most trading opportunities
- Neutral periods show lower total PnL, suggesting fewer opportunities in stable markets

---

## Methodology

### Data Sources
1. **Bitcoin Fear & Greed Index Dataset**
   - 2,644 daily sentiment readings
   - Classifications: Extreme Fear, Fear, Neutral, Greed, Extreme Greed
   - Date range: 2018-2025

2. **Historical Trading Data from Hyperliquid**
   - 211,224 trades
   - Columns: Account, Coin, Execution Price, Size, Side, Timestamp, Closed PnL, Fee, etc.
   - Date range: May 2023 - May 2025

### Analysis Approach
1. **Data Merging:** Historical trades merged with sentiment data based on trade dates
2. **Metric Calculation:**
   - Total trades per sentiment
   - Trading volume (USD) per sentiment
   - Average and total PnL per sentiment
   - Win rates per sentiment
   - Risk metrics (absolute PnL, standard deviation, quartiles)
3. **Statistical Analysis:** Aggregated metrics by sentiment category
4. **Visualization:** 9 comprehensive charts showing different aspects of the relationship

### Key Metrics Calculated
- **Profitability:** Total PnL, Average PnL, Win Rate
- **Volume:** Total Volume USD, Average Trade Size
- **Risk:** Average Absolute PnL, Standard Deviation, Quartiles
- **Behavior:** Buy vs Sell patterns, Time-based trends

---

## Conclusion

The analysis reveals clear patterns in trading behavior across different market sentiment conditions:

1. **Extreme Greed periods** offer the best profitability but require caution for potential reversals
2. **Fear periods** show the highest trading activity, suggesting both opportunity and risk
3. **Extreme Fear periods** carry the highest risk and require conservative position sizing
4. **Neutral periods** provide the most balanced trading environment
5. **Greed periods** offer moderate opportunities with balanced risk

Understanding these patterns can help traders develop more informed strategies that adapt to market sentiment conditions. The key is to balance opportunity with risk management, especially during extreme market conditions.

### Strategic Takeaways
- **Adapt position sizing** based on sentiment (smaller during Extreme Fear, normal during Neutral)
- **Monitor sentiment shifts** as they correlate with trading behavior changes
- **Use sentiment as a filter** for trade selection and risk management
- **Be cautious during extremes** - both Extreme Fear and Extreme Greed require special attention

---

## Appendix

### Files Generated
- **CSV Files:** 7 processed data files in `csv_files/` directory
- **Visualizations:** 9 PNG charts in `outputs/` directory
- **Notebook:** `notebook_1.ipynb` with complete analysis code
- **Summary:** `analysis_summary.json` with key statistics

### Technical Details
- **Analysis Script:** `comprehensive_analysis.py`
- **Python Version:** 3.8+
- **Key Libraries:** pandas, numpy, matplotlib, seaborn
- **Analysis Date:** November 19, 2025

---

**Report Generated by:** Data Science Analysis Pipeline  
**For:** Web3 Trading Team - Data Science Assignment

