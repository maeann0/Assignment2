from Item import item

class mp3(item):

    # Attributes
    Duration = 0
    Artist = ''

    # Methods
    def playExtract(self):
        print(f"Playing a {self.Duration} second extract of {self.Title} by {self.Artist}.")

    def download(self):
        print(f"Downloading {self.Title} by {self.Artist}...")
        print("Download complete.")