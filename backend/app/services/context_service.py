import json

def build_context(summary):

    return json.dumps(summary, indent=2)