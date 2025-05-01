
import streamlit as st

def american_odds_to_decimal(american_odds):
    if american_odds > 0:
        return (american_odds / 100) + 1
    else:
        return (100 / abs(american_odds)) + 1

def american_odds_to_probability(american_odds):
    if american_odds > 0:
        return 100 / (american_odds + 100)
    else:
        return abs(american_odds) / (abs(american_odds) + 100)

def calculate_payout_and_profit(stake, decimal_odds):
    total_payout = stake * decimal_odds
    profit = total_payout - stake
    return total_payout, profit

st.title("Betting Odds Calculator")

american_odds = st.number_input("Enter American odds (e.g., +150 or -200)", step=1, format="%d")
stake = st.number_input("Enter your stake amount", min_value=0.0, step=1.0)

if st.button("Calculate"):
    decimal_odds = american_odds_to_decimal(american_odds)
    probability = american_odds_to_probability(american_odds)
    total_payout, profit = calculate_payout_and_profit(stake, decimal_odds)

    st.markdown(f"### Results")
    st.write(f"**Decimal Odds:** {decimal_odds:.2f}")
    st.write(f"**Implied Probability:** {probability * 100:.2f}%")
    st.write(f"**Total Payout:** ${total_payout:.2f}")
    st.write(f"**Profit:** ${profit:.2f}")
