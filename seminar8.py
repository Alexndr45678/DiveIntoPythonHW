import os
import json
import csv
import pickle


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        total_size = sum(os.path.getsize(os.path.join(root, name)) for name in files)
        results.append(
            {
                "path": root,
                "type": "directory",
                "size": total_size,
                "parent": os.path.dirname(root),
            }
        )
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({"path": path, "type": "file", "size": size, "parent": root})
    with open("results.json", "w") as f:
        json.dump(results, f)

    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["path", "type", "size", "parent"])
        for result in results:
            writer.writerow(
                [result["path"], result["type"], result["size"], result["parent"]]
            )

    with open("results.pickle", "wb") as f:
        pickle.dump(results, f)


traverse_directory("/path/to/directory")
