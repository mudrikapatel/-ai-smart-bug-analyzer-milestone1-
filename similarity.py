import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATASET = "bug_dataset.csv"


def find_similar_bugs(query):

    try:

        df = pd.read_csv(DATASET)


        # Check available columns
        text_columns = []


        for col in df.columns:

            if df[col].dtype == "object":

                text_columns.append(col)



        if len(text_columns) == 0:

            return []



        # Combine all text columns

        df["combined_text"] = df[text_columns].fillna("").agg(
            " ".join,
            axis=1
        )



        vectorizer = TfidfVectorizer(
            stop_words="english"
        )


        vectors = vectorizer.fit_transform(
            df["combined_text"]
        )


        query_vector = vectorizer.transform(
            [query]
        )


        scores = cosine_similarity(
            query_vector,
            vectors
        )[0]



        results = []


        for i, score in enumerate(scores):


            if score >= 0.35:


                results.append({

                    "bug_id":
                    df.iloc[i].get(
                        "bug_id",
                        i+1
                    ),


                    "title":
                    df.iloc[i].get(
                        "title",
                        "Historical Bug"
                    ),


                    "similarity":
                    round(
                        float(score)*100,
                        2
                    ),

                    "fix":
                    df.iloc[i].get(
                    "fix",
                    "Inspect the stack trace, validate input data, and apply the same resolution used for similar historical bugs."
                    )
                })



        results.sort(
            key=lambda x:x["similarity"],
            reverse=True
        )


        return results[:5]



    except Exception as e:

        print("Similarity Error:",e)

        return []