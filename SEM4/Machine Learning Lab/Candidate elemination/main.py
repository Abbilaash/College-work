import pandas as pd

df = pd.read_csv('dataset3.csv')

num_attributes = len(df.columns) - 1 
S = ['ϕ'] * num_attributes
G = [['?'] * num_attributes]


# Candidate Elimination Algorithm
for row in df.itertuples(index=False):  
    print(row)
    instance = row[:-1]
    label = row[-1]

    if label == ' Yes':
        for i in range(num_attributes):
            if S[i] == 'ϕ':
                S = list(instance)
            elif S[i] != instance[i]:
                S[i] = '?'
        G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(num_attributes))]


    elif label == ' No':
        G_new = []
        for g in G:
            for i in range(num_attributes):
                if g[i] == '?':
                    if S[i] != '?':  
                        g_new = g[:i] + [S[i]] + g[i+1:]
                        G_new.append(g_new)

        G = G_new if G_new else G
    

        


# Print final hypotheses
print("Final Specific Hypothesis (S):", S)
print("Final General Hypotheses (G):", G)


# Final Specific Hypothesis: ['Many' '?' ' No' '?' '?']
# Final General Hypothesis: [['Many', '?', '?', '?', '?']]