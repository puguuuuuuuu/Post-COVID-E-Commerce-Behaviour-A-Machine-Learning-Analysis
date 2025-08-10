wcss = []
K_RANGE = range(2, 8)  # try 2..7 clusters
for k in K_RANGE:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    wcss.append(km.inertia_)

plt.figure(figsize=(6,4))
plt.plot(list(K_RANGE), wcss, marker='o')
plt.title('Elbow Method for KMeans')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
plt.grid(True)
plt.tight_layout()
# plt.savefig('figures/fig2_5_elbow.png', dpi=300)
plt.show()
