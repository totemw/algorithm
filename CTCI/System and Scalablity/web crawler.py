"""
If you were designing a web crawler, how would you avoid
getting into infinite loops? - cycle in graph

- detect cycle (hash for url or content? define difference between pages)
- based on url & content and create a signature
- record the priority based on the signature
 (if similar signature has been crawled, set a low priority)
"""