p1 = """Text classification is a natural language processing (NLP) 
    technique that involves automatically categorizing text into 
    different classes or categories. It's a powerful tool that can be 
    used in a wide variety of applications, from spam filtering to 
    sentiment analysis and beyond."""

p2 = """At its core, text classification is a supervised learning 
    task. This means that you start with a set of labeled data, where 
    each piece of text is already categorized into one of several 
    classes. You then use this data to train a machine learning model 
    that can automatically classify new, unlabeled text based on its 
    features."""

p3 = """One of the key challenges of text classification is 
    selecting the right features to use. Features are the 
    characteristics of the text that the model will use to make its 
    predictions. These can include things like the presence or absence 
    of certain words or phrases, the length of the text, and the 
    overall structure of the document. The choice of features can have 
    a significant impact on the performance of the model, so it's 
    important to choose features that are relevant to the 
    classification task."""

p4 = """Another important consideration in text classification is 
    the choice of algorithm. There are many different machine learning 
    algorithms that can be used for text classification, each with its 
    own strengths and weaknesses. Common algorithms include Naive 
    Bayes, Support Vector Machines (SVMs), and Decision Trees."""

p5 = """Once you have trained a text classification model, you can 
    use it to automatically categorize new, unlabeled text. This can 
    be useful in a variety of applications, such as filtering spam 
    emails, identifying sentiment in social media posts, or 
    categorizing news articles by topic."""

result = ""
paragraphs = [p1, p2, p3, p4, p5]

for i in paragraphs:
    result += "<p>" + i + "</p> "

text_classification=result
