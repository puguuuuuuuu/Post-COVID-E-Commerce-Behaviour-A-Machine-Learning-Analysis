# choose k from elbow (e.g., 3)
k = 3
km = KMeans(n_clusters=k, random_state=42, n_init=10)
rfm['Cluster'] = km.fit_predict(X)

# Figure 2.6 — scatter Recency vs Monetary by cluster
plt.figure(figsize=(7,5))
for c in sorted(rfm['Cluster'].unique()):
    subset = rfm[rfm['Cluster'] == c]
    plt.scatter(subset['Recency'], subset['Monetary'], label=f'Cluster {c}', alpha=0.8)

plt.title('Customer Segments (KMeans): Recency vs Monetary')
plt.xlabel('Recency (days since last purchase)')
plt.ylabel('Monetary (total spend)')
plt.legend(); plt.grid(True); plt.tight_layout()
#plt.savefig('figures/fig2_6_kmeans_scatter.png', dpi=300)
plt.show()

# Table 2.2 — segment profiles
segment_means = (rfm.groupby('Cluster')[['Recency','Frequency','Monetary']]
                   .mean().round(2))
print(segment_means)

# segment_means.to_csv('tables/table2_2_segment_means.csv')
