import os, subprocess, sys

project_name = sys.argv[1].replace("_", " ")
review_list = list()

os.chdir("/home/wtc/my_reviews")
all_reviews = subprocess.run(["wtc-lms", "reviews"], capture_output = True, text = True)
for line in all_reviews.stdout.splitlines():
    if project_name in line:
        review_list.append(line)

print(review_list)