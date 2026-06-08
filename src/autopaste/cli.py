import sys
from autopaste.upload import upload

def main():
  if len(sys.argv) > 1:
    filepath = sys.argv[1]
    try:
      with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    except FileNotFoundError:
      print(f"Error: {filepath} doesn't exist!")
      return 

  else:
    content = input("Paste or Write: ")
    if not content.strip():
      print("Error: Content cannot be empty!")
      return

  link = upload(content)
  print(f"Your pastebin url is: {link}")

