from pytube import Playlist, YouTube
import os

def download_playlist(playlist_url, save_path="/Downloads", resolution="720p"):
    """Downloads all videos from a YouTube playlist in the given resolution."""
    
    # Create folder if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Load the playlist
    playlist = Playlist(playlist_url)
    print(f"\n🎥 Downloading Playlist: {playlist.title} ({len(playlist.video_urls)} videos)")

    for index, video_url in enumerate(playlist.video_urls, start=1):
        try:
            yt = YouTube(video_url)

            # Select the video stream with the desired resolution
            video_stream = yt.streams.filter(res=resolution, progressive=True, file_extension="mp4").first()

            if video_stream is None:  # Fallback to best available quality
                video_stream = yt.streams.get_highest_resolution()
                print(f"⚠️ {yt.title} is not available in {resolution}. Downloading best quality instead.")

            print(f"📥 Downloading {index}/{len(playlist.video_urls)}: {yt.title}...")

            # Download video
            video_stream.download(save_path)
            print(f"✅ Downloaded: {yt.title}\n")

        except Exception as e:
            print(f"❌ Failed to download {video_url}: {e}")

    print("\n🎉 Playlist download complete!")

# Main program
if __name__ == "__main__":
    print("🎬 YouTube Playlist Video Downloader 🎬")
    
    playlist_url = input("Enter YouTube playlist URL: ").strip()
    resolution = input("Enter desired resolution (default 720p, press Enter to skip): ").strip() or "720p"
    save_folder = input("Enter save directory (default 'Downloads', press Enter to skip): ").strip() or "Downloads"

    download_playlist(playlist_url, save_folder, resolution)
