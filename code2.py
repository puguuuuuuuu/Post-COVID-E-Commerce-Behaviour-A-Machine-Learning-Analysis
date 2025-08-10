# daily aggregate
daily = (df.groupby(df['InvoiceDate'].dt.date)
           .agg(Daily_Sales=('TotalPrice','sum'),
                Daily_Orders=('InvoiceNo','nunique'),
                New_Cases=('New_Cases','sum'))
           .reset_index()
           .rename(columns={'InvoiceDate':'Date'}))

# ensure sorted by date
daily['Date'] = pd.to_datetime(daily['Date'])
daily = daily.sort_values('Date')

# Figure 2.2
plt.figure(figsize=(10,5))
plt.plot(daily['Date'], daily['Daily_Sales'], label='Daily Sales')
plt.plot(daily['Date'], daily['New_Cases'], label='New COVID Cases')
plt.title('Daily Sales vs COVID-19 Cases')
plt.xlabel('Date'); plt.ylabel('Value'); plt.legend(); plt.grid(True)
plt.tight_layout()
# plt.savefig('figures/fig2_2_sales_vs_cases.png', dpi=300)
plt.show()
