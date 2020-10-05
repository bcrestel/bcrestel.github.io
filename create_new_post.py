#!/usr/bin/env python

import argparse
import datetime
import subprocess
import os

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Parse function arguments.')

	parser.add_argument('title', metavar='title', type=str, nargs=1, help='Title of the new post')
	parser.add_argument('tags', metavar='tags', type=str, nargs='+', help='List of tags for the new post')

	args = parser.parse_args()

	# Create blog post file with correct header
	today = datetime.datetime.today()
	filename = f"{today.year}-{today.month:02d}-{today.day:02d}-" + '_'.join(args.title[0].split(' '))
	file_path = f"_posts/{filename}.md"
	text = (f"---\nlayout: post\ntitle: {args.title[0]}\ntags: {' '.join(args.tags)}\n---\n\n")
	with open(file_path, "w") as file:
		file.write(text)

	# open file in vim
	cmd = os.environ.get('EDITOR', 'vim') + ' ' + file_path
	subprocess.call(cmd, shell=True)
