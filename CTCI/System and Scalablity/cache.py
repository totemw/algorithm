"""
Design a caching mechanism to cache the results of the
most recent queries. Be sure to explain how you would update
the cache when data changes

Support two primary functions:
- efficient lookups given a key
- expiration of odd data so that it can be replaced with new data

Steps:
1. single system: linked list / hash table -- merge them
 hash map for query and linked list for storage
2. Expand to many machines - machine has own cache/ copy of cache/ segment of the cache
3. update the results
   eg. URL changed, order of results changed, new pages appear
      can use a separate hash table/ or just crawl each machine's cache
      implement "automatic time-out" - set expired time - ensure all data is periodically refreshed
4. further enhancement
  maybe assign queries to machines based on their values instead of randomly
  may want update some data much more frequently than others - timeouts basd on URLs / topic/ past data
"""