def action_count(df):
    count = df["action"].value_counts()
    print(count)