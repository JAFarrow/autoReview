import os, subprocess, sys, random, re

os.chdir("/home/wtc/my_reviews")

project_name = sys.argv[1].replace("_", " ")
review_list = list()

all_reviews = subprocess.run(["wtc-lms", "reviews"], capture_output = True, text = True)
for line in all_reviews.stdout.splitlines():
    if project_name in line:
        review_list.append(line)

random_review = review_list[random.randint(0, len(review_list) - 1)]
random_review_alias = random_review[random_review.find("(")+1:random_review.find(")")]
print(random_review_alias)