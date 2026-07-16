def is_more_general(h1, h2):
  more_general_parts = []
  for x,y in zip(h1, h2):
    mg = x == "?" or (x != "0" and (x == y or y == "0"))
    more_general_parts.append(mg)
  return all(more_general_parts)

def candidate_elimination(training_data):
  num_attributes = len(training_data[0]) -1
  S = ["0"] * num_attributes
  G = ["?"] * num_attributes
  G = [G]
  S = [S]

  for instance in training_data:
    x, label = instance[:-1], instance[-1]

    if label == "Yes":
      G = [g for g in G if is_more_general(g, x)]
      for i in range(num_attributes):
        if S[0][i] == "0":
          S[0][i] = x[i]
        elif S[0][i] != x[i]:
          S[0][i] = "?"
    else:
      S = [s for s in S if not is_more_general(s, x)]
      new_G = []
      for g in G:
        for i in range(num_attributes):
          if g[i] == "?":
            for val in set(row[i] for row in training_data) - {x[i]}:
              new_hypothesis = g[:]
              new_hypothesis[i] = val
              if any(is_more_general(g, s) for s in S):
                new_G.append(new_hypothesis)
      G = new_G
  return S, G

training_data = [
    ["Some", "Small", "No", "Affordable", "One", "No"],
    ["Many", "Big", "No", "Expensive", "Many", "Yes"],
    ["Many", "Medium", "No", "Expensive", "Few", "Yes"],
    ["Many", "Small", "No", "Affordable", "Many", "Yes"]
]

S_final, G_final = candidate_elimination(training_data)
print("Final Specific Hypothesis:", S_final)
print("Final General Hypothesis:", G_final)
