current_date = df['InvoiceDate'].max()

rfm = (df.groupby('CustomerID')
         .agg(LastPurchase=('InvoiceDate','max'),
              Frequency=('InvoiceNo','nunique'),
              Monetary=('TotalPrice','sum'))
         .reset_index())

rfm['Recency'] = (current_date - rfm['LastPurchase']).dt.days
rfm = rfm[['CustomerID','Recency','Frequency','Monetary']].copy()

# scale features for KMeans
scaler = StandardScaler()
X = scaler.fit_transform(rfm[['Recency','Frequency','Monetary']])
