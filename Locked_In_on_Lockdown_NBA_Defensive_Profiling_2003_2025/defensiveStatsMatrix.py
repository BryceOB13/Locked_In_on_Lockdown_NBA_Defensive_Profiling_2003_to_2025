import pandas as pd

# File paths
team_abbrev_path = 'data/raw/Team Abbrev.csv'
team_summaries_path = 'data/raw/Team Summaries.csv'
team_stats_per_game_path = 'data/raw/Team Stats Per Game.csv'
opp_stats_per_game_path = 'data/raw/Opponent Stats Per Game.csv'

output_path = 'data/processed/Defensive_Stats_Matrix_2003_2025.csv'

# Load the data
team_abbrev = pd.read_csv(team_abbrev_path)
team_summaries = pd.read_csv(team_summaries_path)
team_stats_pg = pd.read_csv(team_stats_per_game_path)
opp_stats_pg = pd.read_csv(opp_stats_per_game_path)

# Select needed columns
team_abbrev = team_abbrev[['season', 'team', 'abbreviation']]

team_summaries = team_summaries[['season', 'team', 'age', 'w', 'l', 'd_rtg', 'pace',
                                 'opp_e_fg_percent', 'opp_tov_percent', 'opp_ft_fga']]

team_stats_pg = team_stats_pg[['season', 'team', 'drb_per_game', 'stl_per_game', 'blk_per_game', 'pf_per_game']]

opp_stats_pg = opp_stats_pg[['season', 'team',
                             'opp_fg_per_game', 'opp_fg_percent',
                             'opp_x3p_per_game', 'opp_x3p_percent',
                             'opp_x2p_per_game', 'opp_x2p_percent',
                             'opp_ft_per_game', 'opp_fta_per_game',
                             'opp_orb_per_game', 'opp_ast_per_game',
                             'opp_tov_per_game', 'opp_pts_per_game']]

# Merge step-by-step
merged = team_abbrev.merge(team_summaries, on=['season', 'team'], how='left')
merged = merged.merge(team_stats_pg, on=['season', 'team'], how='left')
merged = merged.merge(opp_stats_pg, on=['season', 'team'], how='left')

# Filter out seasons before 2003
merged = merged[merged['season'] >= 2003]

# Sort (optional but cleaner)
merged = merged.sort_values(by=['season', 'team']).reset_index(drop=True)

# Save to processed folder
merged.to_csv(output_path, index=False)

print(f"✅ Defensive stats matrix created and saved to {output_path}")
