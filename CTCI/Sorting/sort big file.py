"""
Imagine you have a 20 GB file with one string per line
Explain how you would sort the file

20G -> do not bring all the data in memory, bring part of the data
we divide the file into chunks, x megabytes each chunk
sort each chunk separately and save back to the file system
Then, we merge the chunks one by one -> fully sorted file

"""