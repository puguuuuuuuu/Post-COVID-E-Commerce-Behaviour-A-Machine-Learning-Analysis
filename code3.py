# 3-day lag of cases
daily['New_Cases_lag3'] = daily['New_Cases'].shift(3)

plt.figure(figsize=(10,5))
plt.plot(daily['Date'], daily['Daily_Sales'], label='Daily Sales')
plt.plot(daily['Date'], daily['New_Cases_lag3'], label='COVID Cases (lag 3 days)')
plt.title('Daily Sales vs COVID-19 Cases (3-day Lag)')
plt.xlabel('Date'); plt.ylabel('Value'); plt.legend(); plt.grid(True)
plt.tight_layout()
# plt.savefig('figures/fig2_2b_sales_vs_cases_lag3.png', dpi=300)
plt.show()
