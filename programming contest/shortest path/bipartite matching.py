"""
Settings:
 - n students and d dorms
 - Each student wants to live in one of the dorms of his choice
 - Each dorm can accommodate cj student
Problem: FInd an assignment that maximized the number of students who get a housing

Find the max-flow
 - make an edge with capacity cj from dorm j to the sink
"""