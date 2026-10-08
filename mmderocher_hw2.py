# Max DeRocher
# 10/4/2026
# Homework 2

loan_amount = float(input("Loan amount: $"))
interest_rate = float(input("Interest rate (%):"))
loan_length = int(input("Loan length (years):"))

interest_decimal = interest_rate / 100
int_rate_month = interest_decimal / 12
number_pmts = loan_length * 12
monthly_pmt = (
    loan_amount
    * (int_rate_month * (1 + int_rate_month) ** number_pmts)
    / ((1 + int_rate_month) ** number_pmts - 1)
)

print(f"Monthly payment: ${monthly_pmt:,.2f}")

print(
    f"{'Month':>5}{'Payment':>10}{'Principal':>12}{'Interest':>10}{'Balance':>12}"
)

balance = loan_amount

for month in range(1, number_pmts + 1):
    interest = balance * int_rate_month
    principal_paid = monthly_pmt - interest
    balance = balance - principal_paid
    print(
        f"{month:5}{monthly_pmt:10,.2f} {principal_paid:12,.2f} {interest:10,.2f} {balance:12,.2f}"
    )
