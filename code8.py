residuals = ols.resid
plt.figure(figsize=(6,4))
plt.scatter(ols.fittedvalues, residuals, alpha=0.6)
plt.axhline(0, linestyle='--')
plt.title('Residuals vs Fitted (Regression Diagnostics)')
plt.xlabel('Fitted values'); plt.ylabel('Residuals')
plt.tight_layout()
# plt.savefig('figures/fig2_8_residuals.png', dpi=300)
plt.show()
