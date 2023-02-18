# This script extracts song names from a file and writes Spotify search URLs for them to a new file.
# This script is not meant to be imported.

from urllib import parse
import sys

def main():
	# This accepts the absolute location of the source text file as the argument.
	source_file_location = sys.argv[1]

	target_count = 0
	source_count = 0

	with open(source_file_location, encoding="utf-8") as source_file:
		for line in source_file:
			source_count += 1

			# This removes the final \n character from the extracted line.
			song_name = line[:-1]
			
			# This URL-econdes the song_name.
			url_encoded_song_name = parse.quote(song_name)
			
			try:
				with open("URLs.txt", "a") as target_file:
					# This appends the URL to the target file.
					target_file.write(f"https://open.spotify.com/search/{url_encoded_song_name}\n")
			except Exception as e:
				print(e)
			else:
				target_count += 1
	
	print(f"\nNo. of song names extracted: {source_count}")
	print(f"No. of Internet Shortcut files created: {target_count}")


if __name__ == "__main__":
	main()
