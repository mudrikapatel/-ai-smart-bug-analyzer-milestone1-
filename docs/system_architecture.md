                        +----------------------+
                        |      User (UI/API)   |
                        +----------+-----------+
                                   |
                                   |
                    Bug Description + Stack Trace
                                   |
                                   v
                    +----------------------------+
                    |    Bug Submission Module   |
                    | (Validate & Preprocess)    |
                    +-------------+--------------+
                                  |
                                  |
                           Generate Embeddings
                                  |
                                  v
                    +----------------------------+
                    |      Embedding Model       |
                    | (Sentence Transformers)    |
                    +-------------+--------------+
                                  |
                                  |
                           Vector Embedding
                                  |
                                  v
                    +----------------------------+
                    |       ChromaDB             |
                    |   Vector Database (RAG)    |
                    +-------------+--------------+
                                  |
                     Top-5 Similar Bug Retrieval
                                  |
                                  v
             +-------------------------------------------+
             |         Retrieved Bug Context             |
             +----------------+--------------------------+
                              |
              +---------------+----------------+
              |                                |
              v                                v
      +-------------------+           +----------------------+
      |   Triage Agent    |           |  Root Cause Agent    |
      |-------------------|           |----------------------|
      | • Severity        |           | • Analyze logs       |
      | • Component       |           | • Identify reason    |
      | • Priority        |           | • Explain failure    |
      +---------+---------+           +----------+-----------+
                |                                |
                +---------------+----------------+
                                |
                                v
                  +------------------------------+
                  |      Fix Advisor Agent        |
                  |------------------------------|
                  | • Suggest Fix                |
                  | • Code Recommendation        |
                  | • Best Practices             |
                  +--------------+---------------+
                                 |
                                 |
                                 v
                  +------------------------------+
                  |      Response Generator       |
                  |------------------------------|
                  | Severity                     |
                  | Root Cause                   |
                  | Similar Bugs                 |
                  | Suggested Fix                |
                  | Confidence Score             |
                  +--------------+---------------+
                                 |
                                 v
                      +----------------------+
                      |   UI / API Response  |
                      +----------------------+
