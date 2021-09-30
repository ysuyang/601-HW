from textblob import TextBlob


def get_subjectivity():
    # this sentence is split by "."
    text = "I am happy today. I feel sad today."
    blob = TextBlob(text)

    data = blob.sentences  # [Sentence("I am happy today."), Sentence("I feel sad today.")]
    for d in data:
    # polarity代表情感极性，取值范围是[-1, 1]，-1代表完全负面，1代表完全正面
    # subjectivity代表主观性程度
        print(d.sentiment, ">>>", d)


get_subjectivity()


