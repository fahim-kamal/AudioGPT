import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def getWordCountAndDelay(file):
    text = file.readline()

    split_text = text.split(" ")
    length = len(split_text)

    delay = file.readline()

    return {"length": length, "delay": delay[0:-2]}


if __name__ == "__main__":
    transcript_delays = []
    GPT_delays = []

    with open("output.txt", 'rt') as file:
        while True:
            res = getWordCountAndDelay(file)
            res2 = getWordCountAndDelay(file)

            if res2["delay"] == "":
                break
            
            transcript_delays.append(round(float(res["delay"]), 4))
            GPT_delays.append(round(float(res2["delay"]), 4))
    
    labels = []
    totals = []

    for i in range(len(transcript_delays)):
        labels.append("Trial " + str(i))

    MAX_SIZE = 8
    if len(labels) <= MAX_SIZE:
        MAX_SIZE = len(labels)
        dif = 0;
    else:
        dif = len(labels) - MAX_SIZE

    data = {'labels': labels[dif:], "TR_delays": transcript_delays[dif:], "GPT_delays": GPT_delays[dif:]}
    df = pd.DataFrame(data)

    X_axis = np.arange(len(df["labels"]))
    plt.bar(X_axis, df['TR_delays'], label='Transcription Delay')
    plt.bar(X_axis, df['GPT_delays'], label='ChatGPT Delay')

    plt.xticks(X_axis, df["labels"])

    plt.title('Delays by Trial')
    plt.xlabel("Trials")
    plt.ylabel("Delay (s)")

    plt.legend()
    plt.savefig('out.png')




    