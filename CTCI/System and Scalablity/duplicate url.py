"""
You have duplicate URLS, hoe do you detect th duplicate
URLs? (identical URLs)

- split into 4000 chunks and apply hash function to each chunk,
then in each file, we apply algorithm in memory
- same procedure, but use multiple machines
   - parallelize the operation <> rely 4000 machines running perfectly
"""