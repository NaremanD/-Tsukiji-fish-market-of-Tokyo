
def prep_data(df):
    
    df = df.assign(lhw=df["Height"]*df["Height"] * df["Width"])

    X = df[["Length3","Height","Width","lhw"]].values
    y = df["Weight"] .values
    
    
    
    
    return X,y