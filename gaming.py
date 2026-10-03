import pandas as pd

print(' --- PART 1: Pandas Series ---')
scores = [29339, 283290, 793207, 8204294, 793493]
players = pd.Series(scores, index=['NightWolf', 'StarBlaze', 'PixelKING', 'CyberFox', 'IronStorm'])
print(players)

print()
print(' --- Part 2: Pandas DataFrame ---')
data = {
    'player': ['NightWolf', 'StarBlaze', 'PixelKING', 'CyberFox', 'IronStorm'],
    'Level':  [ 39, 89, 38, 83, 84],
    'Score':  [29339, 283290, 793207, 8204294, 793493],
    'Wins':   [ 934, 309, 939, 798, 865]
}

df = pd.DataFrame(data)
print(df)

print()
print(' --- Part 3: accessing Rows ---')
print(df.loc[0])
print('Rows 2 and 3:')
print(df.loc[2:3])

print()
print(' --- Part 4: Reading a csv file ---')
full_df = pd.read_csv('Leaderboard.csv')
print(' First 5 rows (head):')
print(full_df.head(3)) 
print()
print('Last 3 rows (tail):')
print(full_df.tail(3))
print()
print('Dataset info:')
print(full_df.info())
print()
print(' --- Part 5: Cleaning Data ---')
print('Rows with missing values removed (dropna):')
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print('Missing values filled with 0 (fillna):')
filled_df = full_df.fillna(0)
print(filled_df.to_string())