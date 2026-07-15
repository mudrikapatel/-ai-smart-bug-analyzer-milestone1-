import bug_parser
import triage_agent
from log_analysis_agent import analyze_log
from similarity import find_similar_bugs


def analyze(filepath):

    text = bug_parser.parse_file(filepath)

    triage = triage_agent.analyze_bug(text)

    log = analyze_log(text)

    similar = find_similar_bugs(text)

    return {
        "triage": triage,
        "log_analysis": log,
        "similar_bugs": similar
    }