"""
Comprehensive Data Science Analysis: Trading Behavior vs Market Sentiment
This script performs a complete analysis of trader behavior in relation to market sentiment.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
from datetime import datetime
import json

warnings.filterwarnings('ignore')

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Paths
BASE_DIR = Path(__file__).parent.parent / 'primetrade.ai'
OUTPUT_DIR = Path(__file__).parent / 'outputs'
CSV_DIR = Path(__file__).parent / 'csv_files'
OUTPUT_DIR.mkdir(exist_ok=True)
CSV_DIR.mkdir(exist_ok=True)

print("Loading datasets...")

# Load datasets
fear_greed = pd.read_csv(BASE_DIR / 'fear_greed_index.csv')
historical_data = pd.read_csv(BASE_DIR / 'historical_data.csv', low_memory=False)

# Clean column names
historical_data.columns = historical_data.columns.str.strip()
fear_greed.columns = fear_greed.columns.str.strip()

print(f"Fear & Greed Index: {len(fear_greed)} rows")
print(f"Historical Trading Data: {len(historical_data)} rows")

# Data preprocessing
print("\nPreprocessing data...")

# Process fear & greed data
fear_greed['date'] = pd.to_datetime(fear_greed['date'], errors='coerce').dt.date
fear_greed = fear_greed.dropna(subset=['date', 'classification'])

# Process historical data
if 'Timestamp IST' in historical_data.columns:
    historical_data['ts'] = pd.to_datetime(historical_data['Timestamp IST'], dayfirst=True, errors='coerce')
elif 'Timestamp' in historical_data.columns:
    historical_data['ts'] = pd.to_datetime(historical_data['Timestamp'], errors='coerce')
else:
    historical_data['ts'] = pd.NaT

historical_data['date'] = historical_data['ts'].dt.date

# Convert numeric columns
numeric_cols = ['Closed PnL', 'Size USD', 'Execution Price', 'Fee', 'Size Tokens']
for col in numeric_cols:
    if col in historical_data.columns:
        historical_data[col] = pd.to_numeric(historical_data[col], errors='coerce')

# Merge datasets
print("Merging datasets...")
merged = historical_data.merge(
    fear_greed[['date', 'classification', 'value']], 
    on='date', 
    how='left'
)

print(f"Merged dataset: {len(merged)} rows")
print(f"Rows with sentiment: {merged['classification'].notna().sum()}")

# Create derived metrics
merged['win'] = merged['Closed PnL'] > 0
merged['loss'] = merged['Closed PnL'] < 0
merged['is_buy'] = merged['Side'].str.upper() == 'BUY' if 'Side' in merged.columns else False
merged['is_sell'] = merged['Side'].str.upper() == 'SELL' if 'Side' in merged.columns else False

# Calculate risk metrics (using absolute PnL as proxy for risk)
merged['abs_pnl'] = merged['Closed PnL'].abs()
merged['risk_reward_ratio'] = np.where(
    merged['Closed PnL'] != 0,
    merged['abs_pnl'] / merged['Size USD'].abs(),
    np.nan
)

# Analysis 1: Overall metrics by sentiment
print("\n=== Analysis 1: Overall Metrics by Sentiment ===")
sentiment_agg = merged.groupby('classification').agg({
    'Account': 'count',
    'Size USD': ['sum', 'mean', 'std'],
    'Closed PnL': ['sum', 'mean', 'std', 'median'],
    'win': 'mean',
    'abs_pnl': 'mean',
    'Fee': 'sum'
}).round(2)

sentiment_agg.columns = [
    'total_trades', 'total_volume_usd', 'avg_trade_size_usd', 'std_trade_size',
    'total_pnl', 'avg_pnl', 'std_pnl', 'median_pnl', 'win_rate', 'avg_abs_pnl', 'total_fees'
]

sentiment_agg = sentiment_agg.reset_index()
sentiment_agg = sentiment_agg.sort_values('total_trades', ascending=False)
print(sentiment_agg)

sentiment_agg.to_csv(CSV_DIR / 'sentiment_aggregated_metrics.csv', index=False)

# Analysis 2: Profitability analysis
print("\n=== Analysis 2: Profitability Analysis ===")
profitability = merged.groupby('classification').agg({
    'Closed PnL': ['sum', 'mean', 'median', lambda x: (x > 0).sum(), lambda x: (x < 0).sum()],
    'win': 'sum',
    'loss': 'sum'
}).round(2)

profitability.columns = ['total_pnl', 'avg_pnl', 'median_pnl', 'winning_trades', 'losing_trades', 'wins', 'losses']
profitability = profitability.reset_index()
profitability['profit_margin'] = (profitability['total_pnl'] / profitability['total_pnl'].abs().sum() * 100).round(2)
print(profitability)

profitability.to_csv(CSV_DIR / 'profitability_by_sentiment.csv', index=False)

# Analysis 3: Volume analysis
print("\n=== Analysis 3: Volume Analysis ===")
volume_analysis = merged.groupby('classification').agg({
    'Size USD': ['sum', 'mean', 'median', 'count'],
    'Size Tokens': ['sum', 'mean'] if 'Size Tokens' in merged.columns else []
}).round(2)

if 'Size Tokens' in merged.columns:
    volume_analysis.columns = ['total_volume_usd', 'avg_volume_usd', 'median_volume_usd', 'trade_count', 
                               'total_tokens', 'avg_tokens']
else:
    volume_analysis.columns = ['total_volume_usd', 'avg_volume_usd', 'median_volume_usd', 'trade_count']

volume_analysis = volume_analysis.reset_index()
print(volume_analysis)

volume_analysis.to_csv(CSV_DIR / 'volume_analysis_by_sentiment.csv', index=False)

# Analysis 4: Risk analysis
print("\n=== Analysis 4: Risk Analysis ===")
risk_analysis = merged.groupby('classification').agg({
    'abs_pnl': ['mean', 'median', 'std'],
    'risk_reward_ratio': ['mean', 'median'],
    'Closed PnL': ['std', lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)]
}).round(2)

risk_analysis.columns = ['avg_abs_pnl', 'median_abs_pnl', 'std_abs_pnl', 
                        'avg_risk_reward', 'median_risk_reward',
                        'pnl_std', 'pnl_q25', 'pnl_q75']
risk_analysis = risk_analysis.reset_index()
print(risk_analysis)

risk_analysis.to_csv(CSV_DIR / 'risk_analysis_by_sentiment.csv', index=False)

# Analysis 5: Buy vs Sell behavior
print("\n=== Analysis 5: Buy vs Sell Analysis ===")
if 'is_buy' in merged.columns:
    buy_sell_analysis = merged.groupby(['classification', 'is_buy']).agg({
        'Account': 'count',
        'Size USD': 'sum',
        'Closed PnL': ['sum', 'mean']
    }).round(2)
    
    buy_sell_analysis.columns = ['trade_count', 'total_volume', 'total_pnl', 'avg_pnl']
    buy_sell_analysis = buy_sell_analysis.reset_index()
    buy_sell_analysis['side'] = buy_sell_analysis['is_buy'].map({True: 'BUY', False: 'SELL'})
    print(buy_sell_analysis)
    
    buy_sell_analysis.to_csv(CSV_DIR / 'buy_sell_analysis.csv', index=False)

# Analysis 6: Time-based trends
print("\n=== Analysis 6: Time-based Trends ===")
merged['year_month'] = merged['ts'].dt.to_period('M')
time_trends = merged.groupby(['year_month', 'classification']).agg({
    'Account': 'count',
    'Size USD': 'sum',
    'Closed PnL': 'sum'
}).round(2)

time_trends.columns = ['trade_count', 'volume', 'pnl']
time_trends = time_trends.reset_index()
time_trends.to_csv(CSV_DIR / 'time_trends.csv', index=False)

# Analysis 7: Top performing accounts by sentiment
print("\n=== Analysis 7: Top Accounts by Sentiment ===")
account_performance = merged.groupby(['classification', 'Account']).agg({
    'Closed PnL': 'sum',
    'Account': 'count',
    'Size USD': 'sum'
}).round(2)

account_performance.columns = ['total_pnl', 'trade_count', 'total_volume']
account_performance = account_performance.reset_index()

top_accounts = account_performance.groupby('classification').apply(
    lambda x: x.nlargest(5, 'total_pnl')
).reset_index(drop=True)

top_accounts.to_csv(CSV_DIR / 'top_accounts_by_sentiment.csv', index=False)

# ========== VISUALIZATIONS ==========
print("\n=== Creating Visualizations ===")

# 1. Trades per sentiment
plt.figure(figsize=(10, 6))
sns.barplot(data=sentiment_agg, x='classification', y='total_trades', palette='viridis')
plt.title('Total Trades by Market Sentiment', fontsize=14, fontweight='bold')
plt.xlabel('Market Sentiment', fontsize=12)
plt.ylabel('Number of Trades', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / '1_trades_per_sentiment.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Average PnL per sentiment
plt.figure(figsize=(10, 6))
sns.barplot(data=sentiment_agg, x='classification', y='avg_pnl', palette='coolwarm')
plt.title('Average Closed PnL by Market Sentiment', fontsize=14, fontweight='bold')
plt.xlabel('Market Sentiment', fontsize=12)
plt.ylabel('Average PnL (USD)', fontsize=12)
plt.xticks(rotation=45)
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / '2_avg_pnl_per_sentiment.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Win rate per sentiment
plt.figure(figsize=(10, 6))
sns.barplot(data=sentiment_agg, x='classification', y='win_rate', palette='RdYlGn')
plt.title('Win Rate by Market Sentiment', fontsize=14, fontweight='bold')
plt.xlabel('Market Sentiment', fontsize=12)
plt.ylabel('Win Rate', fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / '3_win_rate_per_sentiment.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Total volume per sentiment
plt.figure(figsize=(10, 6))
sns.barplot(data=sentiment_agg, x='classification', y='total_volume_usd', palette='plasma')
plt.title('Total Trading Volume by Market Sentiment', fontsize=14, fontweight='bold')
plt.xlabel('Market Sentiment', fontsize=12)
plt.ylabel('Total Volume (USD)', fontsize=12)
plt.yscale('log')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / '4_total_volume_per_sentiment.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Risk metrics
plt.figure(figsize=(10, 6))
sns.barplot(data=risk_analysis, x='classification', y='avg_abs_pnl', palette='magma')
plt.title('Average Absolute PnL (Risk Proxy) by Market Sentiment', fontsize=14, fontweight='bold')
plt.xlabel('Market Sentiment', fontsize=12)
plt.ylabel('Average Absolute PnL (USD)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / '5_risk_metrics_per_sentiment.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. PnL distribution by sentiment
plt.figure(figsize=(12, 6))
sentiment_order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
for sent in sentiment_order:
    if sent in merged['classification'].values:
        data = merged[merged['classification'] == sent]['Closed PnL'].dropna()
        plt.hist(data, alpha=0.6, label=sent, bins=50)
plt.title('PnL Distribution by Market Sentiment', fontsize=14, fontweight='bold')
plt.xlabel('Closed PnL (USD)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.xlim(-1000, 1000)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / '6_pnl_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. Time series of sentiment and trading volume
if 'year_month' in merged.columns:
    monthly_volume = merged.groupby(['year_month', 'classification'])['Size USD'].sum().reset_index()
    monthly_volume['year_month_str'] = monthly_volume['year_month'].astype(str)
    
    plt.figure(figsize=(14, 6))
    for sent in sentiment_order:
        if sent in monthly_volume['classification'].values:
            data = monthly_volume[monthly_volume['classification'] == sent]
            plt.plot(data['year_month_str'], data['Size USD'], marker='o', label=sent, linewidth=2)
    plt.title('Monthly Trading Volume by Market Sentiment Over Time', fontsize=14, fontweight='bold')
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Trading Volume (USD)', fontsize=12)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '7_volume_timeseries.png', dpi=300, bbox_inches='tight')
    plt.close()

# 8. Correlation heatmap
correlation_data = sentiment_agg[['total_trades', 'total_volume_usd', 'avg_pnl', 'win_rate', 'avg_abs_pnl']]
correlation_data.index = sentiment_agg['classification']
corr_matrix = correlation_data.T.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, square=True)
plt.title('Correlation Matrix: Trading Metrics by Sentiment', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(OUTPUT_DIR / '8_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 9. Buy vs Sell comparison
if 'is_buy' in merged.columns:
    buy_sell_pnl = merged.groupby(['classification', 'is_buy'])['Closed PnL'].mean().reset_index()
    buy_sell_pnl['side'] = buy_sell_pnl['is_buy'].map({True: 'BUY', False: 'SELL'})
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=buy_sell_pnl, x='classification', y='Closed PnL', hue='side', palette='Set2')
    plt.title('Average PnL: Buy vs Sell by Market Sentiment', fontsize=14, fontweight='bold')
    plt.xlabel('Market Sentiment', fontsize=12)
    plt.ylabel('Average PnL (USD)', fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title='Side')
    plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '9_buy_vs_sell_pnl.png', dpi=300, bbox_inches='tight')
    plt.close()

print(f"\n=== Analysis Complete ===")
print(f"Outputs saved to: {OUTPUT_DIR}")
print(f"CSV files saved to: {CSV_DIR}")

# Generate summary statistics
summary = {
    'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'total_trades': int(len(merged)),
    'trades_with_sentiment': int(merged['classification'].notna().sum()),
    'date_range': {
        'start': str(merged['date'].min()),
        'end': str(merged['date'].max())
    },
    'sentiment_distribution': {str(k): int(v) for k, v in merged['classification'].value_counts().to_dict().items()},
    'key_insights': {
        'highest_volume_sentiment': str(sentiment_agg.loc[sentiment_agg['total_volume_usd'].idxmax(), 'classification']),
        'highest_avg_pnl_sentiment': str(sentiment_agg.loc[sentiment_agg['avg_pnl'].idxmax(), 'classification']),
        'highest_win_rate_sentiment': str(sentiment_agg.loc[sentiment_agg['win_rate'].idxmax(), 'classification'])
    }
}

with open(OUTPUT_DIR / 'analysis_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

print("\nSummary statistics saved to analysis_summary.json")

