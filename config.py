import python_flask_dev.packaging.incremental_versioning as iv


# VERSIONING = "manual"
# VERSIONING = "dynamic"
VERSIONING = "automatic"

if __name__ == "__main__":
    iv.IncrementalVersioning(VERSIONING)
