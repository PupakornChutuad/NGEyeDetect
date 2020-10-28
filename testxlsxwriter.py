import pandas as pd

data = {'Right':[input()],
        'Center':[input()],
        'Left':[input()]}

df = pd.DataFrame(data, columns=['Right','Center','Left'])
print(df)

while data != 0 :
    new_row = {'Right':input(),'Center':input(),'Left':input()}

    df = df.append(new_row ,ignore_index=True)
    df.to_csv("example.csv")

    print(df)