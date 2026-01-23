from llama_index.core.node_parser import SentenceSplitter

def chunkify(file):
  splitter = SentenceSplitter(chunk_size=1024)
  nodes = splitter.get_nodes_from_documents(documents)
  return nodes
