#imports
import os

#determining file path
absolute_path = os.path.dirname(__file__)
before_path = "before/perfectclear.txt"
after_path = "after/sfx_perfectclear.txt"
full_before_path = os.path.join(absolute_path, before_path)
full_after_path = os.path.join(absolute_path, after_path)

os.rename(full_before_path, full_after_path)
print("renamed")

#if no dir, make dir (default/sfx)

