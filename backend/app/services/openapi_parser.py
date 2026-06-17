import yaml

def parse_openapi(file_path):

    with open(file_path, "r") as f:
        spec = yaml.safe_load(f)

    info = spec.get("info", {})
    paths = spec.get("paths", {})

    endpoints = []

    for path, methods in paths.items():

        for method in methods:

            endpoints.append({
                "path": path,
                "method": method.upper(),
                "summary": methods[method].get("summary", "")
            })

    return {
        "title": info.get("title"),
        "version": info.get("version"),
        "endpointCount": len(endpoints),
        "endpoints": endpoints
    }