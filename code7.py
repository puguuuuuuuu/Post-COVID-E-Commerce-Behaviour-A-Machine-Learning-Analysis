# keep rows without NA
d = daily.dropna(subset=['Daily_Sales','New_Cases']).copy()

# optional: log transform sales if skewed
d['log_sales'] = np.log1p(d['Daily_Sales'])

# statsmodels for coefficients + p-values
X = sm.add_constant(d[['New_Cases']])        # baseline model
y = d['log_sales']                           # or use Daily_Sales if you prefer

ols = sm.OLS(y, X).fit()
print(ols.summary())  # keep this for appendix if needed

# save a compact results table
coef_table = pd.DataFrame({
    'term': ['Intercept', 'New_Cases'],
    'coef': [ols.params['const'], ols.params['New_Cases']],
    'p_value': [ols.pvalues['const'], ols.pvalues['New_Cases']],
    'R2': [ols.rsquared, '']
})
# coef_table.to_csv('tables/table2_3_regression_results.csv', index=False)

# plot fitted line on raw scale (for intuition)
lr = LinearRegression().fit(d[['New_Cases']], d['Daily_Sales'])
pred = lr.predict(d[['New_Cases']])

plt.figure(figsize=(7,5))
plt.scatter(d['New_Cases'], d['Daily_Sales'], alpha=0.6, label='Observed')
plt.plot(d['New_Cases'], pred, label='Fitted (Linear)', linewidth=2)
plt.title('Regression: COVID-19 Cases vs Daily Sales')
plt.xlabel('New COVID-19 Cases')
plt.ylabel('Daily Sales')
plt.legend(); plt.grid(True); plt.tight_layout()
# plt.savefig('figures/fig2_7_regression.png', dpi=300)
plt.show()
