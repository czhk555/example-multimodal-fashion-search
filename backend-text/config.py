# indexing data
DATA_DIR = "../data/images" # Where are the files?
CSV_FILE = "../data/styles.csv" # Where's the metadata?
WORKSPACE_DIR = "../embeddings"
MAX_DOCS = 100
DEVICE = "cpu"

# PQLiteIndexer
COLUMNS = [
    ("gender", "str"),
    ("masterCategory", "str"),
    ("subCategory", "str"),
    ("articleType", "str"),
    ("baseColour", "str"),
    ("season", "str"),
    ("usage", "str"),
    ("year", "int"),
]
DIMS = 512 # This should be same shape as vector embedding

# serving via REST
SERVER = "0.0.0.0" # remove http://
PORT = 12345

# metas for executors
TIMEOUT_READY = -1 # Wait forever for executor to be ready. Good for slow connections
