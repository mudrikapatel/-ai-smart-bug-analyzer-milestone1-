# -ai-smart-bug-analyzer-milestone1-
# AI Smart Bug Analyzer & Fix Advisor
## Milestone 1: Bug Submission + RAG Pipeline
### **1. Problem Statement**
Manual bug triage is slow. Developers waste 30-40% time searching old similar bugs. No centralized knowledge of past fixes → duplicate bugs → wasted effort.

### **2. Solution Overview**
AI-powered system using RAG (Retrieval-Augmented Generation) + Multi-Agent orchestration:
- **Input**: Bug description + stack trace
- **Output**: Similar bugs, root cause, suggested fix
- **Tech Stack**: FastAPI, Gemini 1.5, ChromaDB, LangChain, Streamlit

### **3. System Architecture**


1. **Bug Submission**: User uploads description + stack trace via UI/API
2. **RAG Pipeline**: Embed query → ChromaDB vector search → top-5 similar bugs
3. **Agents**:
   - **Triage Agent**: Assign severity, component
   - **Root Cause Agent**: Analyze why bug happened
4. **Output**: Display findings + suggested fix

### **4. Milestone 1 Scope**
1. Data Ingestion: 10K Mozilla bugs → ChromaDB
2. RAG Pipeline: Semantic search working <1 sec
3. Backend API: `/submit-bug` endpoint
4. 2 Agents: Triage + Root Cause
5. Demo UI: Streamlit

### **5. Tech Stack**

| Component | Technology | Why? |
| --- | --- | --- |
| Backend | Python + FastAPI | Async, LLM friendly |
| LLM | Gemini 1.5 Flash | Free, 1M context |
| Vector DB | ChromaDB | Local, zero setup |
| RAG | LangChain | Best ecosystem |
| Agents | LangGraph | Multi-agent orchestration |
| UI | Streamlit | Rapid demo |

### **6. How to Run**
1. `pip install -r requirements.txt`
2. Add `GEMINI_API_KEY` in `.env`
3. `python backend/ingest.py` - Load data
4. `uvicorn backend.main:app --reload` - API
5. `streamlit run frontend/app.py` - UI

### **7. Demo Video**


### **8. Next Steps - Milestone 2**
1. Duplicate Detection Agent
2. Remediation Agent (code fix suggestions)
3. Apache/Eclipse datasets
4. Cloud deployment
