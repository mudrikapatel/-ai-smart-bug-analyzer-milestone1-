import pickle
import faiss
import pandas as pd


class BugRetriever:

    def __init__(self):
        self.index = faiss.read_index("faiss_index/bug.index")

        with open("faiss_index/vectorizer.pkl", "rb") as f:
            self.vectorizer = pickle.load(f)

        self.data = pd.read_pickle("faiss_index/bug_data.pkl")

    def search(self, query, top_k=5):

        query_vector = self.vectorizer.transform([query]).toarray().astype("float32")

        distances, indices = self.index.search(query_vector, top_k)

        results = []

        for dist, idx in zip(distances[0], indices[0]):

            if idx == -1:
                continue

            row = self.data.iloc[idx]

            similarity = max(0, (1 - float(dist))) * 100

            results.append({

                "bug_id": row["Bug_ID"],
                "title": row["Title"],
                "severity": row["Severity"],
                "priority": row["Priority"],
                "component": row["Component"],
                "root_cause": row["Root_Cause"],
                "fix": row["Suggested_Fix"],
                "similarity": round(similarity, 2)

            })

        return results