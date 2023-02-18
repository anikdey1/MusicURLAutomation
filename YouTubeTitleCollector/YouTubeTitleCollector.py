# This script uses the URLs of YouTube videos to extract their names.
# This script is not meant to be imported.

import sys
import requests


def main():
	# This accepts the absolute file location as an argument.
	source_file_location = sys.argv[1]

	source_record_count = 0
	target_record_count = 0

	with open(source_file_location) as source_file:
		for line in source_file:
			source_record_count += 1

			# This removes the final \n from each line.
			url = line[:-1]

			response = requests.get(url)
		
			# This converts the response content from <bytes> to <str>.
			response_html = str(response.content, 'UTF-8')

			# These capture the indices for the content in the title tag without appended "- YouTube".
			opening_index = response_html.index("<title>")+7
			ending_index = response_html.index("</title>")-9

			# This extracts the title of the page.
			html_title = response_html[opening_index:ending_index]

			# This appends the titles to URLs.txt and appends the exceptions to Errors.txt. 
			try:
				with open("Titles.txt", "a") as target_file:
					target_file.write(f"{html_title}\n")
			except Exception:
				with open("Errors.txt", "a") as error_file:
						error_file.write(f"{url}\n")
			else:
				target_record_count += 1

	print("\nRecords extracted:", source_record_count)
	print("Records dumpted:", target_record_count)


if __name__ == '__main__':
	main()
