from modelscope.hub.snapshot_download import snapshot_download

snapshot_download(
    'sentence-transformers/all-MiniLM-L6-v2',
    cache_dir='./model_files/all-MiniLM-L6-v2',
    local_dir='./model_files/all-MiniLM-L6-v2'
)