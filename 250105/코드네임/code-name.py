MAX_N = 5
agents = []

class agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

for i in range(0, MAX_N):
    codename, score = input().split()
    score = int(score)
    agents.append(agent(codename,score))

lowest_score= agents[0].score
lowest_score_idx = 0

for i in range(1, MAX_N):
    if lowest_score > agents[i].score:
        lowest_score = agents[i].score
        lowest_score_idx = i

print(agents[lowest_score_idx].codename, agents[lowest_score_idx].score)
