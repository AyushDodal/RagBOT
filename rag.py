from llama_index.core.node_parser import SentenceSplitter

def chunkify(file):
  # 1. Convert the UploadedFile (bytes) into LlamaIndex Documents
  reader = PDFReader()
  # ensure cursor is at start
  file.seek(0)
  documents = reader.load_data(file=file)
  
  splitter = SentenceSplitter(chunk_size=1024)
  nodes = splitter.get_nodes_from_documents(documents)
  return nodes
