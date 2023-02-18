# This script extracts song names from a file and creates an Internet Shortcut file for them pointing to a (URL-encoded) Spotify search.
# This script is not meant to be imported.

from urllib import parse
import sys

def main():
	# This accepts the absolute location of the source text file as the argument.
	source_file_location = sys.argv[1]

	target_count = 0
	source_count = 0
	skipped_files = []

	with open(source_file_location) as source_file:
		for line in source_file:
			# This removes the final \n character from the extracted line.
			song_name = line[:-1]

			# This URL-econdes the song_name.
			url_encoded_song_name = parse.quote(song_name)

			# This strips the name of characters that may cause problems with file creation.
			shortcut_filename = song_name.strip("\/:*?<>|")
			
			source_count += 1

			try:
				with open(f".\Shortcuts\{shortcut_filename}.url", "x") as target_file:
					# This attempts to create a new .url file for the song.
					target_file.write(f"[InternetShortcut]\n\rURL=https://open.spotify.com/search/{url_encoded_song_name}\n")
			except FileExistsError:
				# This adds the song names, for whom a .url file already exists, to a list.
				skipped_files.append(song_name)

				# This skips the current iteration if a .url file already exists for the song.
				continue
			else:
				target_count += 1
	
	print(f"\nNo. of song names extracted: {source_count}")
	print(f"No. of Internet Shortcut files created: {target_count}")

	if len(skipped_files) > 0:
		print(f"No. of files skipped: {len(skipped_files)}")
		print("\nAs Internet Shortcut files for them already exist, the following songs were skipped:")
		print("\n", skipped_files, "\n")


if __name__ == "__main__":
	main()
