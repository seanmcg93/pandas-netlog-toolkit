def filter_logs(df, **kwargs):
    for key, value in kwargs.items():

        if key in df.columns:
            if type(value) != list:
                df = df[df[key] == value]
            else:
                df = df[df[key].isin(value)]
        else: print(f"** {key} is not a valid column name.\n** The valid columns are:\n{df.columns}")

    return df




