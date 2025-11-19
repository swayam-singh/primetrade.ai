"""
Generate PDF Report for Trading Behavior vs Market Sentiment Analysis
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from pathlib import Path
import json

# Paths
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / 'outputs'
CSV_DIR = BASE_DIR / 'csv_files'
REPORT_PATH = BASE_DIR / 'ds_report.pdf'

# Load summary data
with open(OUTPUT_DIR / 'analysis_summary.json', 'r') as f:
    summary = json.load(f)

# Load aggregated metrics
import pandas as pd
sentiment_agg = pd.read_csv(CSV_DIR / 'sentiment_aggregated_metrics.csv')
profitability = pd.read_csv(CSV_DIR / 'profitability_by_sentiment.csv')
risk_analysis = pd.read_csv(CSV_DIR / 'risk_analysis_by_sentiment.csv')

# Create PDF
doc = SimpleDocTemplate(str(REPORT_PATH), pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)

# Container for the 'Flowable' objects
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=30,
    alignment=TA_CENTER
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#2c3e50'),
    spaceAfter=12,
    spaceBefore=12
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=11,
    leading=14,
    alignment=TA_JUSTIFY
)

# Title
elements.append(Paragraph("Trading Behavior vs Market Sentiment Analysis", title_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("Data Science Assignment - Web3 Trading Team", styles['Heading2']))
elements.append(Spacer(1, 0.3*inch))

# Executive Summary
elements.append(Paragraph("Executive Summary", heading_style))
elements.append(Paragraph(
    f"This report presents a comprehensive analysis of the relationship between trader behavior and market sentiment. "
    f"The analysis covers {summary['total_trades']:,} trades from {summary['date_range']['start']} to {summary['date_range']['end']}, "
    f"correlated with Bitcoin Fear & Greed Index data. Key findings reveal significant differences in trading behavior "
    f"across different market sentiment conditions, with Extreme Greed periods showing the highest profitability and "
    f"Fear periods showing the highest trading volume.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# Key Findings
elements.append(Paragraph("Key Findings", heading_style))

findings = [
    f"<b>Highest Average PnL:</b> {summary['key_insights']['highest_avg_pnl_sentiment']} sentiment shows the best average profitability",
    f"<b>Highest Trading Volume:</b> {summary['key_insights']['highest_volume_sentiment']} sentiment has the most trading activity",
    f"<b>Highest Win Rate:</b> {summary['key_insights']['highest_win_rate_sentiment']} sentiment shows the best win rate",
    f"<b>Sentiment Distribution:</b> Fear periods account for the most trades ({summary['sentiment_distribution']['Fear']:,}), "
    f"followed by Greed ({summary['sentiment_distribution']['Greed']:,})"
]

for finding in findings:
    elements.append(Paragraph(f"• {finding}", body_style))
    elements.append(Spacer(1, 0.1*inch))

elements.append(Spacer(1, 0.2*inch))

# Detailed Analysis
elements.append(Paragraph("Detailed Analysis by Sentiment", heading_style))

# Create table from aggregated metrics
table_data = [['Sentiment', 'Trades', 'Total Volume (USD)', 'Avg PnL (USD)', 'Win Rate']]
for _, row in sentiment_agg.iterrows():
    table_data.append([
        row['classification'],
        f"{int(row['total_trades']):,}",
        f"${row['total_volume_usd']:,.0f}",
        f"${row['avg_pnl']:.2f}",
        f"{row['win_rate']:.1%}"
    ])

table = Table(table_data, colWidths=[1.5*inch, 1*inch, 1.5*inch, 1*inch, 1*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 9),
]))

elements.append(table)
elements.append(Spacer(1, 0.3*inch))

# Insights by Sentiment
elements.append(Paragraph("Insights by Sentiment Category", heading_style))

insights_text = """
<b>Extreme Greed:</b> Shows the highest average PnL ($67.89) and win rate (46.5%), indicating that traders perform best during extreme bullish sentiment. However, this also suggests potential market reversal risks.

<b>Fear:</b> Has the highest trading volume ($483M) and most trades (61,837), suggesting traders are most active during uncertain market conditions. This could indicate both opportunity and risk.

<b>Extreme Fear:</b> Shows the highest average absolute PnL ($94.01), indicating higher risk exposure. Traders should exercise caution and use conservative position sizing during these periods.

<b>Greed:</b> Moderate trading activity with balanced risk/return profile. Average PnL of $42.74 with 38.5% win rate.

<b>Neutral:</b> Most balanced trading behavior with moderate risk and returns. Average PnL of $34.31 with 40% win rate.
"""

elements.append(Paragraph(insights_text, body_style))
elements.append(Spacer(1, 0.3*inch))

# Trading Strategy Recommendations
elements.append(Paragraph("Trading Strategy Recommendations", heading_style))

recommendations = [
    "<b>During Extreme Greed:</b> While profitability is highest, traders should be cautious of potential market reversals. Consider taking profits and reducing position sizes.",
    "<b>During Fear:</b> High trading volume suggests opportunities exist, but increased volatility requires careful risk management. Focus on quality setups with proper stop-losses.",
    "<b>During Extreme Fear:</b> Highest risk period - use conservative position sizing and wait for clear reversal signals before entering positions.",
    "<b>During Neutral:</b> Balanced approach works best. Focus on consistent strategy execution without over-leveraging.",
    "<b>During Greed:</b> Moderate bullish sentiment allows for balanced risk-taking. Maintain standard position sizing and risk management protocols."
]

for rec in recommendations:
    elements.append(Paragraph(f"• {rec}", body_style))
    elements.append(Spacer(1, 0.1*inch))

elements.append(Spacer(1, 0.3*inch))

# Methodology
elements.append(Paragraph("Methodology", heading_style))
elements.append(Paragraph(
    "The analysis merged historical trading data from Hyperliquid with Bitcoin Fear & Greed Index data based on trade dates. "
    "Key metrics calculated include: total trades, trading volume, average PnL, win rates, and risk metrics (absolute PnL, standard deviation). "
    "The analysis covers all trades from May 2023 to May 2025, with sentiment classifications: Extreme Fear, Fear, Neutral, Greed, and Extreme Greed.",
    body_style
))

elements.append(Spacer(1, 0.3*inch))

# Conclusion
elements.append(Paragraph("Conclusion", heading_style))
elements.append(Paragraph(
    "The analysis reveals clear patterns in trading behavior across different market sentiment conditions. Extreme Greed periods offer "
    "the best profitability but require caution. Fear periods show the highest trading activity, suggesting both opportunity and risk. "
    "Understanding these patterns can help traders develop more informed strategies that adapt to market sentiment conditions.",
    body_style
))

# Build PDF
doc.build(elements)
print(f"PDF report generated: {REPORT_PATH}")

