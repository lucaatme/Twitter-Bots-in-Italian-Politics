import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles, venn3_unweighted


def compare(a, b):
    # intersecate the lists
    return len(set(a).intersection(b))


def compare3(a, b, c):
    # intersecate the lists
    return len(set(a).intersection(b).intersection(c))


with open('botsIdGiuseppeConte.txt') as f:
    conteBots = f.read().splitlines()

with open('botsIdNicolaFratoianni.txt') as f:
    fratoBots = f.read().splitlines()

with open('botsIdSilvioBerlusconi.txt') as f:
    silvioBots = f.read().splitlines()

with open('botsIdEmmaBonino.txt') as f:
    emmaBots = f.read().splitlines()

print("Giuseppe Conte vs Nicola Fratoianni: ", compare(conteBots, fratoBots))
print("Giuseppe Conte vs Silvio Berlusconi: ", compare(conteBots, silvioBots))
print("Giuseppe Conte vs Emma Bonino: ", compare(conteBots, emmaBots))
print("Nicola Fratoianni vs Silvio Berlusconi: ", compare(fratoBots, silvioBots))
print("Nicola Fratoianni vs Emma Bonino: ", compare(fratoBots, emmaBots))
print("Silvio Berlusconi vs Emma Bonino: ", compare(silvioBots, emmaBots))


conteFratoianni = compare(conteBots, fratoBots)
conteBerlusconi = compare(conteBots, silvioBots)
conteBonino = compare(conteBots, emmaBots)
fratoianniBerlusconi = compare(fratoBots, silvioBots)
fratoianniBonino = compare(fratoBots, emmaBots)
berlusconiBonino = compare(silvioBots, emmaBots)

fratoianniBerlusconiBonino = compare3(fratoBots, silvioBots, emmaBots)


# set1 = set(bots)
# set2 = set(bots1)
set3 = set(fratoBots)
set4 = set(silvioBots)
set5 = set(emmaBots)

venn3_unweighted(subsets=(len(fratoBots), len(silvioBots), fratoianniBerlusconi, len(emmaBots), fratoianniBonino, berlusconiBonino, fratoianniBerlusconiBonino),
                 set_labels=('Fratoianni', 'Berlusconi', 'Bonino'),
                 set_colors=("orange", "blue", "red"), alpha=0.7)

plt.show()
